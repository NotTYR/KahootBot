import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(options=Options())
##change it yourself
name = "botss slay   "
## I am a free child labour
questioncount = 10
link = "https://kahoot.it/challenge/125394b4-cab1-4758-afa8-7774fc3b4bae_1679919049723"
driver.get(link)
def WaitForQuestion():
    while True:
        try:
            driver.find_element('xpath', '//div[@data-functional-selector="countdown__count"]')
            break
        except:
            continue

def GetCorrectOptions():
    while True:
        try:
            while True:
                try:
                    driver.find_element('xpath', "//main/div[3]/div[not(@disabled)][1]")
                    break
                except:
                    continue
            options = driver.find_elements('xpath', "//main/div[3]/div[not(@disabled)]")
            print(str(len(options)))
            break
        except:
            continue

def Option(answer):
    i = 0
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

def Username():
    while True:
        try:
            nickname = driver.find_element('xpath', '//input[@id="nickname"]')
            nickname.send_keys(name)
            time.sleep(1)
            go = driver.find_element('xpath', '//button[@type="submit"]')
            go.click()
            break
        except:
            continue
        try:
            spin = driver.find_element('xpath', '//button[@data-functional-selector="namerator-spin-button"]')
            spin.click()
            time.sleep(5)
            okgo = driver.find_element('xpath', '//button[@data-functional-selector="namerator-continue-button"]')
            okgo.click()
            break
        except:
            continue

Username()
for question in range(1, questioncount + 1):
    WaitForQuestion()
    with open("question" + str(question) + ".txt") as f:
        answers = f.read().splitlines()
        for answer in answers:
            Option(answer)
    GetCorrectOptions()
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
