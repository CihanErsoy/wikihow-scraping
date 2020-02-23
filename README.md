wikihow-scraping
a web spider built in python's scrapy framework.
I built this web spider to scrape content from wikihow.com website. Spider scrapes the content specifically from Education and Communication page.
The name of the spider is wikwik.py
To run this spider, you need to change your directory to wik. Then, you need to type "scrapy crawl wikwik -o data.json" in your command line.
After you execute wikwik.py file, a json file called data will be created under wik directory. That json file will contain the content that you scraped.
The scraped content is the title of the article and the article itself.
To build a crawler like this;
--download scrapy--
first, you have to run "scrapy startproject wik" command
secondly, you have to build your spider file which is under spiders directory.
thirdly, you have to build items.py file.
lastly, you have to run wikwik.py file by typing "scrapy crawl wikwik -o data.json" in your command line. Make sure you are in the right directory.

so wikwik.py file is written by me.
items.py is created automatically and changed by me.
json file is produced after scraping process is done. This json file is what we aim for.

Important
the name of the spider is important. Make sure you leave the name of the spider as it is, after you create your project by typing "scrapy startproject wik"
If you dont pay attention to this, the json file will appear empty after crawling.
