import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/taskdb")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-secret-change-in-prod")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False