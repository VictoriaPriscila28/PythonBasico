import time

from twitter import Twitter

consumer_key = 'GCZiWeku15HTPMoRsmTWOcg5r'
consumer_secret = 'vqM1Wg1d85SbLGi91RBSDjsHVDuuHgwX3a2I0MwgDz5PfTMRUN'

token_key = '1756852866109562880-KLVSjWvEZKIbb0A14SScGu0UUE61ml'
token_secret = 'mV9P8PGypWIiSam468H3bkcORjndQcdlMm5xmTKe3S2d9'

twitter = Twitter( consumer_key,consumer_secret,token_key,token_secret)


#resp = twitter.tweet('vamos testar nossa lib')
pesquisa = twitter.search('solyd', 'pt')
for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])

