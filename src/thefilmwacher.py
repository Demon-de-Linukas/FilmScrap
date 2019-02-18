import sys
sys.path.append('D:\Workspace\FilmScrap/src/')
from film import get_film_list_zkm,get_film_list_uni
from sendmail import generate_html,send_mail
import time

old_list=get_film_list_zkm()
starttime = time.time()-(60*60*24*7)
zkm_list=get_film_list_zkm()
uni_list=get_film_list_uni()
html_zkm = generate_html(zkm_list)
html_uni = generate_html(uni_list)
send_mail(html_zkm, True)
send_mail(html_uni, False)

# newtime=time.time()
# while True:
#     new_list=get_film_list_zkm()
#     for film in new_list:
#         if film not in old_list:
#             html=generate_html(new_list)
#             if send_mail(html):
#                 starttime=time.time()
#                 time.sleep(60*60*24*7)
#                 continue
#
#     newtime=time.time()
#     if (newtime-starttime)/3600/24/7 >1:
#         html = generate_html(new_list)
#         if send_mail(html):
#             starttime = time.time()
#             time.sleep(60 * 60 * 24 * 7)
#             continue