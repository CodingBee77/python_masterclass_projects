import bcrypt

password = b"my_secure_password_123!."
# Hash the password
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

entered_password = input("Enter your password: ")
entered_password_as_bytes = bytes(entered_password, encoding='utf-8')
if bcrypt.checkpw(entered_password_as_bytes, hashed):
    print("Logging successful ! ")
else:
    print("Logging failed ! ")