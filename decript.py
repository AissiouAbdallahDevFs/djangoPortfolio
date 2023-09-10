from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY2 = os.environ.get("SECRET_KEY2")

fernet = Fernet(SECRET_KEY2.encode())


encrypted_email = b'gAAAAABk_hI2I47bHxfMvFg9BvXXghNLqKfFzHk85Ne6FSWcyHccVHGrwNnx_zW8PQxbpdKkXPn7Ljd9pFhsPqyLFvQlzTFtgME8NB-VbHwVYGVy6jiRtyQ=' # ICI JE MET LES EMAIL CHIFFRÉS
encrypted_message = b'gAAAAABk_hI2MOsg7XeW2a0pnXU3-Es7aaCPkopRX0jrnFjnwFBf-ewamgA-R6Hs49MWBhY7_yXXUkzNT80_qGRPM3YPUWB_eLtVii4O_if6tl7DKhu0his=' # ICI JE MET LES EMAIL CHIFFRÉS


decrypted_email = fernet.decrypt(encrypted_email).decode()
decrypted_message = fernet.decrypt(encrypted_message).decode()

print(decrypted_email)
print(decrypted_message)
