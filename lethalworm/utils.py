from datetime import timedelta

ISO_8601_REGEX = '^(?:[1-9]\d{3}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8])|(?:0[13-9]|1[0-2])-(?:29|30)|(?:0[13578]|1[02])-31)|(?:[1-9]\d(?:0[48]|[2468][048]|[13579][26])|(?:[2468][048]|[13579][26])00)-02-29)T(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d(?:\.\d{1,9})'



def timestamp_to_iso8601(duration_in_seconds:float) -> timedelta:
    return timedelta(
        days=0,
        seconds=int(duration_in_seconds),
        milliseconds=(duration_in_seconds % 1)*1000
    )


def read_file(filename:str):
    with open(filename) as read_file:
        return read_file.readlines()