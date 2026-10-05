from nicegui import ui
from bin_reminder.data import get_current_date


def build_ui() -> None:
    with ui.column().classes("w-full max-w-xl mx-auto p-6"):
        ui.label("Bin Reminder").classes("text-3xl font-bold")
        ui.label("Today is:",get_current_date().strftime("%A"))
        ui.label("This week you need to take out the () bin")


ui.run(build_ui, title="Bin Reminder", host="0.0.0.0", port=8080, reload=False)
