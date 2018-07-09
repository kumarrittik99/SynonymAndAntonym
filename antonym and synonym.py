import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.synonym.com/synonyms/?term="
word = input("Enter word to find its antonym and synonym.\n")
url = url + word

csvFile = open("AntonymAndSynonym.csv","a+")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["Word","Synonyms","Antonyms","link"])

synonym = []
antonym = []

try:
    data = requests.get(url)
    soup = BeautifulSoup(data.text,"html.parser")

    print("Synonyms of the entered word are:\n")

    for synonyms in soup.find_all('li',{'class':'syn'}):
        synonym.append(synonyms.a.text)
        print(synonyms.a.text,end=" ")


    print("\n\n")

    print("Antonyms of the entered word are:\n")

    for antonyms in soup.find_all("li",class_="ant"):
        antonym.append(antonyms.a.text)
        print(antonyms.a.text,end=" ")


    csvWriter.writerow([word,synonym,antonym,url])

    csvFile.close()



except:
    print("Enter a valid word !!! The word you enter does not belong to the dictionary.")


