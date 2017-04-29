
# coding: utf-8
#i have exported this python file from my ipython notebook.For #better visualisations you can use ipython notebook.You can even #use any python emulator to run this file and see the results.
# In[1]:

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import re
import pandas as pd
import numpy as np
import array
import time
import pylab as pl
import plotly.plotly as py
import plotly.graph_objs as go 

from datetime import datetime
import pandas_datareader.data as web


# In[2]:

get_ipython().magic('matplotlib inline')


# In[3]:

tweet_file1 = [r'C:\Users\Shrekar\Documents\PYTHON\data mining project\Trumpdate.json']
tweet1 = []
for file in tweet_file1:
    with open(file, 'r') as f:
        for line in f.readlines():
            tweet1.append(json.loads(line))
tweetdata1 = pd.DataFrame(tweet1)
tweetdata1


# In[ ]:




# In[4]:

tweetdata1['text']


# In[5]:

tweetdata = pd.DataFrame()
tweetdata['created_at'] = tweetdata1['created_at']
tweetdata['favorite_count'] = tweetdata1['favorite_count']
tweetdata['retweet_count'] = tweetdata1['retweet_count']
tweetdata['text'] = tweetdata1['text']
tweetdata['text'] = tweetdata['text'].map(lambda y: re.sub(r'RT', ' ', y)) 
tweetdata['text'] = tweetdata['text'].map(lambda x: re.sub(r'\W+', ' ', x))
tweetdata


# In[6]:

tweetdata.to_csv(r'c:\Users\Shrekar\Documents\PYTHON\data mining project\tweetdataclean.txt', header=None, index=None, sep=' ', mode='a')


# In[7]:

tweetdata.describe()


# In[8]:

tweets=tweetdata['text']
tweets


# In[9]:

blob = TextBlob(tweets[1])
blob.sentiment


# In[10]:

polar = pd.DataFrame()
n = int(len(tweets)) 
sen = []
for i in range(n):
    blob = TextBlob(tweets[i])
    k = blob.sentiment.polarity
    sen.append(k)
type(tweetdata['created_at'])


# In[11]:

polar


# In[12]:

n = int(len(tweetdata.index))
dateframe = pd.DataFrame()
dat = []
for i in range(n):
    d = datetime.strptime(tweetdata['created_at'][i],'%a %b %d %H:%M:%S %z %Y')
    k = d.strftime('%Y-%m-%d')
    dat.append(k)

dateframe['Date'] = dat


# In[31]:

polar['polarity'] = sen
tweetand_polarity = tweetdata.join(polar, how='outer')
tweetframedf = tweetand_polarity.join(dateframe,how='outer')


# In[30]:

tweetframedf[tweetframedf['polarity']<-0.1]


# In[14]:

tweetframedf[['text','polarity']]


# In[15]:

import plotly.plotly as py
py.sign_in('srikarkatta', 'MYgvU1P1FxjEE5CThyCV')
import plotly.graph_objs as go 


t = go.Scatter(x=tweetframedf.index,
                   y=tweetframedf.polarity)
data1 = [t]
lay = dict(
    title='Tweet polarity graph for 6000 tweets',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        type='Tweets'
    )
)

fig = dict(data=data1, layout=lay)
py.iplot(fig)


# In[16]:

t2 = go.Scatter(x = tweetframedf.index,y = tweetframedf.polarity,mode = 'markers')
data = [t2]
py.iplot(data, filename='Tweet polarity scatter')


# In[17]:

n = int(len(tweets)) 
meanvar = []
tweetmean = pd.DataFrame()
i = 1
while i<n:
    h = tweetframedf.iloc[i:i*50,[-2]].mean()
    i= i+50
    meanvar.append(h)
tweetmean['polarity'] = meanvar
#dfmean


# In[18]:

import plotly.plotly as py
import numpy as np

data = [dict(
        visible = False,
        line=dict(color='00CED1', width=6),
        name = '𝜈 = '+str(step),
        x = tweetmean.index,
        y = tweetmean.polarity) for step in np.arange(0,5,0.1)]
data[10]['visible'] = True

py.iplot(data, filename='Consolidated Tweet Polarity')






# In[19]:

favsort = tweetframedf.sort_values(by='favorite_count', ascending=False)
favsort1 = favsort.head(5)
favsort2 =favsort1.sort_values(by='polarity')
favsort2


# In[20]:

favsort3 = favsort2[['favorite_count','polarity']]
favsort3.set_index('polarity',inplace=True)
favsort3


# In[21]:

colors1 = 'rrbbb' 
favsort3.plot(kind='bar',color=colors1)
print('     Top Five Favorite_count tweets with their polarity')
plt.show()


# In[32]:

favsortr = tweetframedf.sort_values(by='retweet_count', ascending=False)
favsortr


# In[58]:

favsort4 = favsortr[['retweet_count','polarity']]
favsort4 = favsort4.sort_values(by='retweet_count',ascending=False)
favsort4.set_index('polarity',inplace=True)
favsort4r= favsort4.head(50)


# In[65]:

colors2 = 'r' 
favsort4r.plot(kind='bar',color=colors2,figsize=(10, 10))
print('     Top Five retweet_count tweets with their polarity')

plt.show()





# In[24]:

favsort5 = favsort2[['retweet_count','favorite_count','polarity']]
favsort5.set_index('polarity',inplace=True)
favsort5


# In[67]:

favsort5.plot(kind='bar')
print(' Plotting for top 5 favorite_count and their retweet_count  with polarity as index')


# In[26]:

polar.hist()




