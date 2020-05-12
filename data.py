import requests
import re
from bs4 import BeautifulSoup


class Data:
    def __init__(self, upc):
        self.headers = requests.utils.default_headers()
        self.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
        self.upc = upc
        self.s = requests.Session()

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
       

        cookie = requests.cookies.create_cookie(**cookies, **optional)
       
        self.s.cookies.set_cookie(cookie)

        response = self.s.get(url)
        print(self.s.cookies.get_dict())

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # h2 = soup.find_all("h2", class_="oswaldcollection")
        a_tag = soup.find_all("a", class_="hoverlink")
       
        movie_name = re.findall(r'(?<=\btitle=")[^"]*', str(a_tag))
        movie_url = re.findall(r'(?<=\bhref=")[^"]*', str(a_tag))

        self.fetch_nation(movie_url)

        return movie_name

    def fetch_nation(self, movie_url):
        response = self.s.get(movie_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        nation = soup.find(lambda tag: tag.name == "img" and "flag" in tag.src)

        print(nation)
        # nation = soup.find_all("img", src_="")