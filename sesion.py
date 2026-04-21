from dotenv import load_dotenv
import os
import instaloader

# Cargar variables de entorno
load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

L = instaloader.Instaloader()

try:
    print("Iniciando sesión...")
    L.login(USERNAME, PASSWORD)

    print("Guardando sesión...")
    L.save_session_to_file()

    print("Sesión guardada correctamente")

except Exception as e:
    print("Error en login:", e)