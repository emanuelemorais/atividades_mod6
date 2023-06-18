import cv2
from supabase import create_client, Client
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv('API_URL')
key = os.getenv('KEY')
bucket_name = "/exercicio_ponderada4"
supabase: Client = create_client(supabase_url=url, supabase_key=key)

print("Conexão estabelecida")  


video = cv2.VideoCapture(0)

frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)

current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
output_file_name = "output_{}.mp4".format(current_time)

result = cv2.VideoWriter(output_file_name, cv2.VideoWriter_fourcc(*'mp4v'), 10, size)
    
while(True):
    ret, frame = video.read()
  
    if ret == True: 
        result.write(frame)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break
  

video.release()
result.release()

res = supabase.storage.from_(bucket_name).upload(f'{output_file_name}.mp4', f'./{output_file_name}')
print("Salvo com sucesso")

cv2.destroyAllWindows()
   
