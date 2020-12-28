from selenium import webdriver
import time
path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get('https://web.whatsapp.com')

name = input("enter the name of person:")
msg = input("enter msg:")
count = int(input("enter count:"))



##//span[@title="name of person"]
##//*[@id="main"]/footer/div[1]/div[2]/div/div[2]
##//*[@id="main"]/footer/div[1]/div[3]/button

input(" Enter anything after scanning Qr code:")

user = driver.find_element_by_xpath("//span[@title = '{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
##    ##add script for delet for me option()
##    ## add script for delet deleted tab for final(//*[@id="main"]/div[3]/div/div/div[3]/div[12]/div/div/div)
##    #time.sleep(1000)
##    #driver.find_element_by_xpath("//*[@id='main']/div[3]/div/div/div[3]/div[35]/div/div/div/div[1]/div").click()
##    driver.find_element_by_xpath("//*[@id='main']/div[3]/div/div/div[3]/div[35]/div/div/span[2]/div/div").click()
##    driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[5]/div").click()
##    driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/span/div/div/div/div/div/div[3]/div/div[1]/div").click() 
##    print("msg deleted")
    print(i)
print("work done")
driver.close()
