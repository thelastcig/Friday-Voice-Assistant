from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


search = input('Enter the name of reciever: ')
photo = input('Enter the path of video/photo: ')
count = int(input('Enter the number of times the mesage should be sent: '))



class WhatsppBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com/')
        sleep(15)
        self.driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]").send_keys(search,Keys.RETURN)
            
     
    def media(self):

        for n in range(count):
            self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span').click()
            photo_input = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input').send_keys(photo)
            sleep(2)
            photo_send = self.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div").click()


bot=WhatsppBot()       
bot.media()