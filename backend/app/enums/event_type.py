import enum


class EventType(str, enum.Enum):
    MOVIE = "MOVIE"
    CONCERT = "CONCERT"