from app.services.user_service import UserService

class UserController:

    def create_user(user_credentials):
        return UserService.create_user(user_credentials)

    def log_in_user(user_credentials):
        return UserService.log_in_user(user_credentials)