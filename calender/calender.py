import calendar

def year_calendar(year):
    for month in range(1, 13):
        print(calendar.month(year, month))

# Example usage:
year_calendar(2024)