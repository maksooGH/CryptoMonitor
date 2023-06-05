import requests
import json

import src.utls as utls

urlGainers = "https://discord.com/api/webhooks/1115308486851567718/DsHgMQlVDm3H6T_0CRksbf0jZYIhwVYlamp_xM9qr3LoJcK1oyS6Qo47gT74Hd0RuHkh"
urlLosers = "https://discord.com/api/webhooks/1115308625821450313/nNoB1A_3Kko14vhl2DDK99DM8HhwKsjVgcl-eV52AOEP21fUfe-I6zSCxVIJzod2O3ao"

def prepare_and_send_webhooks(data, gainers_webhook_url=urlGainers, losers_webhook_url=urlLosers):
    gainers = [d for d in data if d['LastChange'] > 0.75]
    losers = [d for d in data if d['LastChange'] < -0.75]
    losers = utls.sort_dict_list_asc(losers)
    gainers = utls.sort_dict_list_desc(gainers)
    gainers_embed = {
       
        "embeds": [{
            "title": "Last 1h - Top Gainers",
            "description": "\n".join([f"{g['Ticker']} ({g['LastChange']}%)" for g in gainers]),
            "color": 65280
        }]
    }

    losers_embed = {
        
        "embeds": [{
            "title": "Last 1h - Top Losers",
            "description": "\n".join([f"{l['Ticker']} ({l['LastChange']}%)" for l in losers]),
            "color": 16711680
        }]
    }

    requests.post(gainers_webhook_url, data=json.dumps(gainers_embed), headers={"Content-Type": "application/json"})
    requests.post(losers_webhook_url, data=json.dumps(losers_embed), headers={"Content-Type": "application/json"})
