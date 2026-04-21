import instaloader
import time
# Inicializar
L = instaloader.Instaloader()

# Perfil 
username = "sweatgym__"

profile = instaloader.Profile.from_username(L.context, username)

# 2 publicaciones
posts = profile.get_posts()

for i, post in enumerate(posts):
    if i >= 2:
        break

    print("Post:", post.shortcode)
    print("Likes:", post.likes)
    print("Comentarios:", post.comments)
    print("Fecha:", post.date)
    print("Caption:", post.caption)
    print("-" * 40)
    time.sleep(3)