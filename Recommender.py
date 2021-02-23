import operator


class Recommender():

    def __init__(self , projectName):
        self.__projectName = projectName
        self.__recommenderDirectory = self.__projectName+'/recommenders'
        self.__productDirectory = self.__projectName+'/products'


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

        return sorted(list, key=operator.itemgetter(index), reverse = reverse)