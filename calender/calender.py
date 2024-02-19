import calendar

def print_year_calendar(year):
    for month in range(1, 13):
        print(calendar.month(year, month))

# Example usage:
print_year_calendar(2024)