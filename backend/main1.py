from fastapi import FastAPI
import os
from dotenv import load_dotenv
from supabase import create_client
load_dotenv()

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)
@app.get("/")
def get_users_data():
   
    response = supabase.table("users").select("*").execute()
    if response.data:
        return response.data[0]
    return {"error": "No data found in Supabase"}
