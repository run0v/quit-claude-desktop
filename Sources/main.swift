import AppKit

let bundleID = "com.anthropic.claudefordesktop"

let apps = NSWorkspace.shared.runningApplications.filter {
    $0.bundleIdentifier == bundleID
}

if apps.isEmpty {
    print("Claude Desktop не запущен")
    exit(0)
}

print("Найдено \(apps.count) процесс(ов) Claude Desktop")

for app in apps {
    print("Завершение PID=\(app.processIdentifier)...")
    app.terminate()
}

Thread.sleep(forTimeInterval: 1.5)

let stillRunning = NSWorkspace.shared.runningApplications.filter {
    $0.bundleIdentifier == bundleID
}

if stillRunning.isEmpty {
    print("Claude Desktop успешно закрыт")
} else {
    print("Принудительное завершение...")
    for app in stillRunning {
        app.forceTerminate()
    }
}
