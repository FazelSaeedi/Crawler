import requests
from file import File
from bs4 import BeautifulSoup
import re
import operator
from Brand import Brand



class Crawler:

    def __init__(self):
        self.file = File()




    def run(self, projectName):

        """

        |-------------------------------------------------------------
        |                                                             |
        |                                                             |
        |    create Crawled.txt for Processed links                   |
        |    read brands(links) from queue                            |
        |       for each brand(link) :                                |
        |            get pages of brand for crawl                     |
        |               for each page :                               |
        |                  get productsInfo and                       |
        |                     merge info                              |
        |                                                             |
        |                                                             |
        |       sort array of products and                            |
        |          create a file for store data and                   |
        |             write into it                                   |
        |       remove brand(link) from queue.txt                     |
        |       add brand(link) into crawled.txt                      |
        |                                                             |
        |                                                             |
        |--------------------------------------------------------------
        |                                                             |
        |                                                             |
        |     1 -  create crawled.txt and read queue.txt              |
        |                                                             |
        |     2 -  for each brand(links):                             |
        |                                                             |
        |          2.1 - Modify the data for more readability         |
        |                                                             |
        |          2.2 - Get the number of product pages              |
        |                                                             |
        |          2.3 - New Brand object and array for store         |
        |                          all data of each brand             |
        |                                                             |
        |                                                             |
        |          2.4 - create array for store                       |
        |                         all data of each brand              |
        |                                                             |
        |                                                             |
        |          2.5 - for each page :                              |
        |                                                             |
        |                                                             |
        |                2.5.1 - create page url ,                    |
        |                        send request to it ,                 |
        |                        beautify HTML code                   |
        |                                                             |
        |                                                             |
        |                2.5.2 - parse HTML code and                  |
        |                              get Product Info               |
        |                                                             |
        |                                                             |
        |                2.5.3 - integrate parsed data                |
        |                                                             |
        |                End  for                                     |
        |                                                             |
        |                                                             |
        |          2.6 - sort final Array ORDER BY DESC and           |
        |                     create txt file for                     |
        |                                                             |
        |                                                             |
        |          2.7 - store array into it's file and               |
        |                            remove brand(link) from queue    |
        |                                                             |
        |                                                             |
        |          2.8 - add brand(link) into crawled.txt             |
        |                                                             |
        |                                                             |
        |          End  for                                           |
        |                                                             |
        |                                                             |
        |                                                             |
        |--------------------------------------------------------------
        |                                                             |
        |   :param  projectName                                       |
        |                                                             |
        --------------------------------------------------------------

        """

        # ---  1
        self.file.createCrawledFile(projectName)
        Links = self.file.read_file(projectName + '/queue.txt')

        # ---  2
        for link in Links:

            # ---  2.1
            brandName, LinkUrl = link.split(',')
            LinkUrl = LinkUrl.replace('\n', '')

            # ---  2.2
            pageNumber = self.getPageNumber(LinkUrl)

            # ---  2.3
            brand = Brand(brandName, LinkUrl, pageNumber)

            # ---  2.4
            # array for store all data of eacch brand
            arrayOfproducts = []

            # --- 2.5
            for page in range(1, int(pageNumber) + 1):

                # --- 2.5.1
                url = brand.getLink() + '?page=' + str(page)
                response = self.request(url)
                beautifyResponse = self.beautifyHTML(response.text)

                # --- 2.5.2
                profuctInfo = self.getProductsInfo(self.getPageProducts(beautifyResponse))
                products_rate = profuctInfo[0]
                products_names = profuctInfo[1]
                products_href = profuctInfo[2]

                # --- 2.5.3
                for index, item in enumerate(products_names):
                    integeretedData = [products_names[index], products_rate[index], products_href[index]]
                    arrayOfproducts.append(integeretedData)

            # --- 2.6
            print(arrayOfproducts)
            sortedArray = self.sortListByIndex(arrayOfproducts, 1, True)
            self.file.createFolder(projectName + '/products')

            # --- 2.7
            self.file.addListToFile(projectName + "/products/" + str(brand.getName()) + ".txt", sortedArray)
            self.file.removeLineFromFile(projectName + "/queue.txt", link)
            print(link)

            # --- 2.8
            self.file.addLineToFile(projectName + "/crawled.txt", link)




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




    def getProductName(self , product):

        """

        |--------------------------------------------------
        |                                                 |
        |      from div of each product separate          |
        |                                  a tag          |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |      1 - user BeautifulSoup.select for          |
        |           select one element by id or class     |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |     return a tag element                        |
        |                                                 |
        |--------------------------------------------------


        """

        return product.select('div.info h4 a')




    def getProductRate(self , product):

        """

        |--------------------------------------------------
        |                                                 |
        |      from div of each product separate          |
        |                                div tag          |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |      1 - user BeautifulSoup.select for          |
        |           select one element by id or class     |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |     return a div tag element                    |
        |                                                 |
        |--------------------------------------------------


        """

        return product.select('div.ratestars')