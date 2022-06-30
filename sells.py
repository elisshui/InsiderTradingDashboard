#getting data from insiderarbitrage
import pandas as pd
from datetime import datetime #used to time how long it takes to run the script

def getSells():
    startTime = datetime.now()
    numPages = 3  #number of pages to be scraped
    finalDf = pd.DataFrame()  #final dataframe
    transactionTypes = ['buying', 'sales'] 
    pagesScraped = 0 #num of pages scraped

    for tr in transactionTypes:
        for i in range(numPages): #for evey page
            url = f"https://www.insidearbitrage.com/insider-{tr}/?desk=yes&pagenum={i+1}"  #url of website for certain transaction, page
            df = pd.read_html(url) #reads the html of ^
            df = df[0]
            columns = df.iloc[0] #locating each column in data
            df.columns = columns #assign columns to the dataframe
            df = df[1:] #only want rows from 1st index and lower
            
            if tr == 'buying':
                df['Type'] = 'buy'
            else:
                df['Type'] = 'sell'

            frames = [finalDf, df]
            finalDf = pd.concat(frames)
            pagesScraped+=1  #increase num of pages scraped

            print(f'{pagesScraped} Pages Scraped - Total Elasped Time = {datetime.now() - startTime}')  #fstring to see if page was scraped

    finalDf.to_csv('insider.csv') #creating csv file                 
    print(f'CSV File created.\nExecution time: {datetime.now()-startTime}') #prints time taken to run script