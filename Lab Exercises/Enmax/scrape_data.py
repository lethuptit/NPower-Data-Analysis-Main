# pip3 install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

target_url = "https://www.enmax.com/generation-and-wires/real-time-system-demand"
api="https://www.enmax.com/api/v1/system-demand"
def scrape_with_api():
    # request the target website
    response = requests.get(api)
    # print(response.text)
    # verify the response status
    if response.status_code != 200:
        return f"status failed with {response.status_code}"
    else:
        API_Data = response.json() 
        print("system load: ", API_Data['current_system_load']['value']) 
        print("At time: " , API_Data['current_system_load']['time_stamp'])
        
 
def scrape_with_driver():
    # instantiate options for Chrome
    options = webdriver.ChromeOptions()
    # options = webdriver.EdgeOptions()

    # run the browser in headless mode
    options.add_argument("--headless=new")

    # instantiate Chrome WebDriver with options
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Edge()

    # open the specified URL in the browser
    driver.get(target_url)
    time.sleep(5)

    html = driver.page_source
    # parse the HTML content
    # print(driver.find_elements(By.CLASS_NAME, "heading-2"))
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    str_system_load = soup.find('h4', class_="heading-2 text-black text-center lg:text-left").text
    str_system_load_time = soup.find('p', class_="label-large text-black text-center lg:text-left").text
    print("system load: " , str_system_load)
    print("At time: " , str_system_load_time)

    # close the browser
    driver.quit()


scrape_with_api()