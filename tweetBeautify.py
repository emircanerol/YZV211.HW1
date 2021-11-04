import datetime
import time
import pandas as pd


df = pd.DataFrame(columns=["timestamp", "time", "tweet"])
with open ("elonMuskTweets.csv", 'r') as f:
    titles = f.readline().strip().split(' ')

    for line in f:
        infos = line[:56].split(' ')
        tweet = line[56:].strip()
        
        date = infos[1]
        hour = infos[2]

        three_hours = datetime.timedelta(hours = 3)
        time_obj = datetime.datetime.strptime(date + " " + hour, '%Y-%m-%d %H:%M:%S') - three_hours
        timestamp = time.mktime(time_obj.timetuple())
        df = df.append({'timestamp':timestamp, 'time':time_obj, 'tweet':tweet}, ignore_index=True)
df.head(5)