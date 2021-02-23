from Recommender import Recommender
from Crawler import Crawler
from browser import Browser
from file import File



def crawler( searchEngine , projectName , searchContent , activeBrowser , activeCrawler ):


    """

    |--------------------------------------------------
    |                                                 |
    |     Crawler Function                            |
    |                                                 |
    |--------------------------------------------------
    |                                                 |
    |   1 - initial Browser                           |
    |                                                 |
    |                                                 |
    |   2 - Search into browser                       |
    |                                                 |
    |                                                 |
    |   3 - get brands link                           |
    |                                                 |
    |                                                 |
    |   4 - write links into Queue                    |
    |                                                 |
    |                                                 |
    |   5 - Run Crawler                               |
    |                                                 |
    |                                                 |
    ---------------------------------------------------
    |                                                 |
    |  :param  searchEngine:  e.g : GooGle            |
    |                                                 |
    |  :param  projectName:   e.g : mobile.ir_Crawler |
    |                                                 |
    |  :param  searchContent: e.g : mobile.ir         |
    |                                                 |
    ---------------------------------------------------

    """


    file = File()
    crawler = Crawler()

    searchEnginUrl = searchEngine
    content = searchContent
    projectName = projectName

    browserSwich = True
    crawlerSwich = False


    if activeBrowser :
        if browserSwich:
            # ---  1
            browser = Browser(searchEnginUrl, content)


            # ---  2
            browser.search()


            # ---  3
            brandsLinkInfo = browser.getBrandsLink()


            # ---  4
            file.sendLinkstoQueue(projectName, brandsLinkInfo)
            crawlerSwich = True


    if not activeBrowser and  activeCrawler :
        crawlerSwich = True




    if activeCrawler:
        if crawlerSwich :
            # ---  5
            crawler.run(projectName)
        else:
            print("there is no " + projectName  + " file for crawl")




def recommender(projectName):
    recommender = Recommender(projectName)
    recommender.run()





def main():


    searchEnginUrl = 'https://www.google.com/'
    searchContent = 'mobile.ir'
    projectName = 'mobile.ir_Crawler'


    activeBrowser = False
    activeCrawler = False
    activeRecommender = True


    crawler( searchEnginUrl , projectName , searchContent , activeBrowser , activeCrawler)


    if activeRecommender:
       recommender(projectName)






main()






'''
                            
                            This code rewriting started in  1399 - 11 - 25 | 2021 - 2 -13
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""                                                                                                                                            
|                                                                                                                                  |                                                           
|                                                Mohammad Fazel Tajik Saeedi                                                       |                                                                                       
|                                                                                                                                  |               
|                                                                                                                                  |               
|                                                       Dr haghighat                                                               |                                                                               
|                                                                                                                                  |               
|                                                                                                                                  |                                                                       
|                                            Islamic Azad University of QAZVIN                                                     |                                                                                           
|                                                                                                                                  |                                                               
|                                                                                                                                  |                                                                               
|                                         Start : 1399 - 09 - 09‍‍‍‍  | 2020 - 11 - 29                                                 |                                                                                       
|                                         END   : 1399 - 10 - 09  | 2020 - 12 - 29                                                 |                                                                                                   
|                                                                                                                                  |                                                   
|                                                                                                                                  |                                                   
|     #██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████  |                                                                                                                                               
|     #█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███  |                                                                                                                                               
|     #█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███  |                                                                                                                                               
|     #█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███  |                                                                                                                                               
|     #█░░▄▀░░█████████░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░████░░▄▀░░███  |                                                                                                                                               
|     #█░░▄▀░░█████████░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███  |                                                                                                                                               
|     #█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███  |                                                                                                                                               
|     #█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███  |                                                                                                                                               
|     #█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████  |                                                                                                                                               
|     #█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█  |                                                                                                                                               
|     #█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█  |                                                                                                                                               
|     #█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█  |                                                                                                                                               
|     #██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████  |                                                                                                                                               
|                                                                                                                                  |               
|           #██████████████████████████████████████████████████████████████████████████████████████████████████████████████        |                                                                                                                                       
|           #█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█        |                                                                                                                                       
|           #█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█        |                                                                                                                                       
|           #█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█████████░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░░░░░▄▀░░░░░░█        |                                                                                                                                       
|           #█░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████████░░▄▀░░█████        |                                                                                                                                       
|           #█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█████████░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████████░░▄▀░░█████        |                                                                                                                                       
|           #█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████████░░▄▀░░█████        |                                                                                                                                       
|           #█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░██░░▄▀░░█░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████████░░▄▀░░█████        |                                                                                                                                       
|           #█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████████░░▄▀░░█████        |                                                                                                                                       
|           #█░░▄▀░░█████████░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█████░░▄▀░░█████        |                                                                                                                                       
|           #█░░▄▀░░█████████░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████        |                                                                                                                                       
|           #█░░░░░░█████████░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█████░░░░░░█████        |                                                                                                                                       
|           #██████████████████████████████████████████████████████████████████████████████████████████████████████████████        |                                                                                                                                       
|                                                                                                                                  |                       
|                                                                                                                                  |                                                   
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

'''