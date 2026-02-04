from Counter import Counter


class Clock:
    def __init__(self):
        self.seconds = Counter()
        self.minutes = Counter()
        self.hours = Counter()

    def tick(self):
        self.seconds.increment()

        if self.seconds.get_count() == 60:
            self.seconds.reset()
            self.minutes.increment()

            if self.minutes.get_count() == 60:
                self.minutes.reset()
                self.hours.increment()

                if self.hours.get_count() == 24:
                    self.hours.reset()

    def reset(self):
        self.seconds.reset()
        self.minutes.reset()
        self.hours.reset()

    def get_time(self):
        h = self.hours.get_count()
        m = self.minutes.get_count()
        s = self.seconds.get_count()
        return f"{h:02}:{m:02}:{s:02}"
