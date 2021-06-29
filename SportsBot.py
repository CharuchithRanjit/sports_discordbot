import discord
import os
import requests
import json
import requests

from keep_alive import keep_alive
# The 2 apis called for football scores and basketball scores 
url = "https://api.sofascore.com/api/v1/sport/football/events/live"
url2 = "https://api.sofascore.com/api/v1/sport/basketball/events/live"
payload = ""
headers = {
    "authority": "api.sofascore.com",
    "cache-control": "max-age=0",
    "sec-ch-ua": "^\^"
}
client = discord.Client()

def get_football_score():
  response = requests.request("GET", url, data=payload, headers=headers)

  jsondata = json.loads(response.text)
  league = jsondata['events'][0]['tournament']['name']
  time1 = jsondata['events'][0]['status']['description']
  hometeam = jsondata['events'][0]['homeTeam']['name']
  awayteam = jsondata['events'][0]['awayTeam']['name']

  homescore = jsondata['events'][0]['homeScore']['current']
  awayscore = jsondata['events'][0]['awayScore']['current']
  return (league + " " + hometeam + " " + str(homescore)+" - "+str(awayscore) + " " + awayteam + " " + time1)
def get_basketball_score():
  response = requests.request("GET", url2, data=payload, headers=headers)

  jsondata = json.loads(response.text)
  league = jsondata['events'][0]['tournament']['name']
  time1 = jsondata['events'][0]['status']['description']

  hometeam = jsondata['events'][0]['homeTeam']['name']
  awayteam = jsondata['events'][0]['awayTeam']['name']

  homescore = jsondata['events'][0]['homeScore']['current']
  awayscore = jsondata['events'][0]['awayScore']['current']
  return (league + " " + hometeam + " " + str(homescore)+" - "+str(awayscore) + " " + awayteam + " " + time1)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
# The commands we have to run on github for getting the livescores
  if message.content.startswith('$football score'):
    score = get_football_score()
    await message.channel.send(score)
  if message.content.startswith('$basketball score'):
    score = get_basketball_score()
    await message.channel.send(score)
keep_alive()
client.run(os.environ['TOKEN'])

