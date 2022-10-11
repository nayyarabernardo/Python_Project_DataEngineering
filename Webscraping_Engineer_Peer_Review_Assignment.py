import glob
import pandas as pd
from datetime import datetime
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe

def extract(): # EXTRACT function
    df = extract_from_json('bank_market_cap_1.json')
    return df
# Question 1
df = pd.read_csv("exchange_rates.csv", index_col=0)
exchange_rate = df['Rates']['GBP'] # get the exchange rate from USD to GBP
def transform(): # TRANSFORM function
    dft = extract()

    dft['Market Cap (US$ Billion)'] = dft['Market Cap (US$ Billion)']*exchange_rate
    dft['Market Cap (US$ Billion)'] = dft['Market Cap (US$ Billion)'].round(3)
    dft.columns = ['Name','Market Cap (GBP$ Billion)']

    return dft
def load(dfl): # LOAD function
    dfl.to_csv("bank_market_cap_gbp.csv", index = False)
    return dfl
def log(message): # LOG function
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')
# Running the ETL Process

log("ETL Job Started")

log("Extract phase Started")
# Question 2
df = extract()
df.head()
log("Extract phase Ended")
log("Transform phase Started")
# Question 3
dft = transform()
dft.head()
log("Transform phase Ended")
log("Load phase Started")
dfl = load(dft)
log("Load phase Ended")