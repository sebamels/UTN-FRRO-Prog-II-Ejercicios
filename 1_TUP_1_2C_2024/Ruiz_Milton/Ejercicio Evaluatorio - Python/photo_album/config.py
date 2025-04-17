import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'tp_python'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "photo_album.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
