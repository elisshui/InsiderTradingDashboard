<h1>Insider Trading Dashboard (Python & Tableau)</h1>
<h2>What is Insider Trading?</h2>
Insider trading data is obtained via information disclosed in the U.S. SEC's Form 4. Directors, officers, or owners of more than 10% of any class of a company's securities are defined as "insiders". Thus, are required to fill out the form two-busniess days following a transaction involving their respective company. This data is made public through various insider trading websites and provides investors with useful information pertaining to the performance or prospects of the company.<br>
<h2>Project Description</h2>
This project involved scraping insider trading data from <a href="insidearbitrage.com/insider-sales/?desk=yes">Insider Arbitrage</a>. At first, Selenium was used for web scraping. However, Python's Pandas library was found to be more efficient in completing the scrape. TThus, te data was then cleaned and processed using the <i>pandas</i> and <i>pandas_datareader</i> libraries. Finally, a fully automated dashboard was created using Tableau.
<h2>Web Scraping with Pandas</h2>
To obtain the data from <a href="insidearbitrage.com/insider-sales/?desk=yes">Insider Arbitrage</a>, I wrote a function: <i>getSells()</i> to complete this. The code block below shows how the data needed was located.<br>

```python
url = f"https://www.insidearbitrage.com/insider-{tr}/?desk=yes&pagenum={i+1}"  #url of website for certain transaction, page
df = pd.read_html(url) #reads the html of ^
df = df[0]
columns = df.iloc[0] #locating each column in data
df.columns = columns #assign columns to the dataframe
df = df[1:] #only want rows from 1st index and lower
```

The data in the section located as per the above code was then put into a dataframe and then, a csv file. This was all done using the pandas library.
<h2>Calculating Moving Average</h2>
A dictionary called <i>infoDict</i> was created to store the stock's ticker, current price, and moving average. As seen below, the <i>getInfo()</i> function was utilized to calculate the current price and moving average.

```python
def getInfo(ticker, nPeriods): #get current stock price -> will calculate MA
    try:
        tickerDf = dr.data.get_data_yahoo(ticker,start = date.today() - timedelta(300) , end = date.today())  #creating a dataframe containing the tickers, past 300 days
        currentPrice = tickerDf.iloc[-1]['Close'] #getting last row - current closing price
        MA = pd.Series(tickerDf["Close"].rolling(nPeriods, min_periods=0).mean(), name = 'MA') #calculating moving average: rolling = rolling sum, calc mean and name value MA
        currentMA = MA[-1]  #last row = the curr MA
        return (currentPrice, currentMA)  #return tuple
    except:
        return ('N/A', 'N/A') #if error occurs, return N/A for price and MA
```

The functions <i>getPrice()</i> and <i>getMA()</i> were used to assign a ticker its respective values in the dictionary, <i>infoDict</i>.
<h2>Scraping Stock Sectors and Automating Python Script</h2>
The different stock sectors in the U.S. Stock Market as per <a href = "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/">tradingview.com</a> were scraped and placed into another csv file using a Jupyter Notebook. A batch file as well as the Windows Task Scheduler were used to automate the data scraping process.
<h2>Creating the Dashboard</h2>
Tableau was used to join the stock sector csv file with the scraped data csv file. KPIs, a stock heat map, and a sector tree map were created. These were all put together to create a dashboard seen below.<br><br>
<img src="https://github.com/elisshui/InsiderTradingDashboard/blob/main/tradingDashboard.JPG" alt="Trading Dashboard" width=90%>

---
Project by [Eliss Hui](http://elisshui.epizy.com/ "Eliss Hui") (Jun 2022)
