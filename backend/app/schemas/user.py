from pydantic import BaseModel, EmailStr
from app.enums.user_role import UserRole


class UserBase(BaseModel):
    full_name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.CUSTOMER


class UserResponse(UserBase):
    id: int
    role: UserRole

    model_config = {
        "from_attributes": True
    }