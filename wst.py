import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#url = "http://localhost:9090/webscrape/"

url = "https://www.reddit.com/r/Fairytail_hentai/"
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url)

yes_btn = driver.find_elements_by_xpath("""/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div/div[2]/a[2]""")[0]
print(yes_btn)
yes_btn.click()

obj = driver.find_elements_by_xpath("""/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div""")[0]


res = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res,"lxml")
#print(soup.prettify())

print("")

titles = soup.findAll("h3")
print(titles)
count_data = soup.findAll("div",class_="_3XFx6CfPlg-4Usgxm0gK8R")
#print(members_count)

members_count_div , online_count_div = count_data[0],count_data[1]

print(f"total members: {members_count_div.text}")
print(f"online members: {online_count_div.text}")


#driver.implicitly_wait(600) # seconds
#driver.quit()

'''
soup = BeautifulSoup(res,'lxml')
fs = soup.findAll("ytd-grid-video-renderer")

for f in fs:
	vid_title = f.find('a',{"id":"video-title"}).text
	print(vid_title)

	print("***********")


soup = BeautifulSoup(res,'lxml')
mem = soup.findAll('div',{"class":"_3XFx6CfPlg-4Usgxm0gK8R"})
print(mem.text)

print('----------------------------------------------------')


url = "https://www.reddit.com/r/politics/"
html = requests.get(url).text

soup = BeautifulSoup(html,"lxml")

members = soup.findAll("div",class_="_3XFx6CfPlg-4Usgxm0gK8R")
print(members)
'''
