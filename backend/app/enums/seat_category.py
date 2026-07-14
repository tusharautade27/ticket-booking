import enum


class SeatCategory(str, enum.Enum):
    VIP = "VIP"
    PREMIUM = "PREMIUM"
    STANDARD = "STANDARD"