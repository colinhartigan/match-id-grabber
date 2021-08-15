from valclient.client import Client 
import pyperclip

client = Client()
client.activate()
match = client.fetch_match_history()["History"][0]
pyperclip.copy(match["MatchID"])