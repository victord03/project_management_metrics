from datetime import datetime, timedelta


def calculate_actual_progress(actual_start: datetime.date, reporting_date: datetime.date, duration: int) -> float:
    actual_progress: float = 0.0

    # the percentage between start and finish that the current moment represents

    # % progress = duration -

    return actual_progress


def calculate_planned_progress(planned_start: datetime, duration: int, reporting_date: datetime) -> float:
    return (reporting_date - planned_start).days / duration


def main():

    planned_start = datetime(day=10, month=11, year=2024)
    current_day = datetime(day=16, month=11, year=2024)
    duration: int = 12

    planned_progress = calculate_planned_progress(planned_start, duration, current_day)

    # print(planned_progress)


if __name__ == "__main__":
    main()
