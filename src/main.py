"""Main src file"""
from datetime import datetime

def calculate_progress(
    start: datetime, duration: int, reporting_date: datetime
) -> float:
    """This modular function calculates progress in decimal (ratio) based on
    a start, duration and point in time. The start point in time can be used
    either as a planned start to calculated planned progress, or actual
    start to calculate actual progress."""
    return round((reporting_date - start).days / duration, 2)

def calculate_date_variance(planned_start: datetime, actual_start: datetime) -> int:
    """This function calculates a simplified version of the schedule variance, called
    here 'date variance'. It is simply the number of days of variance between planned
    start and actual start of a given task."""
    return (actual_start - planned_start).days

def main():
    """Main func"""

    planned_start = datetime(day=10, month=11, year=2024)
    current_day = datetime(day=16, month=11, year=2024)
    duration: int = 12

    actual_start = datetime(day=12, month=11, year=2024)

    planned_progress = calculate_progress(
        start=planned_start, duration=duration, reporting_date=current_day
    )
    actual_progress = calculate_progress(
        start=actual_start, duration=duration, reporting_date=current_day
    )
    date_variance = calculate_date_variance(
        planned_start=planned_start, actual_start=actual_start
    )

    print(planned_progress)
    print(actual_progress)

    print(date_variance)

if __name__ == "__main__":
    main()
