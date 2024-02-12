#Publicando e pesquisando no Twitter
from requests_oauthlib import OAuth1Session

# Get consumer key and consumer secret from environment variables
consumer_key = ''
consumer_secret = ''


if not consumer_key or not consumer_secret:
    print("Consumer key or consumer secret not found. Please set them as environment variables.")
    exit(1)


payload = {"text": "Hello world!"}

request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except Exception as e:
    print("Error fetching request token:", e)
    exit(1)


resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
if not resource_owner_key or not resource_owner_secret:
    print("Request token not obtained successfully.")
    exit(1)

print("Got OAuth token:", resource_owner_key)


base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize:", authorization_url)
verifier = input("Paste the PIN here: ")


access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)

try:
    oauth_tokens = oauth.fetch_access_token(access_token_url)
except Exception as e:
    print("Error fetching access token:", e)
    exit(1)

access_token = oauth_tokens.get("oauth_token")
access_token_secret = oauth_tokens.get("oauth_token_secret")
if not access_token or not access_token_secret:
    print("Access token not obtained successfully.")
    exit(1)

print("Got access token:", access_token)


oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

response = oauth.post("https://api.twitter.com/2/tweets", json=payload)

if response.status_code == 201:
    print("Tweet posted successfully!")
else:
    print("Error posting tweet. Response:", response.text)

''' response:
Got OAuth token: 
Please go here and authorize: https://api.twitter.com/oauth/authorize?oauth_token=
Paste the PIN here: 
Got access token: 
Tweet posted successfully!'''
