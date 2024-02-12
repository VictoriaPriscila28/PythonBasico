#Publicando e pesquisando no Twitter
import oauth2
import json
import pprint


consumer = oauth2.Consumer(consumer_key,consumer_secret)
token = oauth2.Token(token_key,token_secret)
cliente = oauth2.Client(consumer,token)
requisicao = request.get('https://api.twitter.com/1.1/search/tweets.json?q=%40twitterdev', headers={"Authorization":"Bearer seu_token"}))
decodificar = requisicao[1].decode()
objeto = json.loads(decodificar)

#pprint.pprint(objeto['statuses'][0]['text'])
print(objeto)
