import XCTest

final class JarvisXRVisualProofTests: XCTestCase {
    private var app: XCUIApplication!
    private var didCaptureFailureScreenshot = false

    override func setUpWithError() throws {
        continueAfterFailure = false
        didCaptureFailureScreenshot = false
    }

    override func tearDownWithError() throws {
        app?.terminate()
        app = nil
    }

    func testAppLaunchesAndShowsOrb() throws {
        _ = try visualProofDirectory()
        launch()
        waitForOrb()
        waitFor(app.staticTexts["jarvis.wordmark"], named: "JARVIS wordmark")
        saveScreenshot("standby")
    }

    func testCaptureRequiredVisualProofScreens() throws {
        let outputDirectory = try visualProofDirectory()
        print("JARVIS visual proof output: \(outputDirectory.path)")
        printVisualProofEnvironment()

        launch()
        waitForOrb()
        waitFor(app.staticTexts["jarvis.wordmark"], named: "JARVIS wordmark")
        saveScreenshot("standby")

        app.otherElements["jarvis.orb"].tap()
        waitForState("Ready")
        saveScreenshot("ready")

        app.otherElements["jarvis.orb"].tap()
        waitForState("Listening")
        saveScreenshot("listening")

        app.otherElements["jarvis.orb"].tap()
        waitForHintContaining("No speech heard")
        saveScreenshot("no-speech")

        app.otherElements["jarvis.orb"].tap()
        waitForState("Listening")
        let input = app.textFields["jarvis.commandInput"]
        input.tap()
        input.typeText("status")
        app.otherElements["jarvis.orb"].tap()
        waitForAnyState(["Speaking", "Done", "Ready"])
        saveScreenshot("processing")

        app.otherElements["jarvis.orb"].press(forDuration: 1.0)
        waitForState("Standby")
        saveScreenshot("long-hold-standby")

        launch(state: "keyboard")
        waitForOrb()
        app.textFields["jarvis.commandInput"].tap()
        waitFor(app.buttons["jarvis.help"], named: "Help button")
        waitFor(app.buttons["jarvis.meshMenu"], named: "Mesh menu")
        saveScreenshot("keyboard")

        launch()
        waitForOrb()
        app.buttons["jarvis.help"].tap()
        waitFor(app.staticTexts["jarvis.help.header"], named: "Help header")
        saveScreenshot("help")

        launch(state: "mesh")
        waitFor(app.staticTexts["jarvis.mesh.header"], named: "Control Mesh header")
        saveScreenshot("mesh")

        launch(state: "inspection")
        waitFor(app.staticTexts["jarvis.inspection.status"], named: "Inspection status")
        saveScreenshot("inspection")

        launch(state: "object_model_missing")
        waitForInspectionStatusContaining("Object model not installed")
        saveScreenshot("object-model-missing")

        launch(state: "settings")
        waitFor(app.switches["jarvis.settings.speechSwitch"], named: "Settings speech switch")
        saveScreenshot("settings")

        launch(state: "diagnostics")
        waitFor(app.textViews["jarvis.diagnostics.text"], named: "Diagnostics text")
        saveScreenshot("diagnostics")
    }

    private func launch(state: String? = nil) {
        app?.terminate()
        app = XCUIApplication()
        app.launchArguments = ["--jarvis-ui-test"]
        if let state {
            app.launchArguments += ["--jarvis-state", state]
        }
        app.launch()
    }

    private func waitForOrb() {
        waitFor(app.otherElements["jarvis.orb"], named: "JARVIS orb", timeout: 8)
    }

    private func waitForState(_ state: String) {
        let label = app.staticTexts["jarvis.state"]
        waitFor(label, named: "state label")
        let predicate = NSPredicate(format: "label == %@", state)
        expectation(for: predicate, evaluatedWith: label)
        waitForExpectations(timeout: 5)
    }

    private func waitForAnyState(_ states: [String]) {
        let label = app.staticTexts["jarvis.state"]
        waitFor(label, named: "state label")
        let predicate = NSPredicate { element, _ in
            guard let element = element as? XCUIElement else { return false }
            return states.contains(element.label)
        }
        expectation(for: predicate, evaluatedWith: label)
        waitForExpectations(timeout: 5)
    }

    private func waitForHintContaining(_ text: String) {
        let hint = app.staticTexts["jarvis.hint"]
        waitFor(hint, named: "hint label")
        let predicate = NSPredicate(format: "label CONTAINS %@", text)
        expectation(for: predicate, evaluatedWith: hint)
        waitForExpectations(timeout: 5)
    }

    private func waitForInspectionStatusContaining(_ text: String) {
        let status = app.staticTexts["jarvis.inspection.status"]
        waitFor(status, named: "inspection status")
        let predicate = NSPredicate(format: "label CONTAINS %@", text)
        expectation(for: predicate, evaluatedWith: status)
        waitForExpectations(timeout: 5)
    }

    private func waitFor(_ element: XCUIElement, named name: String, timeout: TimeInterval = 5) {
        if !element.waitForExistence(timeout: timeout) {
            print("JARVIS UI test missing element: \(name)")
            print(app.debugDescription)
            XCTFail("Missing \(name). Current UI:\n\(app.debugDescription)")
        }
    }

    private func saveScreenshot(_ name: String) {
        let screenshot = XCUIScreen.main.screenshot()
        let attachment = XCTAttachment(screenshot: screenshot)
        attachment.name = name
        attachment.lifetime = .keepAlways
        add(attachment)

        let directory: URL
        do {
            directory = try visualProofDirectory()
            let url = directory.appendingPathComponent("\(name).png")
            try screenshot.pngRepresentation.write(to: url)
            let attributes = try FileManager.default.attributesOfItem(atPath: url.path)
            let size = attributes[.size] as? NSNumber
            XCTAssertGreaterThan(size?.intValue ?? 0, 0, "Screenshot \(name) was empty at \(url.path)")
            print("JARVIS saved screenshot: \(url.path) size=\(size?.intValue ?? 0)")
        } catch {
            XCTFail("Could not write screenshot \(name): \(error)")
        }
    }

    private func visualProofDirectory() throws -> URL {
        let environment = ProcessInfo.processInfo.environment
        let rawDirectory = environment["VISUAL_PROOF_DIR"] ?? environment["JARVIS_SCREENSHOT_DIR"] ?? derivedVisualProofDirectory()
        guard let rawDirectory, !rawDirectory.isEmpty else {
            throw NSError(
                domain: "JarvisXRVisualProof",
                code: 1,
                userInfo: [NSLocalizedDescriptionKey: "VISUAL_PROOF_DIR or JARVIS_SCREENSHOT_DIR must be set for screenshot proof."]
            )
        }
        let directory = URL(fileURLWithPath: rawDirectory, isDirectory: true)
        try FileManager.default.createDirectory(at: directory, withIntermediateDirectories: true)
        return directory
    }

    private func derivedVisualProofDirectory(filePath: String = #filePath) -> String? {
        let marker = "/ios/JarvisXR/"
        guard let range = filePath.range(of: marker) else { return nil }
        let projectRoot = String(filePath[..<range.upperBound])
        return projectRoot + "build/visual-proof"
    }

    private func printVisualProofEnvironment() {
        let keys = ProcessInfo.processInfo.environment.keys
            .filter { $0.contains("VISUAL") || $0.contains("SCREENSHOT") || $0.contains("GITHUB") || $0.contains("XCTest") }
            .sorted()
        print("JARVIS visual proof environment keys: \(keys.joined(separator: ", "))")
        if let value = ProcessInfo.processInfo.environment["VISUAL_PROOF_DIR"] {
            print("VISUAL_PROOF_DIR=\(value)")
        }
        if let value = ProcessInfo.processInfo.environment["JARVIS_SCREENSHOT_DIR"] {
            print("JARVIS_SCREENSHOT_DIR=\(value)")
        }
    }

    override func record(_ issue: XCTIssue) {
        if !didCaptureFailureScreenshot, app != nil {
            didCaptureFailureScreenshot = true
            saveFailureScreenshot()
            print("JARVIS UI failure current app tree:\n\(app.debugDescription)")
        }
        super.record(issue)
    }

    private func saveFailureScreenshot() {
        let environment = ProcessInfo.processInfo.environment
        guard let rawDirectory = environment["VISUAL_PROOF_DIR"] ?? environment["JARVIS_SCREENSHOT_DIR"],
              !rawDirectory.isEmpty else {
            print("JARVIS could not write failure screenshot because VISUAL_PROOF_DIR was missing.")
            return
        }
        do {
            let directory = URL(fileURLWithPath: rawDirectory, isDirectory: true)
            try FileManager.default.createDirectory(at: directory, withIntermediateDirectories: true)
            let url = directory.appendingPathComponent("failure-current-screen.png")
            try XCUIScreen.main.screenshot().pngRepresentation.write(to: url)
            print("JARVIS saved failure screenshot: \(url.path)")
        } catch {
            print("JARVIS could not write failure screenshot: \(error)")
        }
    }
}
