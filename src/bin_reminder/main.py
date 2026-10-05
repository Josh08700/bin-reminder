from nicegui import ui
from bin_reminder.data import *


def build_ui() -> None:
    with ui.column().classes("w-full max-w-xl mx-auto p-6"):
        ui.label("Bin Reminder").classes("text-3xl font-bold")
        ui.label(f"The week is {get_week_date_range()}")
        ui.label(f"Today is: {get_current_date().strftime('%A')}")
        ui.label(f"This week on Thursday evening you need to take out the {get_bin_for_week()} bin")


ui.run(build_ui, title="Bin Reminder", host="0.0.0.0", port=8080, reload=False)
