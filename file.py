import os


class File():




        def __init__(self):
            pass




        def read_file(self, address):


            """

            |--------------------------------------------------
            |                                                 |
            |   Read a txt file and return a array            |
            |                                                 |
            |--------------------------------------------------
            |                                                 |
            |    1 - read txt file line by line               |
            |                                                 |
            |-------------------------------------------------|
            |                                                 |
            |   return array                                  |
            |                                                 |
            ---------------------------------------------------

            """

            file1 = open(address, 'r')
            Lines = file1.readlines()
            return Lines




        def createProjectDir(self, directoryName):


            """

            |--------------------------------------------------
            |                                                 |
            |   create Project Directory                      |
            |                                                 |
            |--------------------------------------------------
            |                                                 |
            |    1 - check if not exist create folder         |
            |                                                 |
            |-------------------------------------------------|
            |                                                 |
            |   parameter : name of project                   |
            |                                                 |
            ---------------------------------------------------

            """

            if not os.path.exists(directoryName):
                print('Creating Project' + directoryName)
                os.makedirs(directoryName)




        def sendLinkstoQueue(self, directory, links):


            """

            |--------------------------------------------------
            |                                                 |
            |   get list of links of each brand and           |
            |       save to .txt file                         |
            |                                                 |
            |--------------------------------------------------
            |                                                 |
            |   1 - create project directory                  |
            |                                                 |
            |                                                 |
            |   2 - reinitialize Queue.txt                    |
            |                                                 |
            |                                                 |
            |   3 - create New Queue                          |
            |                                                 |
            |                                                 |
            ---------------------------------------------------
            |                                                 |
            |   :param  directory:  your folder addres        |
            |                                                 |
            |   :param  links:      list of array             |
            |                                                 |
            ---------------------------------------------------

            """

            file = File()

            # ---  1
            if not self.isExistDirectory(directory):
                file.createProjectDir(directory)



            # ---  2
            if os.path.exists(str(directory) + '/queue.txt'):
                os.remove(str(directory) + '/queue.txt')



            # ---  3
            with open(str(directory) + '/queue.txt', 'w') as f:
                for item in links:
                    f.write("%s\n" % item)



        
        def createFolder(self, directoryName):


            """

            |--------------------------------------------------
            |                                                 |
            |   create ordinary folder                        |
            |                                                 |
            |--------------------------------------------------
            |                                                 |
            |   1 - check if folder not exist make folder     |
            |                                                 |
            ---------------------------------------------------
            |                                                 |
            |   parameter : name of directory                 |
            |                                                 |
            |--------------------------------------------------

            """

            if not os.path.exists(directoryName):
                os.makedirs(directoryName)




        def createCrawledFile(self , directory):

            """

            |--------------------------------------------------
            |                                                 |
            |   Create crawled.txt to directory of project    |
            |                                                 |
            |--------------------------------------------------
            |                                                 |
            |   1 - if exist crawled.txt into directory       |
            |                remove it                        |
            |                                                 |
            |                                                 |
            |   2 - create new crawled.txt into directory     |
            |                                                 |
            |                                                 |
            ---------------------------------------------------

            """
            if self.isExistDirectory(directory):
                # ---  1
                if os.path.exists(directory+'/crawled.txt'):
                    os.remove(directory+'/crawled.txt')
                else:
                    # ---  2
                    open(directory + '/crawled.txt', "w+")
            else:
                print("there is no " + directory + " file for crawl")
                exit()




        def isExistDirectory(self, directory):

            """

            |--------------------------------------------------
            |                                                 |
            |   1- check folder is exist or not               |
            |                                                 |
            |--------------------------------------------------
            |                                                 |
            |   parameter : name of directory                 |
            |                                                 |
            |--------------------------------------------------

            """

            # --- 1
            if os.path.exists(directory):
                return True

            return False


