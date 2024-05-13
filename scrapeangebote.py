
import pandas as pd
import json
import random
# Load the data

for i in range(0, 7):
    with open(f'./rooms{i}.json') as f:
        data = json.load(f)
    import os

    # Check if the file exists and is not empty
    if os.path.isfile('rooms.csv') and os.stat('rooms.csv').st_size != 0:
        df = pd.read_csv('rooms.csv')
    else:
        df = pd.DataFrame(columns=['room_id', 'headline', 'subheading', 'price', 'pictures'])
    # Extract the results
    results = data['data']['results']

    # Initialize lists to store data
    room_ids = []
    headlines = []
    subheadings = []
    prices = []
    pictures = []

    # Loop through the results and extract data
    for result in results:
        room_ids.append(result['attributes']['room_id'])
        headlines.append(result['attributes']['headline']['content'])
        subheadings.append(result['attributes']['subheading']['content'])
        prices.append(result['attributes']['extra_info'][0]['body']['content'])
        pictures.append([item['url'] for item in result['attributes']['pictures']['items']])

    # Create a DataFrame
    df2 = pd.DataFrame({
        'room_id': room_ids,
        'headline': headlines,
        'subheading': subheadings,
        'price': prices,
        'pictures': pictures
    })
    print(type(df))
    df = pd.concat([df, pd.DataFrame(df2)])
df.to_csv('rooms.csv', index=False)
# Print the DataFrame