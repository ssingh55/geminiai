import os
os.environ['GOOGLE_API_KEY']="GOOGLEAPIKEY"

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])