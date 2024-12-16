# models/user_model.py
class User:
    users = [
        {"username": "user1", "password": "password1"},
        {"username": "user2", "password": "password2"}
    ]

    @classmethod
    def find_user(cls, username, password):
        for user in cls.users:
            if user['username'] == username and user['password'] == password:
                return user
        return None