from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# browser = webdriver.Firefox(firefox_binary=FirefoxBinary(
#     firefox_path='/home/zach/Desktop/synopsis/firefox'))
# browser = webdriver.Firefox()
browser = webdriver.Chrome('/home/zach/Desktop/synopsys/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
