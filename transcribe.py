import os
from dotenv import load_dotenv
import requests

def get_url(token, data):
  '''
  Parameter: 
  token: The API key
  data: The File Object to upload
  Return Value: 
  url: URL uplaoded to file
  '''
  headers = { 'authorization': token}
  response = requests.post('https://api.assemblyai.com/v2/upload', headers = headers, data = data)
  print("line 15: ", response.json())
  url = response.json()["upload_url"]
  print("Uploaded file and got temporary URL to file")
  return url

def get_transcribe_id(token, url):
  '''
  Parameter:
  token: the API key
  url: URL to uplaoded file
  Return value: 
  id: The transcribe id of the file
  '''
  endpoint = "https://api.assemblyai.com/v2/transcript"
  json = {
    "audio_url": url
  }
  headers = {
    "authorization": token, 
    "content-type": "application/json"
  }
  response = requests.post(endpoint, json = json, headers = headers)
  print("line 37: ", response)
  id = response.json()['id']
  print("Made request and file is currently queued")
  return id

def get_text(token, transcribe_id):
  '''
  Parameter: 
  token: The API key
  transcribe_id: The ID of the file which is being trasncribed
  Return value:
  result: The response object
  '''
  endpoint = f"https://api.assemblyai.com/v2/transcript/{transcribe_id}"
  headers = {
    "authorization": token
  }
  result = requests.get(endpoint, headers = headers).json()
  print("line 55: ", result)
  return result

def upload_file(fileObj):
  '''
  Paremter: 
  fileObj: The file object to transcribe
  Return value: 
  token: The API key
  transcribe_id: The ID of the file which is being transcribed
  '''
  load_dotenv()
  token = os.getenv("API_TOKEN")
  file_url = get_url(token, fileObj)
  print("line 68: ", file_url)
  transcribe_id = get_transcribe_id(token, file_url)
  return token, transcribe_id