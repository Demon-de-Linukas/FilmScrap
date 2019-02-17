from src.film import get_film_list_zkm
from src.sendmail import generate_html,send_mail
import time

old_list=get_film_list_zkm()
starttime = time.time()-(60*60*24*7)
newtime=time.time()
while True:
    new_list=get_film_list_zkm()
    for film in new_list:
        if film not in old_list:
            html=generate_html(new_list)
            if send_mail(html):
                starttime=time.time()
                time.sleep(60*60*24*7)
                continue

    newtime=time.time()
    if (newtime-starttime)/3600/24/7 >1:
        html = generate_html(new_list)
        if send_mail(html):
            starttime = time.time()
            time.sleep(60 * 60 * 24 * 7)
            continue