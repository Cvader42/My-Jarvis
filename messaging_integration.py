
import os
import json
import requests

def send_message(sender_id, recipient_id, message):
  """Sends a message to the specified recipient."""

  # Get the authentication token.
  token = get_authentication_token("FACEBOOK_MESSENGER")

  # Compose the request.
  url = f"https://graph.facebook.com/v12.0/me/messages?recipient={recipient_id}"
  headers = {"Authorization": f"Bearer {token}"}
  data = {"text": message}

  # Send the request.
  response = requests.post(url, headers=headers, data=data)

  # Check the response status code.
  if response.status_code != 200:
    raise ValueError(f"Failed to send message: {response.status_code}")

def get_messages(sender_id, recipient_id):
  """Gets all of the messages between the specified sender and recipient."""

  # Get the authentication token.
  token = get_authentication_token("FACEBOOK_MESSENGER")

  # Compose the request.
  url = f"https://graph.facebook.com/v12.0/me/messages?sender={sender_id}&recipient={recipient_id}"
  headers = {"Authorization": f"Bearer {token}"}

  # Send the request.
  response = requests.get(url, headers=headers)

  # Check the response status code.
  if response.status_code != 200:
    raise ValueError(f"Failed to get messages: {response.status_code}")

  # Parse the response data.
  messages = json.loads(response.content)["data"]

  # Return the messages.
  return messages

def mark_message_as_read(message_id):
  """Marks the specified message as read."""

  # Get the authentication token.
  token = get_authentication_token("FACEBOOK_MESSENGER")

  # Compose the request.
  url = f"https://graph.facebook.com/v12.0/messages/{message_id}/read"
  headers = {"Authorization": f"Bearer {token}"}

  # Send the request.
  response = requests.post(url, headers=headers)

  # Check the response status code.
  if response.status_code != 200:
    raise ValueError(f"Failed to mark message as read: {response.status_code}")

def delete_message(message_id):
  """Deletes the specified message."""

  # Get the authentication token.
  token = get_authentication_token("FACEBOOK_MESSENGER")

  # Compose the request.
  url = f"https://graph.facebook.com/v12.0/messages/{message_id}"
  headers = {"Authorization": f"Bearer {token}"}

  # Send the request.
  response = requests.delete(url, headers=headers)

  # Check the response status code.
  if response.status_code != 200:
    raise ValueError(f"Failed to delete message: {response.status_code}")

