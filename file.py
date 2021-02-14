import os


class File():




        def __init__(self):
            pass




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


