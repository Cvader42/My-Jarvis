"""
Module to implement the AdvancedCalendar class for advanced calendar operations.
"""

import calendar

class AdvancedCalendar:
    """
    Class to perform advanced calendar operations using the calendar module.
    """

    def __init__(self):
        self.cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
        self.month_names = calendar.month_name[1:]

    def get_month(self, year, month):
        """
        Get the calendar representation of a specific month.
        """
        return self.cal.monthdayscalendar(year, month)

    def get_month_name(self, month):
        """
        Get the name of a specific month.
        """
        return self.month_names[month - 1]

# Example usage
if __name__ == "__main__":
    advanced_calendar = AdvancedCalendar()
    input_year = 2023
    input_month = 8
    month_name = advanced_calendar.get_month_name(input_month)
    month_days = advanced_calendar.get_month(input_year, input_month)

    print(f"Calendar for {month_name} {input_year}:")
    for week in month_days:
        for day in week:
            if day == 0:
                print("   ", end=" ")
            else:
                print(f"{day:2d}", end=" ")
        print()
