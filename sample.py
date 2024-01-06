import os
import google.generativeai as genai
os.environ['GOOGLE_API_KEY']="GOOGLEAPIKEY"

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])