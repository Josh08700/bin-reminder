from datetime import date

from bin_reminder.data import get_bin_for_week, get_current_date, get_week_start_date


def test_get_current_date_returns_today() -> None:
    assert get_current_date() == date.today()


def test_get_week_start_date_returns_monday() -> None:
    assert get_week_start_date(date(2026, 10, 7)) == date(2026, 10, 5)


def test_get_week_start_date_returns_same_date_when_monday() -> None:
    assert get_week_start_date(date(2026, 10, 5)) == date(2026, 10, 5)


# Tests for color of bin.


def test_get_bin_for_anchor_week_is_black() -> None:
    assert get_bin_for_week(date(2026, 10, 5)) == "black"


def test_get_bin_alternates_to_green_the_following_week() -> None:
    assert get_bin_for_week(date(2026, 10, 12)) == "green"


def test_get_bin_alternates_back_to_black_after_two_weeks() -> None:
    assert get_bin_for_week(date(2026, 10, 19)) == "black"


def test_get_bin_is_consistent_for_any_date_in_the_same_week() -> None:
    assert get_bin_for_week(date(2026, 10, 5)) == "black"
    assert get_bin_for_week(date(2026, 10, 11)) == "black"
    assert get_bin_for_week(date(2026, 10, 12)) == "green"


def test_get_bin_alternates_for_weeks_before_anchor_week() -> None:
    assert get_bin_for_week(date(2026, 9, 28)) == "green"
    assert get_bin_for_week(date(2026, 9, 21)) == "black"
