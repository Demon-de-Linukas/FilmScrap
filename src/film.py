import requests
from lxml import html as ht


def get_film_list_zkm():
    raw_html = requests.get('https://www.filmpalast.net/programm.html')
    tree = ht.fromstring(raw_html.text)

    film_name = {}


    articels = tree.cssselect("#c203 > div > div > article")
    for articel in articels:
        obj = articel.cssselect("[class='item-link outline']")[0]
        title=obj.attrib['title'].replace(': Vollständige Filminfos anzeigen','')
        href='https://www.filmpalast.net/%s'%obj.attrib['href']
        i_ref=obj.cssselect('img')[0].attrib['data-src']
        img_ref = 'https://www.filmpalast.net/%s' % i_ref
        film_name[title]=[{'href':href,'img_ref':img_ref}]
    return film_name