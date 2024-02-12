import time

from twitter import Twitter

consumer_key = ''
consumer_secret = ''

token_key = ''
token_secret = ''

twitter = Twitter( consumer_key,consumer_secret,token_key,token_secret)


#resp = twitter.tweet('vamos testar nossa lib')
pesquisa = twitter.search('solyd', 'pt')
for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])

