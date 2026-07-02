from app.modules.users.repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    async def get_all_users(self):
        return await self.repository.get_all_users()