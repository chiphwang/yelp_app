from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())






def get_business(term,language,city):
    auth = Oauth1Authenticator(
        consumer_key=os.environ['consumer_key'],
        consumer_secret=os.environ['consumer_secret'],
        token=os.environ['token'],
        token_secret=os.environ['token_secret'],
    )
    params = {
    'term': term,
    'lang': language,
    'limit': 3,
    }
    client = Client(auth)
    response=client.search(city, **params)
    return response


#city = "oakland, CA"
#response = get_business("food","en",city)


#for business in response.businesses:
#    print(business.name)
#    print(business.rating)

#stuff= []

#for business in response.businesses:
#    #print(business.name,business.rating,business.phone)
#    stuff.append({"name": business.name,
#    "rating": business.rating,
#    "phone": business.phone,
#    })

#print (stuff)
#    return businesses
#businesses = get_businesses('New York City', 'food')


#businesses = get_businesses('New York City', 'food')
