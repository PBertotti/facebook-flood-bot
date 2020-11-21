#-----------------------
# Author: Paulo B. Bertotti
# Date: 04/09/2020
# Brief: Facebook comment bot
#-----------------------

#Creating Selenium web server and importing dependencies;
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time, json

#Creating functional driver constant for chrome;
driver = Chrome()

#Creating break for facebook algorithym;
def messageBreak():
    message = ['Voce', 'esta', 'sendo', 'atacado', 'pelo', '[PauloBot]']

    for let in message:
        let.__len__.__format__

#Creating chromedriver script;
with Chrome() as driver:
    with open(f'config.json', 'r', encoding='utf-8') as f: 
        content = json.loads(f.read())
    f.close()

    #Setting parameters;
    email = 'bcbrunop@gmail.com'
    password = 'Novato11!!'
    link = 'https://www.facebook.com/bernardo.junior.79656/posts/2713009795609469'
    qtdMessage = '2500'

    #Acessing Facebook;
    driver.get("https://www.facebook.com/")
    time.sleep(2)

    #Logging in;
    emailInput = driver.find_element_by_xpath('//*[@id="email"]')
    emailInput.send_keys(email)

    pwdInput = driver.find_element_by_xpath('//*[@id="pass"]')
    pwdInput.send_keys(password)

    button = driver.find_element_by_xpath('//*//*[@id="u_0_b"]')
    button.click()
    time.sleep(4)

    #Acessing vitim's post;
    driver.get(link)
    time.sleep(4)

    #Acessing comment camp;
    commentInput = driver.find_element_by_xpath(
        '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div/div/div/div/form/div[2]/div/div[2]/div')

    #Posting messages on the post;
    for i in range(qtd_message):
        commentInput.send_keys(messageBreak(), Keys.ENTER)
        time.sleep(2)

    #Watching the world burn;
    time.sleep(100)

#THIS IS A AUTHENTICATED SCRIPT, DO NOT USE IT WITHOUT PERMISSION
#USE ONLY FOR FUN, NOT SPAM
#Have fun ;)