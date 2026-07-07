import XCTest

final class JarvisXRVisualProofTests: XCTestCase {
    private var app: XCUIApplication!

    override func setUpWithError() throws {
        continueAfterFailure = false
    }

    override func tearDownWithError() throws {
        app?.terminate()
        app = nil
    }

    func testCaptureRequiredVisualProofScreens() throws {
        launch()
        waitForOrb()
        XCTAssertTrue(app.staticTexts["jarvis.wordmark"].exists)
        XCTAssertFalse(app.staticTexts["Blocked"].exists)
        saveScreenshot("01-standby")

        app.otherElements["jarvis.orb"].tap()
        waitForState("Ready")
        saveScreenshot("02-ready-after-single-tap")

        app.otherElements["jarvis.orb"].tap()
        waitForState("Listening")
        saveScreenshot("03-listening-after-second-tap")

        app.otherElements["jarvis.orb"].tap()
        waitForHintContaining("No speech heard")
        saveScreenshot("05-no-speech-ready")

        app.otherElements["jarvis.orb"].tap()
        waitForState("Listening")
        let input = app.textFields["jarvis.commandInput"]
        input.tap()
        input.typeText("status")
        app.otherElements["jarvis.orb"].tap()
        waitForAnyState(["Speaking", "Done", "Ready"])
        saveScreenshot("04-processing-result-after-command")

        app.otherElements["jarvis.orb"].press(forDuration: 1.0)
        waitForState("Standby")
        saveScreenshot("06-long-hold-standby")

        launch(state: "keyboard")
        waitForOrb()
        app.textFields["jarvis.commandInput"].tap()
        XCTAssertTrue(app.buttons["jarvis.help"].exists)
        XCTAssertTrue(app.buttons["jarvis.meshMenu"].exists)
        saveScreenshot("07-keyboard-open")

        launch()
        waitForOrb()
        app.buttons["jarvis.help"].tap()
        XCTAssertTrue(app.staticTexts["jarvis.help.header"].waitForExistence(timeout: 5))
        saveScreenshot("08-help")

        launch(state: "mesh")
        XCTAssertTrue(app.staticTexts["jarvis.mesh.header"].waitForExistence(timeout: 5))
        saveScreenshot("09-control-mesh")

        launch(state: "inspection")
        XCTAssertTrue(app.staticTexts["jarvis.inspection.status"].waitForExistence(timeout: 5))
        saveScreenshot("10-inspection")

        launch(state: "object_model_missing")
        waitForInspectionStatusContaining("Object model not installed")
        saveScreenshot("11-object-model-missing")

        launch(state: "settings")
        XCTAssertTrue(app.switches["jarvis.settings.speechSwitch"].waitForExistence(timeout: 5))
        saveScreenshot("12-settings")

        launch(state: "diagnostics")
        XCTAssertTrue(app.textViews["jarvis.diagnostics.text"].waitForExistence(timeout: 5))
        saveScreenshot("13-diagnostics")
    }

    private func launch(state: String? = nil) {
        app?.terminate()
        app = XCUIApplication()
        app.launchArguments = ["-JARVIS_UI_TESTING"]
        if let state {
            app.launchArguments += ["-JARVIS_VISUAL_STATE", state]
        }
        app.launch()
    }

    private func waitForOrb() {
        XCTAssertTrue(app.otherElements["jarvis.orb"].waitForExistence(timeout: 8))
    }

    private func waitForState(_ state: String) {
        let label = app.staticTexts["jarvis.state"]
        XCTAssertTrue(label.waitForExistence(timeout: 5))
        let predicate = NSPredicate(format: "label == %@", state)
        expectation(for: predicate, evaluatedWith: label)
        waitForExpectations(timeout: 5)
    }

    private func waitForAnyState(_ states: [String]) {
        let label = app.staticTexts["jarvis.state"]
        XCTAssertTrue(label.waitForExistence(timeout: 5))
        let predicate = NSPredicate { element, _ in
            guard let element = element as? XCUIElement else { return false }
            return states.contains(element.label)
        }
        expectation(for: predicate, evaluatedWith: label)
        waitForExpectations(timeout: 5)
    }

    private func waitForHintContaining(_ text: String) {
        let hint = app.staticTexts["jarvis.hint"]
        XCTAssertTrue(hint.waitForExistence(timeout: 5))
        let predicate = NSPredicate(format: "label CONTAINS %@", text)
        expectation(for: predicate, evaluatedWith: hint)
        waitForExpectations(timeout: 5)
    }

    private func waitForInspectionStatusContaining(_ text: String) {
        let status = app.staticTexts["jarvis.inspection.status"]
        XCTAssertTrue(status.waitForExistence(timeout: 5))
        let predicate = NSPredicate(format: "label CONTAINS %@", text)
        expectation(for: predicate, evaluatedWith: status)
        waitForExpectations(timeout: 5)
    }

    private func saveScreenshot(_ name: String) {
        let screenshot = XCUIScreen.main.screenshot()
        let attachment = XCTAttachment(screenshot: screenshot)
        attachment.name = name
        attachment.lifetime = .keepAlways
        add(attachment)

        guard let directory = ProcessInfo.processInfo.environment["JARVIS_SCREENSHOT_DIR"],
              !directory.isEmpty else { return }
        let url = URL(fileURLWithPath: directory).appendingPathComponent("\(name).png")
        do {
            try FileManager.default.createDirectory(at: url.deletingLastPathComponent(), withIntermediateDirectories: true)
            try screenshot.pngRepresentation.write(to: url)
        } catch {
            XCTFail("Could not write screenshot \(name): \(error)")
        }
    }
}
