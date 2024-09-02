from ninja import NinjaAPI, Schema

api = NinjaAPI()


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    # is not request.user.is_authenticated
    email: str = None


@api.get("/test")
def test(request):
    """
    This endpoint tests if the API is working correctly.

    Parameters:
    - request: The request object.

    Returns:
    - str: The string "test".
    """
    print(request)
    return "test"


@api.get("/user", response=UserSchema)
def user(request):
    print(request)
    return request.user
