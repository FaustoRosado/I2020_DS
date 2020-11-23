import requests
import csv
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"
#print(soup.title.text)
#table = soup.find('table', attrs={"class" : "wikitable"})

response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")
#trs = soup.find('tbody').findAll('tr')[2:-1]
trs = soup.find('tbody').findAll('tr')[2:237]

#     hd_list = []
    
    
#     country = []
#     cases = []
#     deaths = []
#     recoveries = []
#     death_rate = []
#     recovery_rate = []
    
#     for tr in trs:
        #country.append(tr.find_all("th")[1].find('a').text)
#         t_header = tr.findAll('th')
#         t_data = tr.findAll('td')
#         hd_row = []
#         hd_row.append(tr.find_all("th", attrs = {'scope' : 'row'})[1].find('a').text)
#         for td in t_data:
#             td_text = td.text
#             if td.get_text().replace("\n", "") == 'No data':
#                 td_text = None
        #else:
#         hd_row.append(int(t_data[0].text.replace("\n", "").strip()))
#         hd_row.append(int(t_data[1].text.replace("\n", "").strip()))
#         hd_row.append(int(t_data[2].text.replace("\n", "").strip()))
#         hd_list.append(hd_row)
#     return hd_list
        
        
#         country.append(tr.find_all("th", attrs = {'scope' : 'row'})[1].find('a').text)
         
#         tds = tr.find_all('td')
#         if t_td .get_text().replace("\n", "") == "No data":
#         cases.append(tds[0].text.replace("\n", "").strip())
#         deaths.append(tds[1].text.replace("\n", "").strip())
#         recoveries.append(tds[2].text.replace("\n", "").strip())
        
        
        
        
        
        
        #d_rate = int(tds[0]) / float(int(tds[1])) *100
        #print(d_rate)
        #death_rate.append(d_rate)

#         t_header = row.findAll('th')[1:]
#         t_data = row.findAll('td')[:-1]
#         thd_row = []
#         thd_row.append(t_header.text.replace('[', "").strip()
#         for td in t_data:
#             text_td = td.text.strip()
#             text_td = "".join(text_td.split(',')
#             if text_td == "No data":
#                 text_td = None
#             elif '.' in text_td:
#    return cases

def format_cell(data):
    try:
        return int(data.text.strip().replace(',',''))
    except: 
        return None

def rates(rate, case):
    try :
        return float(format(rate/case, '.3f'))
    except TypeError:
        return None
    
hd_list = []

for tr in trs:
    country = tr.find_all("th", attrs = {'scope' : 'row'})[1].find('a').text
    cases = format_cell(tr.find_all('td')[0])
    deaths = format_cell(tr.find_all('td')[1])
    recoveries = format_cell(tr.find_all('td')[2])
    
    death_rate = rates(deaths, cases)
    recovery_rate = rates(recoveries, cases)
    
    dlist = [country, cases, deaths, recoveries, death_rate, recovery_rate]
    
    hd_list.append(dlist)

#for info in hd_list:
    #print(info)
    

def make_csv():
    with open('fausto-rosado_covid-report.csv', 'w') as filename:
    
        file = csv.writer(filename)
        file.writerow(['country', 'cases', 'deaths', 'recoveries', 'death rate', 'recovery rate'])
        for info in hd_list:
            file.writerow(info)
            
if __name__ == '__main__':
    make_csv()



