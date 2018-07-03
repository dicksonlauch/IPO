import pandas as pnd
import urllib.request as urlreq
from bs4 import BeautifulSoup

# IPO codes that are issued last two years are stored in code.csv
df = pnd.read_csv('code.csv', dtype = 'str', header = None)
stock_codes = df[0].values.tolist()
print(stock_codes)

# Features
offer_range = {}
global_offering = {}
for i in range(3): # range(len(stock_codes))
    # let Python open the website -- take some time
    page = urlreq.urlopen("http://www.aastocks.com/tc/ipo/IPOInfor.aspx?symbol=" + stock_codes[i])
    # Get the HTML of the website
    soup = BeautifulSoup(page, 'html.parser')
    print(soup.find_all('td', attrs={'class' : 'subtitle2'}))
    # By checking the websitre, the offer range corresponds to the 2nd entry in the list
    tag2 = soup.find_all('td', attrs={'class' : 'subtitle2'})[2]
    offer_range[stock_codes[i]] = tag2.get_text().strip()
    # Same for the total number of shares issued globally
    tag1 = soup.find_all('td', attrs={'class': 'subtitle2'})[1]
    global_offering[stock_codes[i]] = tag1.get_text().strip()

output = pnd.DataFrame({'Offer Range' : offer_range, 'Global Offering' : global_offering})
print(output)

output.to_csv('field.csv')