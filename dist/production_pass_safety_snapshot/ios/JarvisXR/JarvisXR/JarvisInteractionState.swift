import Foundation
import UIKit

enum JarvisInteractionState: String {
    case standby = "Standby"
    case ready = "JARVIS ready"
    case listening = "Listening"
    case heardYou = "Heard you"
    case processing = "Processing"
    case speaking = "Speaking"
    case done = "Done"
    case inspection = "Inspection"
    case quiet = "Quiet"
    case blocked = "Blocked"
}

enum JarvisIntent: String {
    case ready
    case visionInspection
    case readText
    case barcodeScan
    case objectDetection
    case deviceStatus
    case memory
    case controlMesh
    case settings
    case voice
    case unsupported
}

struct JarvisAssistantDecision {
    let intent: JarvisIntent
    let plan: JarvisCommandPlan?
    let response: JarvisResponse
}

final class JarvisAssistantCore {
    private let router: JarvisCommandRouter
    private let planner: JarvisCommandPlanner

    init(router: JarvisCommandRouter = JarvisCommandRouter(), planner: JarvisCommandPlanner = JarvisCommandPlanner()) {
        self.router = router
        self.planner = planner
    }

    func decide(_ rawCommand: String) -> JarvisAssistantDecision {
        let plan = planner.plan(rawCommand)
        let normalized = plan.normalizedCommand
        if normalized == "jarvis ready" || normalized == "ready" {
            return JarvisAssistantDecision(
                intent: .ready,
                plan: plan,
                response: .ok("JARVIS ready.", display: "JARVIS ready.", data: ["mode": "ready"])
            )
        }
        let response = router.route(JarvisCommand(rawCommand))
        return JarvisAssistantDecision(intent: classify(normalized, response: response), plan: plan, response: response)
    }

    func normalize(_ command: String) -> String {
        var value = command
            .lowercased()
            .replacingOccurrences(of: "’", with: "'")
            .replacingOccurrences(of: "what's", with: "what is")
            .replacingOccurrences(of: "whats", with: "what is")
        value = value
            .components(separatedBy: CharacterSet(charactersIn: ",.?;!\""))
            .joined(separator: " ")
        for prefix in ["hey jarvis ", "okay jarvis ", "ok jarvis ", "jarvis "] {
            if value.hasPrefix(prefix) {
                value = String(value.dropFirst(prefix.count))
                break
            }
        }
        return value
            .components(separatedBy: .whitespacesAndNewlines)
            .filter { !$0.isEmpty }
            .joined(separator: " ")
    }

    private func classify(_ command: String, response: JarvisResponse) -> JarvisIntent {
        if response.data["action"] == "inspect" || response.data["action"] == "open_camera" {
            if response.data["vision"] == "ocr" {
                return .readText
            }
            if response.data["vision"] == "object_model_required" {
                return .objectDetection
            }
            return .visionInspection
        }
        if response.data["action"] == "control_mesh" || response.data["url_scheme"] != nil {
            return .controlMesh
        }
        if response.data["action"] == "settings" {
            return .settings
        }
        if command.contains("battery") || command.contains("status") || command.contains("diagnostics") {
            return .deviceStatus
        }
        if command.contains("note") || command.contains("remember") || command.contains("memory") {
            return .memory
        }
        if command.contains("voice") || command.contains("speaking") || command.contains("quiet") {
            return .voice
        }
        return response.status == .ok ? .deviceStatus : .unsupported
    }
}

struct JarvisKeyboardLayoutResult {
    let compact: Bool
    let inputBottomInset: CGFloat
    let orbWidthMultiplier: CGFloat
    let orbMaxWidth: CGFloat
    let orbCenterYOffset: CGFloat
    let titleTopInset: CGFloat
    let transientAlpha: CGFloat
}

enum JarvisXRLayoutModel {
    static let designWidth: CGFloat = 414
    static let designHeight: CGFloat = 896

    static func layout(
        screenHeight: CGFloat,
        safeTop: CGFloat,
        safeBottom: CGFloat,
        keyboardOverlap: CGFloat
    ) -> JarvisKeyboardLayoutResult {
        let keyboardVisible = keyboardOverlap > 20
        if keyboardVisible {
            let bottomInset = keyboardOverlap + 10
            let usableHeight = max(360, screenHeight - safeTop - bottomInset)
            let compactOrbMax = min(212, usableHeight * 0.34)
            return JarvisKeyboardLayoutResult(
                compact: true,
                inputBottomInset: bottomInset,
                orbWidthMultiplier: 0.46,
                orbMaxWidth: compactOrbMax,
                orbCenterYOffset: -usableHeight * 0.20,
                titleTopInset: 10,
                transientAlpha: 0.72
            )
        }
        return JarvisKeyboardLayoutResult(
            compact: false,
            inputBottomInset: safeBottom > 0 ? 14 : 18,
            orbWidthMultiplier: 0.74,
            orbMaxWidth: 320,
            orbCenterYOffset: -68,
            titleTopInset: 20,
            transientAlpha: 1.0
        )
    }
}
