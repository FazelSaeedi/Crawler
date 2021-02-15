import requests

from bs4 import BeautifulSoup
import re
import operator


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




    def sortListByIndex(self , list , index , reverse = True):


        """

        |--------------------------------------------------
        |                                                 |
        |      get a list and a index of list             |
        |                   then sort it                  |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |      1 - sort list by index                     |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |      :param  List(array)                        |
        |                                                 |
        |      :param  index of list(array)               |
        |                                                 |
        |      :param  reverse  ? true   :  false         |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |     return a sorted list                        |
        |                                                 |
        |--------------------------------------------------

        """

        return sorted(list, key = operator.itemgetter(index), reverse = reverse)




    def getPageProducts(self , butifyResponse):

        """

        |--------------------------------------------------
        |                                                 |
        |      get div of phons and parse                 |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |      1 - sort list by index                     |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |     return a parsed html code                   |
        |                                                 |
        |--------------------------------------------------

        """

        # --- 1
        return butifyResponse.select('div.phonesgrid div')




    def getProductsInfo(self , productsOfPage):

        """

        |--------------------------------------------------
        |                                                 |
        |    get a beautiful code of div of all product   |
        |                separate rate name and href      |
        |                         and return              |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |      1 - for each product :                     |
        |                                                 |
        |          1.2 - get product rate                 |
        |                                                 |
        |          1.3 - get product name                 |
        |                                                 |
        |          1.4 - get product hrep                 |
        |                                                 |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |     return 3 array of informations of product   |
        |                                                 |
        |--------------------------------------------------

        """


        products_rate  = []
        products_names = []
        products_href  = []


        # get each product info
        # --- 1
        pre = ''
        for product in productsOfPage:


            product_rate = self.getProductRate(product)
            product_name = self.getProductName(product)
            #product_detail_link = product.select('div span')[1]['data-tipurl']



            # --- 1.2
            for r in product_rate:
                title = r['title']
                rate = re.findall(r'[0-9]+', title)
                #print(rate)
                final_rate = (int(rate[0]) * int(rate[2]))/100
                final_rate = round(final_rate)
                products_rate.append(final_rate)


            # --- 1.3
            # --- 1.4
            for i in product_name:
                name = i.text
                if (name != pre):
                    pre = name
                    products_names.append(name)
                    products_href.append('https://www.mobile.ir' + i['href'])



        return products_rate , products_names , products_href