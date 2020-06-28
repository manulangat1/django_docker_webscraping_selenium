from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

url = "https://dev.to/"
from decouple import config 
username = config('username')
pw =config('password')
def scraps(url):
    print(url)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    sleep(2)
    login = driver.find_element_by_xpath("//section[1]/div/a[1]").click()
    sleep(17)
    input1 = driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(username)
    sleep(3)
    input2 = driver.find_element_by_xpath('//*[@id="password"]').send_keys(pw)
    sleep(3)
    sign = driver.find_element_by_name("commit").click()
    sleep(15)
    sleep(20)
    lis_of_articles = (i for i in driver.find_elements_by_xpath('//*[@id="featured-story-marker"]/div/div[1]') )
    for i in lis_of_articles:
        print(i)
        print()
    driver.quit()

scraps(url)