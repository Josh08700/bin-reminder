from datetime import date, timedelta


def get_current_date() -> date:
    return date.today()


def get_week_start_date(current_date: date | None = None) -> date:
    reference_date = current_date if current_date is not None else get_current_date()
    return reference_date - timedelta(days=reference_date.weekday())