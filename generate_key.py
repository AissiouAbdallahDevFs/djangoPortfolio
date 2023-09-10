import secrets
import base64

# Générer une séquence d'octets aléatoires de 32 octets
random_bytes = secrets.token_bytes(32)

# Encoder les octets en base64 pour obtenir la clé secrète
secret_key = base64.urlsafe_b64encode(random_bytes)

# Afficher la clé secrète
print(secret_key.decode())