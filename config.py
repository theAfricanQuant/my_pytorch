
# Learning Pytorch
# in 20234
# (c) Ricky Macharm, MScFE
# https://www.SisengAI.com
#
#
import os
from dotenv import load_dotenv

def set_environment():
    load_dotenv()  # Load environment variables from .env file
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
    WOLFRAM_ALPHA_APPID = os.getenv('WOLFRAM_ALPHA_APPID')
    GOOGLE_KEY = os.getenv('GOOGLE_API_KEY') 
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
    # You can fetch other keys similarly

set_environment()
