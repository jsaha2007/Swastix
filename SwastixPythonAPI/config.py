import os
from dotenv import load_dotenv

load_dotenv()

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/swastix_db")

# App Configuration
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")

# OTP Configuration
OTP_EXPIRY_MINUTES = int(os.getenv("OTP_EXPIRY_MINUTES", "10"))
OTP_LENGTH = int(os.getenv("OTP_LENGTH", "6"))

# Email Configuration (for notifications)
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_EMAIL = os.getenv("SMTP_EMAIL", "your-email@gmail.com")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "your-password")

# SMS Configuration (Twilio or similar)
SMS_API_KEY = os.getenv("SMS_API_KEY", "your-sms-key")
SMS_SENDER = os.getenv("SMS_SENDER", "Swastix")

# Application Settings
APPOINTMENT_REMINDER_HOURS = int(os.getenv("APPOINTMENT_REMINDER_HOURS", "24"))
