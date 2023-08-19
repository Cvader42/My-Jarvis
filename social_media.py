import os
import json
import requests

def post_to_twitter(message):
    # Authenticate with Twitter
    twitter_auth = os.getenv("TWITTER_AUTH")
    headers = {"Authorization": f"Bearer {twitter_auth}"}

    # Post the message to Twitter
    response = requests.post("https://api.twitter.com/2/tweets", headers=headers, data={"text": message})
    return response.status_code

def post_to_facebook(message):
    # Authenticate with Facebook
    facebook_auth = os.getenv("FACEBOOK_AUTH")
    headers = {"Authorization": f"Bearer {facebook_auth}"}

    # Post the message to Facebook
    response = requests.post("https://graph.facebook.com/v12.0/me/feed", headers=headers, data={"message": message})
    return response.status_code

def send_message_on_messenger(sender_id, recipient_id, message):
    # Authenticate with Facebook Messenger
    facebook_messenger_auth = os.getenv("FACEBOOK_MESSENGER_AUTH")
    headers = {"Authorization": f"Bearer {facebook_messenger_auth}"}

    # Send the message to the recipient
    response = requests.post(
        f"https://graph.facebook.com/v12.0/me/messages?recipient={recipient_id}",
        headers=headers,
        data={"text": message},
    )
    return response.status_code

def search_for_people(query):
    # Authenticate with Facebook
    facebook_auth = os.getenv("FACEBOOK_AUTH")
    headers = {"Authorization": f"Bearer {facebook_auth}"}

    # Search for people matching the query
    response = requests.get(
        f"https://graph.facebook.com/v12.0/search?q={query}",
        headers=headers,
    )
    return json.loads(response.content)["data"]

def add_friend(friend_id):
    # Authenticate with Facebook
    facebook_auth = os.getenv("FACEBOOK_AUTH")
    headers = {"Authorization": f"Bearer {facebook_auth}"}

    # Add the friend
    response = requests.post(
        f"https://graph.facebook.com/v12.0/me/friends?uids={friend_id}",
        headers=headers,
    )
    return response.status_code

def post_to_instagram(message):
    # Authenticate with Instagram
    instagram_auth = os.getenv("INSTAGRAM_AUTH")
    headers = {"Authorization": f"Bearer {instagram_auth}"}

    # Post the message to Instagram
    response = requests.post(
        "https://graph.instagram.com/v1/media?caption={}".format(message),
        headers=headers,
    )
    return response.status_code

def post_to_linkedin(message):
    # Authenticate with LinkedIn
    linkedin_auth = os.getenv("LINKEDIN_AUTH")
    headers = {"Authorization": f"Bearer {linkedin_auth}"}

    # Post the message to LinkedIn
    response = requests.post(
        "https://api.linkedin.com/v2/posts?updateContent={}".format(message),
        headers=headers,
    )
    return response.status_code
