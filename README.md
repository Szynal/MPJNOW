

# Kurs: Metody przetwarzania języka naturalnego oraz wyszukiwanie (Projekt i Laboratorium)


##  PWR - 2 semestr - MGR

      Prowadzący: Jakub Klikowski

### lab2 

 * Creating a project
     ```bash
        scrapy startproject tutorial
     ```

 * This will create a tutorial directory with the following contents:
     ```bash
      tutorial/
        scrapy.cfg            # deploy configuration file
    
        tutorial/             # project's Python module, you'll import your code from here
            __init__.py
    
            items.py          # project items definition file
    
            middlewares.py    # project middlewares file
    
            pipelines.py      # project pipelines file
    
            settings.py       # project settings file
    
            spiders/          # a directory where you'll later put your spiders
                __init__.py

     ```
   * How to run our spider
    ```bash
       scrapy crawl quotes
    ```
    
      Dokumentacja (lab2):
      
      * <https://gazetawroclawska.pl/wiadomosci/>
      * <https://docs.scrapy.org/en/latest/intro/install.html>
      * <https://docs.scrapy.org/en/latest/intro/tutorial.html>
      * <https://blog.hubspot.com/website/how-to-inspect>
      * <https://docs.scrapy.org/en/latest/topics/spiders.html?highlight=rule#crawlspider>
      * <https://docs.python.org/3/library/json.html>

  
