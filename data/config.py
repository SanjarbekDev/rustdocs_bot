from environs import Env

# import os

# BOT_TOKEN=str(os.environ.get('TOKEN'))
# IP=str(os.environ.get("ip"))
# ADMINS=['1672039210']

# DATA_URL=str(os.environ.get("DATABASE_URL"))


# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili


DB_USER=env.str("DB_USER")
DB_PASS=env.str("DB_PASS")
DB_HOST=env.str("DB_HOST")
DB_NAME=env.str("DB_NAME")