from selenium import webdriver
from selenium.webdriver.common.by import By
import time, io, requests, hashlib, os
from PIL import Image

folder_path=r'C:\Users\91890\Desktop\PythonDatabase\ImageFolder'


def gettingImageLinks(name,numImages):

    browser=webdriver.Firefox()
    browser.get('https://google.com')

    #print(browser)
    input_elem=browser.find_element(By.CSS_SELECTOR,'input.gLFyf')
    input_elem.send_keys(name)
    input_elem.submit()
    time.sleep(2)

    #changeWindow()
    window=browser.window_handles[0]
    browser.switch_to.window(window)
    time.sleep(2)
    
    elem=browser.find_element(By.XPATH,'/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[3]/a')
    elem.click()

    #changeWindow()
    window=browser.window_handles[0]
    browser.switch_to.window(window)
    time.sleep(2)
    
    img_links=[]
    
    img_thumbnail=browser.find_elements(By.CSS_SELECTOR,'img.rg_i.Q4LuWd')
    
    count=0
    
    for i in img_thumbnail:
        if count==int(numImages):
            break
        else:
            count=count+1

        i.click()
        time.sleep(2)
    
        img=browser.find_element(By.XPATH,'/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')
        if(img.get_attribute('src') and ("http" in img.get_attribute('src'))):
            img_links.append(img.get_attribute('src'))

    return img_links

def downloadImage(img_links):
    for url in img_links:
        image_content = requests.get(url).content
        
        try:
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
            with open(file_path, 'wb') as f:
                image.save(f, "JPEG", quality=85)
                print(f"SUCCESS - saved {url} - as {file_path}")
        except Exception as e:
            print(f"ERROR - Could not save {url} - {e}")

def downloadImageOF(name,numImages):
    
    #name,numImages=input("Enter name of the person and number of the images to download separated by ',':- ").split(',')
    #print(f"Name of the person:- {name} \n Number of images to be downloaded:- {numImages}")

    imageLinks=gettingImageLinks(name,numImages)
    #browser.close()
    downloadImage(imageLinks)







