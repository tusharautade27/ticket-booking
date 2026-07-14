import enum


class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    ORGANIZER = "ORGANIZER"
    CUSTOMER = "CUSTOMER"