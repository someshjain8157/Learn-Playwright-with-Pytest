from cryptography.fernet import Fernet

key = Fernet.generate_key()

print("KEY =", key.decode())