import time
from datetime import datetime as dt

host_temp = "hosts"
host_path = "C:\Windows\System32\drivers\etc\host"
redirect = "127.0.0.1"
website_list = ["www.youtube.com, youtube.com, netflix.com, www.netflix.com"]

while True:
    if dt(dt.now().year,dt.now().month, dt.now().day, 8) < dt.now() < dr(dt.now().year,dt.now().month, dt.now().day, 16):
        print("working hours...")
        with open(host_temp,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ ''+ website+'\n')    
    else:
        with open(host_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("fun hours")
    time.sleep(5)
