'''Week 08 Team Activity'''
'''Demonstrates inheritance and polymorphism.'''
# NOTE: 2 ways of property -> decorator syntax or property object


class Time:
    """
    Represents a time of day (hours, minutes, seconds).
    """

    def __init__(self):
        self._hours = 0  # _ private variables
        self._minutes = 0
        self._seconds = 0
        # stretch challenge
        self._hours_simple = 0
        self._period = 0

    # HOURS
    def get_hours(self):
        return self._hours

    def set_hours(self, value):
        if value > 23:
            value = 23

        elif value < 0:
            value = 0

        self._hours = value

    # create property object
    hours = property(get_hours, set_hours)

    # HOURS SIMPLE - stretch challenge
    @property
    def hours_simple(self):
        return self._hours_simple

    @hours_simple.setter
    def hours_simple(self, value):
        if value > 23:
            value = 11

        elif value > 12:
            value -= 12

        elif value < 0:
            value = 0

        self._hours_simple = value

    # PERIOD - stretch challenge
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        if value < 12:
            self._period = 'AM'
        else:
            self._period = 'PM'

    # MINUTES
    def get_minutes(self):
        return self._minutes

    def set_minutes(self, value):
        if value > 59:
            value = 59

        elif value < 0:
            value = 0

        self._minutes = value

    # object property
    minutes = property(get_minutes, set_minutes)

    # SECONDS
    def get_seconds(self):
        return self._seconds

    def set_seconds(self, value):
        if value > 59:
            value = 59

        elif value < 0:
            value = 0

        self._seconds = value

    # object property
    seconds = property(get_seconds, set_seconds)


def main():
    """
    Tests the time class.
    """
    # create time object
    time = Time()

    # input
    hours = int(input('Enter hours: '))
    minutes = int(input('Enter minutes: '))
    seconds = int(input('Enter seconds: '))

    time.hours = hours
    time.hours_simple = hours
    time.period = hours
    time.minutes = minutes
    time.seconds = seconds

    # output
    print(f'Hours: {time.hours}')
    print(f'Hours simple: {time.hours_simple} {time.period}')
    print(f'Minutes: {time.minutes}')
    print(f'Seconds: {time.seconds}')


if __name__ == "__main__":
    main()
