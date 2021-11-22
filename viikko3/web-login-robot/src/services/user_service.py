import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
        elif len(username) <= 3:
            raise UserInputError("Username is too short. Minimum lenght is 3")
        elif re.search('[0-9]',password) is None or len(password) <= 5:
            raise UserInputError("Password is unvalid. Make sure password contains atleast 1 digit and is atleast 5 characters long.")
        self.checkPassword(password,password_confirmation)
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

    def checkPassword(self, password, password2):
        if password != password2:
            raise UserInputError("Passwords do not match together")


user_service = UserService()
