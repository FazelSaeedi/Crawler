
class Brand:
    def __init__(self , name ,link , pageNumber):
        self.__link = link
        self.__name = name
        self.__pageNumber = pageNumber




    def setName(self , name):
        self.__name = name

    def getName(self):
        return self.__name




    def setLink(self , link):
        self.__link = link

    def getLink(self):
        return self.__link




    def setPageNumber(self , pageNumber):
        self.__pageNumber = pageNumber

    def getPageNumber(self):
        return self.__pageNumber


