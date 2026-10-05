from nicegui import ui
from nicegui.testing import User


async def test_home_page_shows_app_intro(user: User) -> None:
    await user.open("/")

    await user.should_see("Bin Reminder")
    await user.should_see("Your upcoming bin reminders will appear here.")
