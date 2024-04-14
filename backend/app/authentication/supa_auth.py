from supabase import create_client, Client
import dotenv

dotenv.load_dotenv()

import os

# Your Supabase project URL
SUPABASE_URL = os.getenv('SUPABASE_URL')
# Your Supabase anon/public key
SUPABASE_KEY =os.getenv('SUPABASE_KEY')

# Create a Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def sign_in_user_with_Oauth():
    data = supabase.auth.sign_in_with_oauth({
  "provider": 'google'
})

# Function to sign in a user
def sign_in_user(email, password):
    # Attempt to sign in
    data = supabase.auth.sign_in_with_password({"email":email, "password":password})
    
    # Check if sign in was successful
    if data:
        print("Sign in successful!")
        return data
    else:
        print(f"Failed to sign in")
        return None


def force_sign_in_for_testing():
    email=os.getenv('mark_email')
    password=os.getenv('mark_pw')
    data = supabase.auth.sign_in_with_password({"email": email, "password": password})
    return data

def sign_out_user():
     supabase.auth.sign_out()

def get_current_user():
    user = supabase.auth.get_user()
    return user

def get_current_session():
    # Check if there is an active session or user ID
    session = supabase.auth.get_session()
    if not session:
        return get_current_user()
    return session

def authenticate_user(username: str, password: str):
    print(username)
    user=sign_in_user(username,password)
    return user

