

# There are six files as of now:-
## 1. Signing in to ieeexplore account using selenium(ieeexplore_signin.py)
- In this program selenium is used to open Firefox browser and then go to ieeexplore page and sign in using username and password
- You will require 'geckodriver.exe' to open Firefox

## 2. Reading Contents from Wikipedia page using command prompt(readContentsFromWikipedia.py):-
- This program takes topic to be searched from comand prompt and then searches for the topic on wikipedia
- After searching it downloads the content from wikipedia and prints the texts of the paragraph on the searched page
- After printing it converts the text to speech using pyttsx3

## 3. Scraping Mens T-shirts from shopclues.com:-
- Details like tshirt name, product id, price, sizes available, print pattern & color family and tshirt link is scraped from the mens section of the website
- Scraped details are then stored in to a csv file, creating an unprocessed dataset for further use
- Only 20 tshirts are scraped but more can be scraped depending on the needs

## 4. Scraping top 250 movies from IMDB website:-
- The program opens top 250 movies chart webpage of IMDB and scraps the name, year and links for each movie
- After scraping all the links the program opens all the links one by one to scrap a brief summary about the movie
- This process is repeated until all 250 movies are scraped and the final details are zipped and stored into a list

##5. Download Sports Celebrity Image:- (DownloadImageSportsCelebrity.py and sportsCelebrityImages.py)
-There are two files for this program. DownloadImageSportsCelebrity.py imports the second file sportsCelebrityImages.py and then passes the required arguments to the functions of second file for the desired results.
-First, the porgram opens google's images section to scrap links of images and store them
-Then, it downloads the contents from the links to form the Images
-At last all the images are stored at a particular folder specified by the folder's path
