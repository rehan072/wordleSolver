
import requests
from bs4 import BeautifulSoup

response = requests.get("https://github.com/3b1b/videos/blob/master/_2022/wordle/data/allowed_words.txt")

doc = BeautifulSoup(response.text, "html.parser")


words_file = open("allowed_words.xls","w")


#tags = doc.find_all("td") #works
index = 1
while index <= 25906:
    words = doc.find_all("td")[index].string
    index += 2
    words = str(words)
    words_file.write(words + "\n")
    print(words)

print("done")