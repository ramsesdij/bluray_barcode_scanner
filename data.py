import requests
import re
from bs4 import BeautifulSoup


class Data:
    movie_name = None
    pub_nation = None

    def __init__(self, upc):
        self.headers = requests.utils.default_headers()
        self.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
        self.upc = upc
        self.s = requests.Session()
        self.set_cookies_session()
        self.find_movie()

    def set_cookies_session(self):
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

    def find_movie(self):
        url = f"https://www.blu-ray.com/movies/search.php?ean={self.upc}&asin=&casingid=&slipcoverfront=&slipcoverback=&submit=Search&action=search"

        response = self.s.get(url)
        print(self.s.cookies.get_dict())

        soup = BeautifulSoup(response.content, 'html.parser')
        a_tag = soup.find_all("a", class_="hoverlink")
       
        name = re.findall(r'(?<=\btitle=")[^"]*', str(a_tag))

        if name:
            year = re.findall(r'\(.*\)', str(a_tag))
            print(year)
            name = name[0].replace(' ' + year[0], '')

            self.movie_name = name
            print("FOUND MOVIE NAME: " + self.movie_name)

            name_url = re.findall(r'(?<=\bhref=")[^"]*', str(a_tag))

            if name_url:
                self.find_nation(name_url[0])

    def find_nation(self, movie_url):
        response = self.s.get(movie_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        td = soup.find_all('td', {'width': '518'})
        nation = re.findall(r'(?<=\btitle=")[^"]*', str(td))

        if nation:
            self.pub_nation = nation[0]
            print("FOUND NATION: " + self.pub_nation)

    def get_all_data(self):
        return self.movie_name, self.pub_nation
