import selenium
import pandas as pd
import yfinance as yf
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.parse
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

df = pd.read_csv('Rohitt-chauhan/General-Files/data.csv')
# df['Company Name '] = df['Company Name '].str.replace(r'\.$','', regex=True).replace(r' ','-', regex=True).str.lower()
compnay_list = df['Company Name '].to_list()
compnay_list

symbol_class = '/html/body/main/div[1]/div/div/div[1]/div/div/div/label'

Size = '/html/body/main/div[1]/div/div/div[1]/div/div/div/a[1]'

industry_class = '/html/body/main/div[1]/div/div/div[1]/div/div/div/a[2]'


Company_data = pd.DataFrame()
Company_data = pd.DataFrame(columns=["company_name", "symbol", "Company_Size", "Industry"])

path = '/Users/rohit/Downloads/New folder/chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


driver = webdriver.Chrome(ChromeDriverManager().install())

i = 0
a = i//20
url = 'https://www.etmoney.com/stocks/list-of-stocks'


for Company_name in compnay_list:

        for a in range(a+2):
                button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[4]/button')
                button.click()
                time.sleep(6)
                driver.get(url)
                time.sleep(5)
                se = driver.find_element(By.CSS_SELECTOR, 'a[title="{}"]'.format(Company_name))
                se.click()
                time.sleep(5)
                find = driver.find_element(By.XPATH, symbol_class)
                symbol = find.text
                        
                find_size = driver.find_element(By.XPATH, Size)
                Company_Size = find_size.text
                        
                find_industry = driver.find_element(By.XPATH, industry_class)
                Industry = find_industry.text
                time.sleep(5)

                print(Company_name)

                new_row = pd.DataFrame({
                                "company_name": [Company_name],
                                "symbol": [symbol],
                                "Company_Size": [Company_Size],
                                "Industry": [Industry]
                                })
                        
                Company_data = pd.concat([Company_data,new_row], ignore_index=True)
                print(Company_data)

                i= i+1

                driver.back()