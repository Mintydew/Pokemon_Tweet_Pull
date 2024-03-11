import tweepy
import requests

# Hide access tokens/keys when uploading project to GitHub


pokemon_api_url = "https://pokeapi.co/api/v2/pokemon/?limit=100000"

poke_list = []
tweet_dict = {}

response = requests.get(pokemon_api_url)

# If api response is successful, extract the data in it's json format
if response.status_code == 200:
    data_json_format = response.json()

# For each pokemon, append the name of the pokemon to the poke_list for use at the scraping section.
    for pokemon in data_json_format['results']:
        poke_list.append(pokemon['name'])
else:
    print(f'Error with api response. Code = {response.status_code}')

# Pass in authentication key
client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, wait_on_rate_limit=True)

# Defining the search query and max result parameter for search_recent_tweets method

for pokemon in poke_list:
    query = f"{pokemon} -is:retweet"
    max_results = 20

    tweets = client.search_recent_tweets(query=query, max_results=max_results)

    for tweet in tweets:
        if pokemon not in tweet_dict:
            tweet_dict[pokemon] = 1
        else:
            tweet_dict[pokemon] += 1

print(max(tweet_dict, key=lambda k:tweet_dict[k]))
