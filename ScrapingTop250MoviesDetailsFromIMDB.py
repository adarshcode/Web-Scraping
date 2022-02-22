from selenium import webdriver
from selenium.webdriver.common.by import By

#Opening the Firefox browser and getting contents from the provided link
browser=webdriver.Firefox()
browser.get('https://www.imdb.com/chart/top')

movie_name=[] #list to store all top movie's name
movie_year=[] #list to store all top movie's year
movie_summary=[] #list to store all top movie's summary
random_list=[] #to store 10 random movie's name, year and summary


movie_details=browser.find_elements(By.CLASS_NAME,'titleColumn')
print(len(movie_details)) #number of movies present in the top chart

for i in movie_details:
    name=i.find_element(By.TAG_NAME,'a') #extracting name
    year=i.find_element(By.TAG_NAME,'span') #extracting year
    movie_name.append(name.text) #storing name
    movie_year.append(year.text) #storing year

movie_link=[] #to store links of every element so that details can be extracted from every movie's link

for i in movie_details:
    name=i.find_element(By.TAG_NAME,'a')
    movie_link.append(name.get_attribute('href'))

for link in movie_link:
    browser.get(link)
    summary=browser.find_element(By.CLASS_NAME,'GenresAndPlot__TextContainerBreakpointXL-sc-cum89p-2')
    movie_summary.append(summary.text)

final_list=list(zip(movie_name,movie_year,movie_summary,movie_link)) #zipping all the data into a list


browser.close() #closing the browser after scraping all the informations