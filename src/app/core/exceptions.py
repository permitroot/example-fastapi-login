from fastapi.exceptions import HTTPException
from starlette import status


class BadRequest(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST)


class NotFoundUser(HTTPException):
    def __init__(self, user_id):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user(user_id={user_id}) is not exists.")