from fastapi import FastAPI
import uvicorn
from supabase import create_client, Client
from dotenv import load_dotenv
import os
from record import record

load_dotenv()
url = os.getenv('API_URL')
key = os.getenv('KEY')
bucket_name = "/exercicio_ponderada4"
supabase: Client = create_client(supabase_url=url, supabase_key=key)

app = FastAPI()


@app.get("/")
def read_root():
    filename = record()
    supabase.storage.from_(bucket_name).upload(f'{filename}.mp4', f'./{filename}')
    return {"Vídeo salvo com sucesso!"}

if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
#uvicorn main:app --reload