import bcrypt

# Hashing with bcrypt
def hash_password_bcrypt(password):
    # Convert the password to bytes
    password_bytes = password.encode()
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password

# Verifying a password against a hashed password
def check_password_bcrypt(password, hashed_password):
    # Convert the password to bytes
    password_bytes = password.encode()
    # Check if the password matches the hashed password
    return bcrypt.checkpw(password_bytes, hashed_password)