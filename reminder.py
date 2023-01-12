import time
from plyer import notification 

if __name__ == '__main__':
    while True:
        print("What shall I remind you about?")
        text = str(input())
        print("In how many minutes?")
        local_time = float(input())
        time.sleep(local_time*60)
        notification.notify (
            title = "all day reminder",
            message = text,          
            timeout = 10
        )
        break

       