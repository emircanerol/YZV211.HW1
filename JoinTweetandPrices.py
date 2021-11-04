import datetime
import time
import pandas as pd

tw = pd.read_csv("tweetFinal.csv")
btc = pd.read_csv("BTCUSD_min2.csv",index_col=False)

def controlMissedValue(btc:pd.DataFrame):
    i = int(btc['unix'][0] / 60)
    for x in btc['unix']:
        x = int(x/60)
        if i != x:
            print(x*60)
            break
        i -= 1
controlMissedValue(btc)



def JoinTweetandPrices(tw,btc):
    cols = ['unix', 'date', 'tweet', 'day start', 'tweet time price', 'ten minute', 'hour', 'day end']
    df = pd.DataFrame(columns=cols) # create a dataframe to save data
    for line in tw.iloc: # every line in tweets DataFrame .iloc is
        
        temp = line['unix'] # to save time value because t will change
        t=line['unix'] # better for calculations
        t = t-t%60 # round to minute
        date = line[1] # better to represent as date
        tweet = line['tweet']

        int_location = int((btc['unix'][0] - t) / 60) # calculate where the value is        
        ds = t - t%86400 # day start
        
        #prices
        nw = btc['unix'][int_location] # get open price for tweet time
        nw_open = btc['open'][int_location]
        ten_minute = btc['open'][int_location - 10] # int_loc + 10 minutes
        hour = btc['open'][int_location - 60]
        day_loc = int((btc['unix'][0]-ds)/60)
        day_start = btc['open'][day_loc]
        day_end = btc['open'][day_loc - 1440] # day_loc - 1440: go to 1 day later
        
        # create a temporary dataframe and append to df
        final_line = pd.DataFrame({'unix':[temp], 
                                   'date':[date], 
                                   'tweet':[tweet], 
                                   'day start':[day_start], 
                                   'tweet time price':[nw_open],
                                   'ten minute':[ten_minute], 
                                   'hour':[hour], 
                                   'day end':[day_end]})

        df = df.append(final_line, ignore_index=True)
    return df

df = JoinTweetandPrices(tw, btc)
df.to_csv('/Users/emircanerol/Desktop/final.csv')