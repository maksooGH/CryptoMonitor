import requests
import json

import src.utls as utls

def prepare_and_send_webhooks(data, gainers_webhook_url, losers_webhook_url):
    gainers = [d for d in data if d['LastChange'] > 0.5]
    losers = [d for d in data if d['LastChange'] < -0.5]
    losers = utls.sort_dict_list_asc(losers)
    gainers = utls.sort_dict_list_desc(gainers)
    gainers_embed = {
       
        "embeds": [{
            "title": "Last 1h - Top Gainers",
            "description": "\n".join([f"{g['Ticker']}          ({g['LastChange']}%)" for g in gainers]),
            "color": 65280
        }]
    }

    losers_embed = {
        
        "embeds": [{
            "title": "Last 1h - Top Losers",
            "description": "\n".join([f"{l['Ticker']}          ({l['LastChange']}%)" for l in losers]),
            "color": 16711680
        }]
    }

    requests.post(gainers_webhook_url, data=json.dumps(gainers_embed), headers={"Content-Type": "application/json"})
    requests.post(losers_webhook_url, data=json.dumps(losers_embed), headers={"Content-Type": "application/json"})
