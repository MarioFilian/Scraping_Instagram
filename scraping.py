import instaloader
import time
import random
import os
from dotenv import load_dotenv

# 1. Cargar el usuario desde tu .env
load_dotenv()
USERNAME = os.getenv("IG_USERNAME")

if not USERNAME:
    print("❌ Error: No se encontró IG_USERNAME en el archivo .env")
    exit()

# 2. Inicializar Instaloader
L = instaloader.Instaloader()

# 3. Cargar la sesión guardada (¡Esto evita hacer login de nuevo!)
try:
    L.load_session_from_file(USERNAME)
    print(f"✅ Sesión de '{USERNAME}' cargada correctamente.")
except FileNotFoundError:
    print(f"❌ No se encontró el archivo de sesión para {USERNAME}.")
    print("Por favor, ejecuta primero tu script de login para crear la sesión.")
    exit()
except Exception as e:
    print("❌ Error al cargar la sesión:", e)
    exit()

# 4. Configurar el objetivo y extraer datos
TARGET_PROFILE = "goalss_ec"

try:
    # Obtenemos el perfil
    profile = instaloader.Profile.from_username(L.context, TARGET_PROFILE)
    print(f"\n🔍 Extrayendo datos de: @{TARGET_PROFILE}")
    print(f"Seguidores: {profile.followers} | Posts totales: {profile.mediacount}\n")

    # Iteramos sobre los posts
    for i, post in enumerate(profile.get_posts()):
        # Límite: solo extraer los primeros 3 posts para aprender y no saturar
        if i >= 3:
            print("✅ Límite de prueba alcanzado.")
            break

        # Imprimir los datos extraídos
        print(f"--- Post {i+1} ---")
        print(f"URL: https://www.instagram.com/p/{post.shortcode}/")
        print(f"Likes: {post.likes}")
        print(f"Comentarios: {post.comments}")
        print(f"Fecha: {post.date_utc}")
        print("-" * 20)

        # 5. Delay anti-bloqueo (CRÍTICO)
        # Solo esperamos si no es el último post que vamos a revisar
        if i < 2: 
            delay = random.uniform(3.5, 7.2) # Pausa aleatoria entre 3 y 7 segundos
            print(f"⏳ Pausa estratégica de {delay:.2f} segundos...\n")
            time.sleep(delay)

except instaloader.ProfileNotExistsException:
    print(f"❌ El perfil @{TARGET_PROFILE} no existe o está mal escrito.")
except Exception as e:
    print(f"❌ Error durante el scraping: {e}")