import calendar

class AdvancedCalendar:
    def __init__(self):
        self.cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
        self.month_names = calendar.month_name[1:]
    
    def get_month(self, year, month):
        return self.cal.monthdayscalendar(year, month)
    
    def get_month_name(self, month):
        return self.month_names[month - 1]

# Example usage
if __name__ == "__main__":
    advanced_calendar = AdvancedCalendar()
    year = 2023
    month = 8
    month_name = advanced_calendar.get_month_name(month)
    month_days = advanced_calendar.get_month(year, month)
    
    print(f"Calendar for {month_name} {year}:")
    for week in month_days:
        for day in week:
            if day == 0:
                print("   ", end=" ")
            else:
                print(f"{day:2d}", end=" ")
        print()

