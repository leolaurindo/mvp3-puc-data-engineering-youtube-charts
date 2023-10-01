"""
This script executes a scrap using selenium library to navigate
through different urls of the YouTube chart web page and to download
the .csv files that will empower our analysis. The page has javascript
object filtered by week and number of views. The difference in urls are
the dates, which are composed of the opening date of the week and its
closing date in YYYY-MM-DD format. The script identifies the download
button and downloads a .csv file. After the download, the file is read
with the pandas library, a numerica column is added to reference the
week, another one is added with the opening date of the week and for
the last column added the script adds the week's closing date. In the
end, the script prints its execution time, the number of files downloaded
and the average execution time per downloaded file.
"""

import os
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import json
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from datetime import datetime

execution_start = time.time()

load_dotenv()

# Get the script's absolute directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the base directory for saving the downloaded files
base_dir = os.path.join(script_dir, os.environ["DOWNLOAD_CHARTS_PATH"])

# Selecting dates of interest
with open('reference_dates.json', 'r') as file:
    dates_json = json.load(file)

# Pair the URLs with their respective start and end dates
url_date_pairs = []
for element in dates_json["chartPeriods"]:
    start = element["startTime"].replace("-", "")
    end = element["endTime"].replace("-", "")
    formatted_url = f'https://charts.youtube.com/charts/TopSongs/br/{start}-{end}?hl=pt'
    url_date_pairs.append((formatted_url, start, end))

driver_path = os.path.join(script_dir, os.environ["CHROME_DRIVER_PATH"])
service = Service(executable_path=driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('prefs', {'download.default_directory' : base_dir})
options.add_argument('--headless')

i = 0 

for url, start, end in url_date_pairs:
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    check_box_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='download-container style-scope ytmc-charts']/paper-icon-button"))
    )
    check_box_element.click()

    time.sleep(6)
    
    date_string = url.split("/")[-1].split("?")[0][-8:]
    formatted_date = date_string[:4] + '-' + date_string[4:6] + '-' + date_string[6:]

    charts_path = os.path.join(base_dir, f'youtube-charts-top-songs-br-weekly-{formatted_date}.csv')
    df = pd.read_csv(charts_path)
    
    df["week_open"] = datetime.strptime(start, "%Y%m%d").date()
    df["week_close"] = datetime.strptime(end,"%Y%m%d").date()
    df.to_csv(charts_path)
    i+=1
    driver.quit()

execution_end = time.time()
elapsed_time = execution_end - execution_start
average_download_time = elapsed_time / len(url_date_pairs)
print(f"Tempo de execução do script: {elapsed_time} segundos")
print(f"Foram baixados {len(url_date_pairs)} arquivos")
print(f"Tempo médio de execução por arquivo: {average_download_time}")
