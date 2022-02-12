import bs4, requests, pyttsx3, sys

#opening a wikipedia web page to download its contents
print()
print("OPENING THE WIKIPEDIA PAGE!!")
print()
texts=requests.get('https://en.wikipedia.org/wiki/'+' '.join(sys.argv[1:]))
texts.raise_for_status()
print("SEARCHING FOR {} ON WIKIPEDIA!!".format(' '.join(sys.argv[1:])))
print()
print("SEARCH SUCCESFULL!!!")
#parsing the downloaded contents
soup=bs4.BeautifulSoup(texts.text,'html.parser')

#selecting specific elements from parsed content
sentences=soup.select('p')

#converting the selected content to string
str(sentences)

######################################################################################
#printing the length of 2nd element of the list 'sentences'
#print(len(sentences[2]))

#printing the length of text or inner html of the element
#print(len(sentences[2].getText()))

#printing the text at sentences[2]
#print(sentences[2].getText())
########################################################################################

#following is the code to print all the text or inner html contents of 'sentences' and then convert the text to speech

for i in range(5): #we are only reading first five paragrphs but we can read as many as we want
        
        if len(sentences[i].getText())==1:
            continue

        print("THE LENGTH OF THE PARAGRAPH IS :-",len(sentences[i].getText()))
        print()
        print(sentences[i].getText())
        print()

        tts=pyttsx3.init()
    
        temp=True
        while temp==True:
            tospeech=sentences[i].getText()
        
            tts.say(tospeech)
            tts.runAndWait()

            stop=input("ENTER 'q' TO STOP AND EXIT OR 'p' TO CONTINUE TO NEXT PARAGRAPH:-  ")
            if stop=='q':
                sys.exit()
            elif stop=='p':
                temp=False
            else:
                print("INVALID CHOICE!! EXITING PROGRAM!!!")
                sys.exit()

