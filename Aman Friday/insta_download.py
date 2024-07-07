from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import os
import urllib.request
from getpass import getpass

user=input('Enter user id: ')
pw=getpass('Enter password: ')
dwuser=input('Enter the userid of person whose pics you want to download: ')

class InstaDownload:
    def __init__(self):
        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("http://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(user)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw,Keys.RETURN)
        print('logged in')
        sleep(5)
        #self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        print('clicked not now')
    def download_user_img(self):
        sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(dwuser,Keys.RETURN)
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div[1]").click()
        print(f'searched for {dwuser}')
        
        img_srcs = []
        finished = False
        while not finished:

            finished = self.infinite_scroll() # scroll down

            img_srcs.extend([img.get_attribute('src') for img in self.driver.find_elements_by_class_name('FFVAD')]) # scrape srcs 

        img_srcs = list(set(img_srcs)) # clean up duplicates
        print('downloading image')
        for idx, src in enumerate(img_srcs):
            self.download_image(src, idx, dwuser)
        self.driver.quit()  
        os.startfile(f"{dwuser}\\{dwuser}_0.jpg")       
        
    def download_image(self, src, image_filename, folder):
        folder_path = './{}'.format(folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        img_filename = f'{dwuser}_{image_filename}.jpg'
        urllib.request.urlretrieve(src, '{}/{}'.format(folder, img_filename))


    def infinite_scroll(self):
   
    
        self.last_height = self.driver.execute_script("return document.body.scrollHeight")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)

        self.new_height = self.driver.execute_script("return document.body.scrollHeight")


        if self.new_height == self.last_height:
            return True

        self.last_height = self.new_height
        return False



bot=InstaDownload()
bot.download_user_img()