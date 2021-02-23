import operator
from file import File


class Recommender():

    def __init__(self , projectName):
        self.__projectName = projectName
        self.__recommenderDirectory = self.__projectName+'/recommenders'
        self.__productDirectory = self.__projectName+'/products'



    def run(self):

        """

         array[] MPEP = most popular each product
        |--------------------------------------------------
        |                                                 |
        |       search between products and               |
        |              Recommend  most popular product    |
        |                                                 |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |      1 - create Recommender folder              |
        |                                                 |
        |      2 - get extention of prodect brand file    |
        |                                                 |
        |      3 - for each  brand :                      |
        |                                                 |
        |          3.1 - get first product of each brand  |
        |             and append into most popular array  |
        |                                                 |
        |      4 - sort MPEP array                        |
        |                                                 |
        |      5 - write MPEP into txt file and return    |
        |                                                 |
        |--------------------------------------------------


        """

        # --- 1
        file = File()
        file.createFolder(self.__recommenderDirectory)


        # --- 2
        if(file.isExistDirectory(self.__productDirectory)):
            brandsCrawedNames = file.getFileNameInDir(self.__productDirectory , 'txt')

            MPEP = []
            count = 0

            productCount = 0
            # --- 3
            for brand in brandsCrawedNames:

                # --- 3.1
                brandName = brand.replace('.txt' , '')
                products = file.read_file(self.__productDirectory+'/'+brand)

                brandcount = len(products)
                productCount = productCount + brandcount ;

                product = products[0].replace('\n' , '').replace('[' , '').replace(']' , '').replace("'", '').replace('"' , '')
                x = product.split(",")
                x.append(brandName)

                MPEP.append(x)
                count += 1

            # --- 4
            for index, p in enumerate(MPEP):
                MPEP[index][1] = int(MPEP[index][1])

            MPEP = self.sortListByIndex(MPEP, 1, True)

            for x in MPEP:
                print(x)


            # --- 5
            file.addListToFile(self.__projectName+'/recommenders/'+'TopProduct' + ".txt", MPEP)


            print("--" * 100)
            print("Number of Product : " + str(productCount))

        else:
            return print(self.__productDirectory + '/' + 'is Not Exist ')




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