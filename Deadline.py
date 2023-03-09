from datetime import datetime, timedelta

class Deadline():
    def deadline(self, days_before_deadline):
        return datetime.now() + timedelta(days=days_before_deadline)