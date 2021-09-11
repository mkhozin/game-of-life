import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_need_a_secret_key'
