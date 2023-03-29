import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(options=Options())
randomlyGeneratedNumber = str(random.randint(1, 10000))
##change it yourself
name = "俊熙"
raresymbol = "HJASHDFJdasbfncUCFHcfhdsdjhbg"
anotherone = "iumcuiucn47yasducfngshzdfg"
## I am a free child labour
questioncount = 10
link = "https://kahoot.it/challenge/125394b4-cab1-4758-afa8-7774fc3b4bae_1679919021819"
allanswers = []
def WaitForQuestion():
    while True:
        try:
            driver.find_element('xpath', '//div[@data-functional-selector="dialog-actions"]/button').click()
            Username()
        except:
            pass
        try:
            driver.find_element('xpath', '//div[@data-functional-selector="countdown__count"]')
            break
        except:
            continue
def GetCorrectOptions():
    with open("answer.txt", 'w') as text:
        while True:
            try:
                while True:
                    try:
                        driver.find_element('xpath', "//main/div[3]/div")
                        time.sleep(1)
                        break
                    except:
                        continue
                options = driver.find_elements('xpath', "//main/div[3]/div[not(@disabled)]")
                correctoptions = []
                for option in options:
                    correctoptions.append(option.text)
                allanswers.append(raresymbol.join(correctoptions))
                text.write(anotherone.join(allanswers))
                break
            except:
                continue

def AnswerList():
    with open("answer.txt") as slay:
        return slay.read().split(anotherone)

def OptionOTTF(number):
    button = driver.find_element('xpath', f"html/body/div/div/div/div/div/div/div/main/div[2]/button[{number}]")
    button.click()
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
    try:
        submit = driver.find_element('xpath', "html/body/div/div/div/div/div/div/div/main/div[1]/div[3]/div/button")
        submit.click()
    except:
        pass

def Username():
    while True:
        try:
            notme = driver.find_element('xpath', '//button[@data-functional-selector="challenge-progress__cancel"]')
            notme.click()
        except:
            pass
        try:
            nickname = driver.find_element('xpath', '//input[@id="nickname"]')
            nickname.send_keys(name + " " + randomlyGeneratedNumber)
            while True:
                try:
                    go = driver.find_element('xpath', '//button[@type="submit"]')
                    go.click()
                    break
                except:
                    pass
            break
        except:
            pass
        try:
            spin = driver.find_element('xpath', '//button[@data-functional-selector="namerator-spin-button"]')
            spin.click()
            time.sleep(5)
            okgo = driver.find_element('xpath', '//button[@data-functional-selector="namerator-continue-button"]')
            okgo.click()
            break
        except:
            pass
def Next():
    while True:
        try:
            nextqn = driver.find_element('xpath', '//button[@data-functional-selector="next-button"]')
            nextqn.click()
            break
        except:
            continue
    while True:
        try:
            driver.find_element('xpath', '//div[@data-functional-selector="time-left"]')
            break
        except:
            pass
        try:
            scorenextqn = driver.find_element('xpath', '//button[@data-functional-selector="score-next-button"]')
            scorenextqn.click()
            break
        except:
            continue


driver.get(link)
Username()
for question in range(questioncount):
    WaitForQuestion()
    OptionOTTF(1)
    Submit()
    GetCorrectOptions()
    Next()
driver.get(link)
Username()
for question in range(questioncount):
    WaitForQuestion()
    answerlist = AnswerList()
    if len(answerlist) <= question:
        answers = []
    else:
        answers = answerlist[question].split(raresymbol)
    for answer in answers:
        Option(answer)
    Submit()
    Next()
