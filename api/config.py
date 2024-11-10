import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')  # Default secret key
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to save resources
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///goalview.db')  # Database URI

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    MAX_ITEMS = 100  # Maximum number of items for bulk insertion

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    MAX_ITEMS = 50  # Lower max items in production to prevent large inserts

class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = True
    MAX_ITEMS = 10  # Lower max items in testing to handle test cases easily
