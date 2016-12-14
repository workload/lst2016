import pandas as pd
import datetime
import time



df=pd.DataFrame({'time':['15:37','15:38','15:39','15:40'],
                 'from':['SHH','SZH','WXH','ZJH'],
                 'to':['NJH','NJH','NJH','NJH']})

time_ls = list(df['time'])
from_ls = list(df['from'])
to_ls = list(df['to'])
date = '2016-12-14 '

def ex(a,b):
    print("Time is reached. train from {} to {}".format(a, b))

def main():
    i=0
    try:
        while time.strftime("%H:%M", time.localtime()) == df['time'][i]:   
	ex(from_ls[i],to_ls[i])
	time_ls.remove(df['time'][i])
	i+=1

	timeArray = time.strptime(date+df['time'][i+1]+":00", "%Y-%m-%d %H:%M:%S")
	timeStamp = int(time.mktime(timeArray))
	ime.sleep(timeStamp-time.time())

    except:
	print 'all finished!'

