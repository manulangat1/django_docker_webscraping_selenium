from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from selenium.webdriver.chrome.options import Options  


from decouple import config 
username = config('username')
pw =config('password')
def scraps():
    url = "https://dev.to/"
    print(url)
    chrome_options = Options()  
    chrome_options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    driver.get(url)
    sleep(2)
    login = driver.find_element_by_xpath("//section[1]/div/a[1]").click()
    sleep(17)
    print(login)
    input1 = driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(username)
    sleep(3)
    input2 = driver.find_element_by_xpath('//*[@id="password"]').send_keys(pw)
    sleep(3)
    sign = driver.find_element_by_name("commit").click()
    sleep(15)
    # crayons-story__body
    lis_of_articles = [i for i in driver.find_elements_by_xpath('//*[@id="false"]/div/div') ]
    for i in lis_of_articles:
        print(i)
        print()
    print(len(lis_of_articles))
    sleep(3)
    driver.quit()

scraps()