import time

import requests
import json
import random

coords=[[41.4682974272428,41.39364168714724,41.418411945389494,41.432286772376784,41.40996089032589],[2.22804492421789,2.176728896915847,2.162798245122815,2.199220151548843,2.2082973602015272],[46.31703848925413,41.34378561569511,41.392983068484,41.40686332728126,41.359086570205136],[2.052333262952554,2.0873791502117456,2.1265776945857056,2.162999601011734,2.1358562591273085]]

# Define the base URL
base_url = "https://api.badiapp.com/v1/application/search/rooms"
# Define the headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer e06bd540627a9e6514c6a0f81c20c6837b32eb927fe28948c2b38bfd7eed062c"
}

for j in range(0,4):
    for i in range (1,3):
        # Define the parameters
        params = {
            "page": i,
            "per": 20,
            "token": "eyJwYWdlIjoyLCJwZXIiOjIwLCJvZmZzZXQiOjB9",
            "bounds[ne][lat]": coords[0][j],
            "bounds[ne][lng]": coords[1][j],
            "bounds[sw][lat]": coords[2][j],
            "bounds[sw][lng]": coords[3][j],
            "sort_by": "relevance",
            "available_from": "2024-05-16",
            "length_of_stay[]": "short",
            "place_types[]": 1
        }

        # Make the request
        response = requests.get(base_url, headers=headers, params=params)
        # Parse the JSON response
        data = response.json()
        file=open(f'rooms{random.randint(0,10000)}.json','w')
        json.dump(data,file)
        file.close()
        time.sleep(5)
