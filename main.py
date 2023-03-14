import random
import time

questioncount = 10
link = "https://kahoot.it/challenge/01328379?challenge-id=125394b4-cab1-4758-afa8-7774fc3b4bae_1678713359146"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(options=Options())
driver.get(link)
nickname = None
def WaitForQuestion():
    while True:
        try:
            driver.find_element('xpath', '//div[@data-functional-selector="countdown__count"]')
            break
        except:
            continue

def Option(answer):
    i = 0;
    options = driver.find_element('xpath', f"html/body/div/div/div/div/div/div/div/main/div[2]").text.split('\n')
    for option in options:
        i += 1
        if option == answer:
            button = driver.find_element('xpath', f"html/body/div/div/div/div/div/div/div/main/div[2]/button[{i}]")
            button.click()
def GetOptionText(option):
    return driver.find_element('xpath', f"html/body/div/div/div/div/div/div/div/main/div[2]/button[{option}]/span/span").text

def Submit():
    submit = driver.find_element('xpath', "html/body/div/div/div/div/div/div/div/main/div[1]/div[3]/div/button")
    submit.click()
while True:
    try:
        nickname = driver.find_element('xpath', '//input[@id="nickname"]')
        break
    except:
        continue
nickname.send_keys("BotsSuperior"+ str(random.randint(1, 10000)))
time.sleep(1)
go = driver.find_element('xpath', '//button[@type="submit"]')
go.click()
for question in range(1, questioncount + 1):
    WaitForQuestion()
    with open("question" + str(question) + ".txt") as f:
        answers = f.read().splitlines()
        for answer in answers:
            Option(answer)
    Submit()
    while True:
        try:
            nextqn = driver.find_element('xpath', '//button[@data-functional-selector="next-button"]')
            nextqn.click()
            break
        except:
            continue
    while True:
        try:
            scorenextqn = driver.find_element('xpath', '//button[@data-functional-selector="score-next-button"]')
            scorenextqn.click()
            break
        except:
            continue
while True:
    pass