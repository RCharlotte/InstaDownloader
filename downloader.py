import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def download_files(url, destination ):
    import urllib
    resource=urllib.request.urlopen(url)
    filename=destination+url[-8:]+".jpg"
    output=open(filename,"wb")
    output.write(resource.read())



header={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
url= "https://www.instagram.com/rc_ccharlotte/"
response= requests.get(url, headers=header)

response.text

#soup=BeautifulSoup(response.text, "html.parser")

DRIVER_PATH= "C:\seleniumbrowser\chromedriver_win32\chromedriver.exe"

#driver= webdriver.chrome(executable_path = DRIVER_PATH)

s = Service("C:\seleniumbrowser\chromedriver_win32\chromedriver.exe")
s2 = Service("C:\seleniumbrowser\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.instagram.com/rc_ccharlotte/")
driver.implicitly_wait(60)

soup=BeautifulSoup(driver.page_source, "html.parser")

links= []
for a in soup.find_all("a", href= True):
    if a['href'].startswith('/p'):
        links.append("https://www.Instagram.com/" + a['href'])
        print("Link found: https://www.Instagram.com/{0}".format(a['href']))




list(enumerate(links))



for i,j in enumerate(links):
    driver_i = webdriver.Chrome(service=s2)
    driver_i.get(j)
    soup_i=BeautifulSoup(driver_i.page_source, "html.parser")
    image_link=soup_i.find_all("div",{'class':'eLAPa kPFhm'})[0].find_all('img')[0]['src']
    download_files(image_link,'C:/Users/Charlotte/InstagramDownloads/')







#download_files('https://scontent-mba1-1.cdninstagram.com/v/t51.2885-15/274823353_291224023080296_7112917837142817978_n.jpg?stp=dst-jpg_e35&_nc_ht=scontent-mba1-1.cdninstagram.com&_nc_cat=108&_nc_ohc=AqYpsGbWr1wAX8Aj3Ve&edm=AABBvjUBAAAA&ccb=7-4&oh=00_AT9Up8T7jEvTTiKxdvFkmHWS7LhzZcYcZ3WxRsXTo8oGzg&oe=6222A116&_nc_sid=83d603','C:/Users/Charlotte/InstagramDownloads/')