import os


class Setting:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    HOSTNAME = os.getenv('HOSTNAME')
    DATABASE_URL = os.getenv('DATABASE_URL').replace('postgres://', 'postgresql://')
    CLOUDINARY_URL = os.getenv('CLOUDINARY_URL')
