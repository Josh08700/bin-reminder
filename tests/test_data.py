from datetime import date

from bin_reminder.data import get_current_date, get_week_start_date


def test_get_current_date_returns_today() -> None:
    assert get_current_date() == date.today()


def test_get_week_start_date_returns_monday() -> None:
    assert get_week_start_date(date(2026, 10, 7)) == date(2026, 10, 5)


def test_get_week_start_date_returns_same_date_when_monday() -> None:
    assert get_week_start_date(date(2026, 10, 5)) == date(2026, 10, 5)
