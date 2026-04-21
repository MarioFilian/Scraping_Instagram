import instaloader
import time
import random

# Inicializar
L = instaloader.Instaloader()

#Debe ser el mismo username con el que hiciste login
USERNAME = "mario.filian"

# Cargar sesión
try:
    L.load_session_from_file(USERNAME)
    print("Sesión cargada")
except Exception as e:
    print("No se pudo cargar la sesión:", e)
    exit()

# Perfil objetivo
TARGET_PROFILE = "sveltygym"

try:
    profile = instaloader.Profile.from_username(L.context, TARGET_PROFILE)
    print(f"Extrayendo datos de: {TARGET_PROFILE}")

    for i, post in enumerate(profile.get_posts()):
        if i >= 2:
            break

        print({
            "post": post.shortcode,
            "likes": post.likes,
            "comments": post.comments,
            "date": str(post.date)
        })

        #Delay anti-bloqueo
        delay = random.uniform(2, 5)
        print(f"Esperando {delay:.2f} segundos...\n")
        time.sleep(delay)

except Exception as e:
    print("❌ Error en scraping:", e)