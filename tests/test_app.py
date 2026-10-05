from nicegui import ui
from nicegui.testing import User

from bin_reminder.data import get_current_date


async def test_home_page_shows_app_intro(user: User) -> None:
    await user.open("/")

    await user.should_see("Bin Reminder")
    await user.should_see(get_current_date().strftime("%A"))
