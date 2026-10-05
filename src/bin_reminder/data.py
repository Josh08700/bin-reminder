from datetime import date, timedelta

BLACK_BIN_WEEK_START = date(2026, 10, 5)


def get_current_date() -> date:
    return date.today()


def get_week_start_date(current_date: date | None = None) -> date:
    reference_date = current_date if current_date is not None else get_current_date()
    return reference_date - timedelta(days=reference_date.weekday())


def get_week_date_range(week_date: date | None = None) -> str:
    week_start = get_week_start_date(week_date)
    week_end = week_start + timedelta(days=6)
    return f"{week_start:%d %B} - {week_end:%d %B}".lower()


def get_bin_for_week(week_date: date | None = None) -> str:
    reference_date = week_date if week_date is not None else get_current_date()
    week_start = get_week_start_date(reference_date)
    weeks_since_black_week = (week_start - BLACK_BIN_WEEK_START).days // 7
    return "black" if weeks_since_black_week % 2 == 0 else "green"