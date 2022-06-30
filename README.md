<h1>Insider Trading Dashboard</h1>
<h2>What is insider trading?</h2>
Insider trading data is obtained via information disclosed in the U.S. SEC's Form 4. Directors, officers, or owners of more than 10% of any class of a company's securities are defined as "insiders". Thus, are required to fill out the form two-busniess days following a transaction involving their respective company. This data is made public through various insider trading websites and provides investors with useful information pertaining to the performance or prospects of the company.<br>
<h2>Project Description</h2>
This project involved scraping insider trading data from <a href="nsidearbitrage.com/insider-sales/?desk=yes">Insider Arbitrage</a>e. At first, Selenium was used for web scraping. However, Python's Pandas library was fond to be more efficient in completing the scrape. The data was then cleaned and processed using the pandas and pandas_datareader libraries. Finally, a fully automated dashboard was created using Tableau.
<h2>Web Scraping with Pandas</h2>
To obtain the data from <a href="nsidearbitrage.com/insider-sales/?desk=yes">Insider Arbitrage</a>, I wrote a function: getSells() to complete this. The code block below shows how the data needed was located.<br>
```
    url = f"https://www.insidearbitrage.com/insider-{tr}/?desk=yes&pagenum={i+1}"  #url of website for certain transaction, page
    df = pd.read_html(url) #reads the html of ^
    df = df[0]
    columns = df.iloc[0] #locating each column in data
    df.columns = columns #assign columns to the dataframe
    df = df[1:] #only want rows from 1st index and lower
```
The data in the section located as per the above code was then put into a dataframe and then, a csv file. This was all done using the pandas library.
<h2>Calculating Moving Average</h2>
