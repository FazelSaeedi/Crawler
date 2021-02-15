import requests

from bs4 import BeautifulSoup


class Crawler:

    def __init__(self):
        print("this is initial function of Crawler Class")




    def getPageNumber(self, brandUrl):


        """

        |--------------------------------------------------
        |                                                 |
        |    get bace brandUrl and                        |
        |                crawl number of pages            |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |    1 - send request to baceURL of brand         |
        |                and beautify HTML code           |
        |                                                 |
        |    2 - use bs4.select_one for select and parse  |
        |            number of div of paginationbox       |
        |                                                 |
        |    3 - check number of pages and return         |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |   :param  baceBrandUrl  Link                    |
        |                                                 |
        |--------------------------------------------------

        """


        # --- 1
        response = self.request(brandUrl)
        beautifyResponse = self.beautifyHTML(response.text)



        # --- 2
        pageNumber = beautifyResponse.select_one('div.paginationbox').text.split()[-2]



        # --- 3
        pageNumber_isDigit = True
        try:
            num = int(pageNumber)
        except ValueError:
            pageNumber_isDigit = False


        if (pageNumber_isDigit == True):
            pass
        else:
            pageNumber = 1

        return pageNumber




    def beautifyHTML(self, response):

        """

        |--------------------------------------------------
        |                                                 |
        |      use BeautifulSoup library                  |
        |           receive a HTML dirty code             |
        |           beatify dirty HTML code               |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |      1 - BeautifulSoup()  => get 2 parameter    |
        |               1 - dirty HTML code               |
        |               2 - type of parse e.g :           |
        |                     html.parser                 |
        |                     xml.parser                  |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |     :param  response => ( HTML code )           |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |     return beatify of dirty HTML code           |
        |                                                 |
        |--------------------------------------------------

        """

        # --- 1
        return BeautifulSoup(response, 'html.parser')




    def request(self, url):


        """

        |--------------------------------------------------
        |                                                 |
        |      use requests library                       |
        |      send request to :url                       |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |      1 - get(url) => send request to url        |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |     :param  URL of a web page                   |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |     return HTML of Web page                     |
        |                                                 |
        |--------------------------------------------------

        """

        # --- 1
        return requests.get(url)
