from datetime import datetime


def calculate_planned_progress(planned_start: datetime.date, duration: int, reporting_date: datetime.date):
    return duration - (planned_start - reporting_date)


def main():

    planned_start = datetime(day=12, month=11, year=2024)
    current_day = datetime(day=12, month=11, year=2024)
    duration = 4

    planned_progress = calculate_planned_progress(planned_start, duration, current_day)

    print(planned_progress)


if __name__ == "__main__":
    main()
