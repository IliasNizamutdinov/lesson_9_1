import requests
from pprint import pprint

if __name__ == '__main__':

    TOKEN = 2619421814940190
    dict_name = dict.fromkeys(["Hulk","Captain America","Thanos"])

    for name in dict_name.keys():
        url_n = f"https://superheroapi.com/api/{TOKEN}/search/{name}"
        resp = requests.get(url_n)
        id = resp.json()['results'][0]['id']
        url_id = f"https://superheroapi.com/api/{TOKEN}/{id}/powerstats"
        resp_p = requests.get(url_id)
        dict_name[name] = resp_p.json()["intelligence"]

    dict_name_s = dict(sorted(dict_name.items()))

    pprint(dict_name_s)

