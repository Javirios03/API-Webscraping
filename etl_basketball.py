import requests
from bs4 import BeautifulSoup

url = "https://www.sportytrader.es/cuotas/baloncesto/usa/nba-306/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

teams = soup.find(class_='leading-normal tracking-normal font-avenir dark:bg-base-nightblack')
# teams = teams.find(class_='container-global ')
print(teams)
# teams = teams.find(class_='container mx-auto bg-white my-4 dark:bg-base-nightblack')
