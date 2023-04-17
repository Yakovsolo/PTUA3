# Task Nr.3:

# Create a class called TimeUtils that has a static method called time_to_seconds that takes a time string in the
# format hh:mm:ss and returns the total number of seconds represented by that time. Use functional programing paradigm.


class TimeUtils:
    @staticmethod
    def time_to_seconds(time_str) -> str:
        hours, minutes, seconds = map(int, time_str.split(":"))
        seconds_in_time_str = hours * 3600 + minutes * 60 + seconds
        return f"There are {seconds_in_time_str} seconds in {hours}h {minutes}min and {seconds}sec"


print(TimeUtils.time_to_seconds("23:24:11"))

# Output:
# There are 84251 seconds in 23h 24min and 11sec
