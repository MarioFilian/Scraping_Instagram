import instaloader

loader = instaloader.Instaloader()
profile = instaloader.Profile.from_username(loader.context, "natgeo") 

print("Username:", profile.username)
print("Bio:", profile.biography)
print("Followers:", profile.followers)
print("Posts:", profile.mediacount)