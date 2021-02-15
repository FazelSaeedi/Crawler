

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