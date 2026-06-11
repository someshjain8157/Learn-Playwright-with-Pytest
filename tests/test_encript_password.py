from cryptography.fernet import Fernet

key = b"mSOsopcw5PtndQQxRK8p3c0PJ_I5yHKN6E-Qi3zjIdg="
cipher = Fernet(key)

encrypted_password = cipher.encrypt(
    b"SuperSecretPassword!"
)

print("ENCRYPTED PASSWORD =", encrypted_password.decode())