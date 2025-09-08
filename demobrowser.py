import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome driver service is invoking chrome browser, the webdriver will not automatically invoke chrome by itself
# driver service takes all the commands froom websdriver and invokes them in chrome - checks chrome browser version 16- -> 160 
# if the versions are different, this driver service goes to theinternet for you and downloads the required version and runs commands on your behalf
# when you're working to some companies, somedimes driver service does not have permissions to download the required version by itself.
# the oldest libraries sometimes also cannot be found in the download packages path, you can manually
# download the chrome driver - make sure you have both latest versions long story short, or you might need manual set up.
# yu can give the service path to show from where you downloade=d the webdriver
# 1: take your google chrome version from help center in chrome
# 2:look for chrome webdriver download website.
# https://googlechromelabs.github.io/chrome-for-testing/
# 3:find the version that is corresponding to your chrome version - make sure you're copying the link to chrome driver, not to chrome:
# https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.80/win64/chromedriver-win64.zip
# 4: paste it in chrome and download, then take the path and put it in service path
# 5: copy file path, C:\Users\user\Downloads, unzip it and take .exe file for driver

#service_obj=Service(r"C:\Users\user\Documents\selenium learning\chromedriver-win64\chromedriver")
 #this way selenium will skip automatic download step, if you ust write webdriver.chrome(), this way selenium will automatically download the version of chrome driver for us.
#driver = webdriver.Chrome(service=service_obj)

#driver.get("https://rahulshettyacademy.com")


driver = webdriver.Chrome()
#to run it for different browsers - for all of them you need to set up different drivers, like Edge driver for Edge browser:
#also, dont import chrome, import edge or firefox - gecko driver for firefox, also set up service for these browsers
#edge (msedgdriver)/chrome/firefox driver download
#driver = webdriver.Firefox()   /    webdriver.Edge()
driver.get("https://rahulshettyacademy.com")
# #maximize the window output
driver.maximize_window()
# #if you want to know the title of the page
print(driver.title)
#url you're landing
print(driver.current_url)






time.sleep(2)