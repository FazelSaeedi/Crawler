from selenium import webdriver


class Browser:



    def __init__(self , searchEngin_Url , searchContent):

        self.__searchEngin_Url = searchEngin_Url
        self.__searchContent = searchContent
        self.__browser = webdriver.Firefox()