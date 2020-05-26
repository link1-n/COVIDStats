from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

link = 'https://www.worldometers.info/coronavirus/country/india/'
url = requests.get(link)

soup = BeautifulSoup(url.content, 'lxml')
numbers = soup.findAll(class_='maincounter-number')

total = numbers[0].span.getText()
total_int = int(total.replace(',',''))

death = numbers[1].span.getText()
death_int = int(death.replace(',',''))

recover = numbers[2].span.getText()
recover_int = int(recover.replace(',',''))
j = 7
newCase = soup.findAll(class_ = 'news_li', limit = j)

newCaseT = []
x = []

for i in reversed(range(j)):
    lol = int(newCase[i].strong.getText().replace(' new cases','').replace(',',''))
    newCaseT.append(lol)

for i in range(1, j+1):
    x.append(i)

x.pop(6)
dailyCase = newCaseT[:] 
#[:] was added because python creates a reference to the variable when simply equated
dailyCase.pop(6)

plt.plot(x, dailyCase, marker = 'o', markerfacecolor = 'pink')
plt.xlabel("Day")
plt.ylabel("Number of New Cases")
plt.title("Number of New COVID-19 Cases in the Past 6 Days")
plt.grid()
plt.show()

active = total_int - (death_int + recover_int)

print(f"In India:\n\tTotal Cases: {total}\n\tRecovered: {recover}\n\tDeaths: {death}\n\tActive Cases: {active}")
print(f"\tNumber of New Cases Today: {newCaseT[6]}\n\tNumber of New Cases Yesterday: {newCaseT[5]}")