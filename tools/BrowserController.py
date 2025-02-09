import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import multiprocessing

def play_video(videoname):
    process = multiprocessing.Process(target=open_browser, args=(videoname,))
    process.start()
    return process
def open_browser(videoname):
    web = webdriver.Edge()
    web.get("http://192.168.88.1:5244/")
    web.maximize_window()
    WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/input[1]'))).send_keys('yifei')
    WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/input[2]'))).send_keys('147852369987syf')
    web.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[1]/div[3]/button[2]').click()
    time.sleep(2)
    # 等待某个元素出现
    WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div'))).click()
    WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="search-input"]'))).send_keys(videoname)
    web.find_element(by=By.XPATH, value='//*[@id="hope-modal-cl-48--body"]/div/div[1]/button[2]').send_keys(Keys.ENTER)
    WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="hope-modal-cl-48--body"]/div/div[2]/a'))).click()
    WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div[1]/a'))).click()
    return '主人观影愉快喵！'

def open_airconditioner():
    respone = requests.post('http://192.168.88.1:8123/api/webhook/-XS4S8e3ZsUc7y_DyFs_VJSyR')
    return '空调打开了喵！'


if __name__ == '__main__':
    open_browser()