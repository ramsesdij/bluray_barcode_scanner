import requests
import re
from bs4 import BeautifulSoup


class Data:
    def __init__(self, upc):
        self.headers = requests.utils.default_headers()
        self.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
        self.upc = upc

    def search_upc(self):
        url = f"https://www.blu-ray.com/movies/search.php?ean={self.upc}&asin=&casingid=&slipcoverfront=&slipcoverback=&submit=Search&action=search"
        
        cookies = {
            "name": 'country',
            "value": 'all'
        }

        optional = {
            "port": None,
            "domain": '.blu-ray.com',
            "path": '/'
        }
       
        s = requests.Session()
        cookie = requests.cookies.create_cookie(**cookies, **optional)
       
        s.cookies.set_cookie(cookie)
        print(s.cookies)

        response = s.get(url)
        print(s.cookies.get_dict())
        # print(req.cookies)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        h2 = soup.find_all("h2", class_="oswaldcollection")
        a_tag = soup.find_all("a", class_="hoverlink")
       
        movie_name = re.findall(r'(?<=\btitle=")[^"]*', str(a_tag))
        
        print(h2)
        print(movie_name)
