import os
from dotenv import load_dotenv


class Env:
    def __init__(self):
        load_dotenv()
        self.tv_user = os.getenv('TV_USER')
        self.tv_pass = os.getenv('TV_PASS')