
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

s = Service("/Users/rehan/Documents/sixdegrees_project/chromedriver")
chrome_driver_binary = "/Users/rehan/Documents/sixdegrees_project/chromedriver"

driver = webdriver.Chrome(service = s)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver.maximize_window()
driver.get("https://www.nytimes.com/games/wordle/index.html")

global word_test
word_test = "earth" ## use information theory to figure best words that go into this array, priority queue


def inputting_words(words_index):
    sliced_letter = []
    #individual splicing
    for i in range(0,len(words_index)): ##iterating through a string
            sliced_letter.append(words_index[i])
        
    for i in range(0,5):
        letter = sliced_letter[i]
        letter_XPATH = "//button[@data-key= '{}']".format(letter)
        letter_input = driver.find_element(By.XPATH,letter_XPATH)
            #clicking_input
        driver.execute_script("arguments[0].click();",letter_input)

    #finding and clicking enter
    enter_key = driver.find_element(By.XPATH,"//button[@data-key= '↵']")
    driver.execute_script("arguments[0].click();",enter_key)
    time.sleep(5)


rowNum = 0
def detection():
    global rowNum
    rowNum += 1 
    global data_state
    data_state = []
    for i in range(0,500,100):
        tiles_XPATH = driver.find_element(By.XPATH,"//div[@class= 'Row-module_row__dEHfN'][{}]//div[@style= 'animation-delay: {}ms;']//div[@class= 'Tile-module_tile__3ayIZ']".format(rowNum,i))
        data_state.append(tiles_XPATH.get_attribute("data-state"))
    print(data_state)
    return data_state








#present_letterCount('p',4, present_letterCount('a', 2, present_letterCount('h',1,present_letterCount('h',4, present_letterCount('a', 1, present_letterCount('p', 2, all_words))))))
