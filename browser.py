from selenium import webdriver
import time

class Browser:



    def __init__(self , searchEngin_Url , searchContent):

        self.__searchEngin_Url = searchEngin_Url
        self.__searchContent = searchContent
        self.__browser = webdriver.Firefox()




    def search(self):


        """

        |--------------------------------------------------
        |                                                 |
        |  open search engine and                         |
        |        find content and                         |
        |        open content .                           |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |   1 - open  searchEngin_Url                     |
        |                                                 |
        |   2 - find  searchContent                       |
        |                                                 |
        |   3 - open  searchContent                       |
        |                                                 |
        |--------------------------------------------------

        """

        # ---  1
        self.openSearchEngin()


        # ---  2
        self.findSearchContent()


        # ---  3
        self.openSearchContent()
        print('Search Function Finish')



    def openSearchEngin(self):
        """

        |--------------------------------------------------
        |                                                 |
        |     use Selenium.get                            |
        |                                                 |
        |--------------------------------------------------

        """

        browser = self.__browser
        browser.get(self.__searchEngin_Url)
        print("Get" + '  ->  ' + str(self.__searchEngin_Url))




    def findSearchContent(self):

        """

        |--------------------------------------------------
        |                                                 |
        |   Enter  __searchContent in input               |
        |                              and Click it       |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |   1 - use  find_element_by_name -> Input        |
        |            and write __searchContent            |
        |                                                 |
        |                                                 |
        |   2 - use find_element_by_class_name -> Submit  |
        |            and click                            |
        |                                                 |
        ---------------------------------------------------

        """

        # ---  1
        browser = self.__browser
        browser.find_element_by_name('q').send_keys(self.__searchContent)
        time.sleep(3)


        # ---  2
        browser.find_element_by_class_name('gNO89b').click()
        print("Get" + '  ->  ' + str(self.__searchEngin_Url) + '  ->  ' + 'Search ' + '  ->  ' + str(self.__searchContent))




    def openSearchContent(self):

        """

        |--------------------------------------------------
        |                                                 |
        |   use find_element_by_xpath -> __searchContent  |
        |       and click it                              |
        |                                                 |
        |--------------------------------------------------

        """

        browser = self.__browser
        browser.find_element_by_xpath('//a[@href="https://www.'+self.__searchContent+'/"]').click()

        print('Crawler Search ' + '  ->  ' + str(self.__searchContent))
        print('Crawler Open ' + '  ->  ' + str(self.__searchContent))

        time.sleep(4)