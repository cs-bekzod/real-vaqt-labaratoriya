import time
import asyncio
import instaloader

class GetInstagramProfile():
    def __init__(self) -> None:
        self.L = instaloader.Instaloader()

    async def download_user_profile_picture(self,username):
        self.L.download_profile(username, profile_pic_only=True)
        
    async def get_user_username(self,user_name):
        profile = instaloader.Profile.from_username(self.L.context, user_name)
        print("Foydalanuvchi username:",profile.username)

    async def get_user_followers(self,user_name):
        profile = instaloader.Profile.from_username(self.L.context, user_name)
        print("Followerlar soni:",profile.followers)

    async def get_user_followings(self,user_name):
        profile = instaloader.Profile.from_username(self.L.context, user_name)
        print("Followinglar soni:",profile.followees)
        
    async def get_user_bio(self,user_name):
        profile = instaloader.Profile.from_username(self.L.context, user_name)
        print("Bio dagi yozuv:",profile.biography)
    
    async def get_user_posts(self,user_name):
        profile = instaloader.Profile.from_username(self.L.context, user_name)
        print("Postlari soni:",profile.mediacount)


async def main():
    users_number = int(input("Foydalanuvchilar sonini kiriting:"))
    users_list = []

    for i in range(users_number):
        user = input(f'{i+1} - foydalanuvchi nomini kiriting:')
        users_list.append(user)
    
    cls = GetInstagramProfile()
    for usr in users_list:
        await asyncio.gather(cls.download_user_profile_picture(usr),cls.get_user_username(usr),cls.get_user_followers(usr),cls.get_user_followings(usr),cls.get_user_bio(usr),cls.get_user_posts(usr))
        time.sleep(1)
        print('-----------------------------------------')

asyncio.run(main())
    # user = input("Foydalanuvchi nomini kiriting:")
    # cls.download_user_profile_picture(user)
    # cls.get_user_username(user)
    # cls.get_user_followers(user)
    # cls.get_user_followings(user)
    # cls.get_user_bio(user)
    # cls.get_user_posts(user)
   