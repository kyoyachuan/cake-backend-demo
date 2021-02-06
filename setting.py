import os


class Setting:
    AIRTABLE_BASE_KEY = os.getenv('AIRTABLE_BASE_KEY')
    AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY')

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
