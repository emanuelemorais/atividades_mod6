from fastapi import FastAPI
import uvicorn
from supabase import create_client, Client
from dotenv import load_dotenv
import os
from record import record
from fastapi.responses import HTMLResponse, RedirectResponse

load_dotenv()
url = os.getenv('API_URL')
key = os.getenv('KEY')
bucket_name = "/exercicio_ponderada4"
supabase: Client = create_client(supabase_url=url, supabase_key=key)

app = FastAPI()


@app.get("/")
def read_root():
    return HTMLResponse(content=open("static/index.html", "r").read())


@app.get("/record")
def read():
    filename = record()
    supabase.storage.from_(bucket_name).upload(f'{filename}.mp4', f'./{filename}')
    alert = """
    <head>
        <meta http-equiv="refresh" content="0.5;URL='http://127.0.0.1:8000/'" />
    </head>
    <script>
        alert("Video salvo com sucesso!! :)")
    </script>
    """
    
    return HTMLResponse(content=alert)


if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
#uvicorn main:app --reload