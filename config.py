import secrets
import os

class Config:
    SECRET_KEY = secrets.token_hex(32)  # Secure key for your app
    DATABASE_NAME = "smart_water_manage"
    DATABASE_USER = "postgres"
    DATABASE_PASSWORD = "Qwerty@34"  # You can move this to an environment variable if preferred
    DATABASE_HOST = "localhost"
    DATABASE_PORT = 5432
    OAUTH2_CLIENT_ID = "your-oauth2-client-id"  # Directly keep it in the config or use a secret manager
    OAUTH2_CLIENT_SECRET = "your-oauth2-client-secret"
    SERVER_METADATA_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    OAUTH2_REDIRECT_URI = 'http://127.0.0.1:5000/auth/google/callback'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465  # Use 587 for TLS
    MAIL_USE_TLS = False  # If using SSL (use True if you're using TLS)
    MAIL_USE_SSL = True  # If using SSL (use False if you're using TLS)
    MAIL_USERNAME = 'your-email@gmail.com'
    MAIL_PASSWORD = 'your-email-password'  # Use app-specific password if using Gmail
    MAIL_DEFAULT_SENDER = 'your-email@gmail.com'
