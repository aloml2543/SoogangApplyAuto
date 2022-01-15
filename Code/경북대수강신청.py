# pip install selenium bs4 pytesseract cv2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
import subprocess


try:
    subprocess.Popen('C:/Program Files/Google/Chrome/Application/chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
except:
    subprocess.Popen('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')

def sugang(): 
    URL= "https://sugang.knu.ac.kr/Sugang/comm/support/login/loginForm.action?redirUrl=%2FSugang%2Fcour%2FlectReq%2FonlineLectReq%2Flist.action"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(executable_path='C:/Users/aoml3/OneDrive/바탕 화면/test/수강신청/chromedriver', options=options)
    driver.get(url=URL)
    da = Alert(driver)
    driver.implicitly_wait(10)

    while True:
        try:
            print(1)
            driver.find_element_by_xpath('//*[@id="user.stu_nbr"]').clear()
            driver.find_element_by_xpath('//*[@id="user.stu_nbr"]').send_keys('2019114538')
            driver.find_element_by_xpath('//*[@id="user.usr_id"]').clear()
            driver.find_element_by_xpath('//*[@id="user.usr_id"]').send_keys('aoml3245')
            driver.find_element_by_xpath('//*[@id="user.passwd"]').clear()
            driver.find_element_by_xpath('//*[@id="user.passwd"]').send_keys('egoism3658!')
            
            driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[4]/td/button[1]').click()

        except TimeoutException:
            break
        except KeyboardInterrupt:
            return
        except UnexpectedAlertPresentException:
            try:
                da.accept()
            except NoAlertPresentException:
                continue
        except ElementNotInteractableException:
            da.accept()
        except AttributeError:
            da.accept()
        except NoSuchElementException:
            break
    

    
    while True:
        print(1)
        try:            
            btn=driver.find_elements_by_xpath("//*[contains(text(), '신청')]")
            for i in btn:
                try:
                    i.click()
                    #i.send_keys(Keys.ENTER)
                except UnexpectedAlertPresentException:
                    try:
                        da.accept()
                    except NoAlertPresentException:
                        continue
                except ElementNotInteractableException:
                    try:
                        da.accept()
                    except:
                        continue
                except AttributeError:
                    try:
                        da.accept()
                    except:
                        continue
        except KeyboardInterrupt:
            return
        except NoSuchElementException:
            continue
        except UnexpectedAlertPresentException:
            try:
                da.accept()
            except NoAlertPresentException:
                continue
        except ElementNotInteractableException:
            try:
                da.accept()
            except:
                continue
        except AttributeError:
            try:
                da.accept()
            except:
                continue

sugang()