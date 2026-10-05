from nicegui import ui


def build_ui() -> None:
    with ui.column().classes("w-full max-w-xl mx-auto p-6"):
        ui.label("Bin Reminder").classes("text-3xl font-bold")
        ui.label("Your upcoming bin reminders will appear here.")


ui.run(build_ui, title="Bin Reminder", host="0.0.0.0", port=8080, reload=False)
