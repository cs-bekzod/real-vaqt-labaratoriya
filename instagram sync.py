import instaloader
from datetime import datetime

class GetInstagramProfile():
    def __init__(self) -> None:
        self.L = instaloader.Instaloader()

    def download_user_profile_picture(self,username):
        self.L.download_profile(username, profile_pic_only=True)
        
    def get_user_username(self,user_name):
        profile = instaloader.Profile.from_username(self.L.context, user_name)
        print("Foydalanuvchi username:",profile.username)

    def get_user_followers(self,user_name):
        profile = instaloader.Profile.from_username(self.L.context, user_name)
        print("Followerlar soni:",profile.followers)

    def get_user_followings(self,user_name):
        profile = instaloader.Profile.from_username(self.L.context, user_name)
        print("Followinglar soni:",profile.followees)
        
    def get_user_bio(self,user_name):
        profile = instaloader.Profile.from_username(self.L.context, user_name)
        print("Bio dagi yozuv:",profile.biography)
    
    def get_user_posts(self,user_name):
        profile = instaloader.Profile.from_username(self.L.context, user_name)
        print("Postlari soni:",profile.mediacount)



if __name__=="__main__":
    user = input("Foydalanuvchi nomini kiriting:")
    cls = GetInstagramProfile()
    cls.download_user_profile_picture(user)
    cls.get_user_username(user)
    cls.get_user_followers(user)
    cls.get_user_followings(user)
    cls.get_user_bio(user)
    cls.get_user_posts(user)
   