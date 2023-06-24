#twitter bot

import requests #allows talk to http
import os #allows user to interact with your operating system
import json #javascript object notation -  defaul format for data. Need this library to interact with python world. Twitter returns Json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN") #environment variable. MY local comp is an environment.
#as long as my shell is open, bearer token is set. You set an enviroment variable that you can retrieve.
#bearer tokens identify you to the host of API. Used to authenticate and grant access. Twitter gives you the ID to enter here.

def create_url(): #visitng the below url
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=lang,author_id"
    # Be sure to replace your-user-id with your own user ID or one of an authenticating user
    # You can find a user ID by using the user lookup endpoint
    id = "your-user-id" #GET FROM TWITTER
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/users/{}/liked_tweets".format(id)
    return url, tweet_fields


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2LikedTweetsPython"
    return r


def connect_to_endpoint(url, tweet_fields): #I am the client, response is API output. Passes URL with parameter tweet_fields
    response = requests.request(
        "GET", url, auth=bearer_oauth, params=tweet_fields)
    print(response.status_code) #API simply returns a status code
    if response.status_code != 200: #anything not 200 is not a good status code (has errors?)
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json() #if 200, then i get json code back regarding the request from this block.


def main(): 
    url, tweet_fields = create_url() #create_url above returns two variables. They are going here.
    json_response = connect_to_endpoint(url, tweet_fields)
    print(json.dumps(json_response, indent=4, sort_keys=True)) #function dumps turns json into printable info


if __name__ == "__main__":
    main()

