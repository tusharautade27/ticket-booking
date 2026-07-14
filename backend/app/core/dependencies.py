from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.core.config import settings
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    print("\n" + "=" * 70)
    print("get_current_user() called")
    print("=" * 70)
    print("Received Token:")
    print(token)

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        print("\nDecoded Payload:")
        print(payload)

        email = payload.get("sub")

        print("\nExtracted Email:")
        print(email)

        if email is None:
            print("\nERROR: 'sub' not found in token")
            raise credentials_exception

    except JWTError as e:
        print("\nJWT Decode Error:")
        print(str(e))
        raise credentials_exception

    print("\nSearching user in database...")

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    print("Database Result:")
    print(user)

    if user is None:
        print("\nERROR: User not found")
        raise credentials_exception

    print("\nAuthentication Successful")
    print("=" * 70)

    return user