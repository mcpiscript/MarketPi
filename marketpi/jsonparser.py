from urllib.request import urlopen
import json

def get_world_list(url: str):
    result = json.loads(urlopen(url).read())
    
    return result["worlds"]
    
