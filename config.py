from dotenv import load_dotenv
import os

from app import app
load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')