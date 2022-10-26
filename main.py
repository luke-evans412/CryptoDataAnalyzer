

#library imports
import pandas as pd
import requests
import bs4 as bs

#variable declarations to obtain trending crypto information from webpage into separate arrays
page = requests.get('https://coinmarketcap.com/best-cryptos/')
soup = bs.BeautifulSoup(page.text, "html.parser")
tables = soup.find(class_="sc-1kzt9sl-1 eLgweq")
trendingCryptos = tables.find_all("tr")
trendingCryptoPrices = []
trendingCryptoNames = []

#gets the price of the trending cryptocurrency
for container in trendingCryptos:
    try:
        price = container.find('span').text.strip()
    except:
        price = ''
    finally:
        trendingCryptoPrices.append(price)
#gets the name of the trending cryptocurrency
for container in trendingCryptos:
    try:
        name = container.find(class_="sc-14rfo7b-0 lhJnKD").text.strip()
    except:
        name = ''
    finally:
        trendingCryptoNames.append(name)

#gets rid of empty elements and prints names
trendingCryptoPrices.pop(0)
trendingCryptoNames.pop(0)
print("Trending Cryptocurrency Names: ")
print(trendingCryptoNames)

#variable declarations to obtain positive growth crypto information
# from webpage into separate arrays
page1 = requests.get('https://coinmarketcap.com/gainers-losers/')
soup1 = bs.BeautifulSoup(page1.text, "html.parser")
positiveTable = soup1.find(class_="sc-1yw69nc-0 DaVcG table-wrap")
positiveCryptos = positiveTable.find_all("tr")
positivePrices = []
positiveNames = []
percentIncreases = []
positiveVolume = []

#gets the price of the growing cryptocurrency
for container in positiveCryptos:
    try:
        price = container.find('span').text.strip()
    except:
        price = ''
    finally:
        positivePrices.append(price)

#gets the name of the positive cryptocurrency
for container in positiveCryptos:
    try:
        name = container.find(class_="sc-14rfo7b-0 lhJnKD").text.strip()
    except:
        name = ''
    finally:
        positiveNames.append(name)

#gets the percent increase of the positive growth cryptocurrency
for container in positiveCryptos:
    try:
        percentIncrease = container.find(class_="sc-15yy2pl-0 kAXKAX").text.strip()
    except:
        percentIncrease = ''
    finally:
        percentIncreases.append(percentIncrease)

#gets the volume of the growing cryptocurrency
for container in positiveCryptos:
    try:
        ch = "%"
        positiveCryptoVolume = container.findNext("tr").text.strip()
        cryptoString = positiveCryptoVolume.split(ch, 1)
        if len(cryptoString) > 0:
            positiveCryptoVolume = cryptoString[1]
    except:
        positiveCryptoVolume = ""
    finally:
        positiveVolume.append(positiveCryptoVolume)

#gets rid of empty elements and prints names
positiveNames.pop(0)
positivePrices.pop(0)
percentIncreases.pop(0)
print("Growing Cryptocurrency Names: ")
print(positiveNames)

#variable declarations to obtain negative growth crypto information
# from webpage into separate arrays
negativePrices = []
negativeNames = []
percentDecreases = []
negativeVolumes = []

table = soup1.find(class_="sc-1yw69nc-0 DaVcG table-wrap")
negativeTable = table.find_all_next(class_="uikit-col-md-8 uikit-col-sm-16")[-1]
negativeCryptos = negativeTable.findAll("tr")

#gets the price of the negative cryptocurrency
for container in negativeCryptos:
    try:
        price = container.find('span').text.strip()
    except:
        price = ''
    finally:
        negativePrices.append(price)

#gets the name of the negative cryptocurrency
for container in negativeCryptos:
    try:
        name = container.findNext(class_="sc-14rfo7b-0 lhJnKD").text.strip()
    except:
        name = ''
    finally:
        negativeNames.append(name)

#gets the percent decrease of the negative cryptocurrency
for container in negativeCryptos:
    try:
        percentDecrease = container.findNext(class_="sc-15yy2pl-0 hzgCfk").text.strip()
    except:
        percentDecrease = ''
    finally:
        percentDecreases.append(percentDecrease)

#gets the volume of the declining cryptocurrency
for container in negativeCryptos:
    try:
        ch = "%"
        negativeCryptoVolume = container.findNext("tr").text.strip()
        cryptoString = negativeCryptoVolume.split(ch, 1)
        if len(cryptoString) > 0:
            negativeCryptoVolume = cryptoString[1]
    except:
        negativeCryptoVolume = ""
    finally:
        negativeVolumes.append(negativeCryptoVolume)

#gets rid of empty elements and prints names
negativePrices.pop(0)
negativeNames.pop(0)
percentDecreases.pop(0)
print("Declining Cryptocurrency Names: ")
print(negativeNames)


#array declarations to prepare data for output to Excel
empty1 = []
empty2 = []
output = [trendingCryptoNames, trendingCryptoPrices, empty1, positiveNames,
          positivePrices, percentIncreases, positiveVolume, empty2,
          negativeNames, negativePrices, percentDecreases, negativeVolumes, empty1]

#dataframe declarations to organize data
df = pd.DataFrame(output)
df1 = df.transpose()

#array declaration for column names. Dataframe columns are assigned names afterwards
newColumns = ['Trending Name', 'Trending Price', '____', 'Name+', 'Price+', '%+', 'Volume', '____',
              'Name-', 'Price-', '%-', 'Volume', '----']
df1.columns = newColumns

#output dataframe to csv
df1.to_csv('cryptoData.csv', index=False, encoding='utf-8')

