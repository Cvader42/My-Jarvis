from datetime import datetime, timedelta

class ReminderManager:
    def __init__(self):
        self.reminders = []
        self._repeating_reminders = {}

    def set_reminder(self, message, time, is_repeating=False, repeat_interval=timedelta(minutes=15)):
        reminder_time = datetime.now() + timedelta(seconds=time)
        if is_repeating:
            self._repeating_reminders[reminder_time] = (message, repeat_interval)
        else:
            self.reminders.append((reminder_time, message))

    def check_reminders(self):
        current_time = datetime.now()
        for reminder_time, message in self.reminders:
            if current_time >= reminder_time:
                speak(f"Reminder: {message}")
                self.reminders.remove((reminder_time, message))

        # Check for repeating reminders
        for reminder_time, (message, repeat_interval) in self._repeating_reminders.items():
            if current_time >= reminder_time:
                # The reminder has expired, so reschedule it
                reminder_time += repeat_interval
                self.set_reminder(message, reminder_time, is_repeating=True)


