import cv2
import datetime


def record():

    video = cv2.VideoCapture(0)

    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    size = (frame_width, frame_height)

    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_file_name = "assets/output_{}.mp4".format(current_time)

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
    cv2.destroyAllWindows()
    
    return output_file_name
    