import time
from selenium import webdriver


def run():
    # Here Chrome  will be used
    driver = webdriver.Chrome(r'/path/to/chromedriver')

    # URL of website
    url = "https://popcat.click/?fbclid=IwAR1JliB6HE1ABRqBgFnpJNO9m-HYotCcY9nfN1RpFPVl8VksKEho2ayZD0Q"

    # Opening the website
    driver.get(url)

    # getting the button by xpath
    button = driver.find_element_by_xpath('//*[@id="app"]/div')
    time.sleep(2) # time for loading

    # clicking on the button
    while True:
        button.click()
        time.sleep(0.005)


if __name__ == '__main__':
    run()
