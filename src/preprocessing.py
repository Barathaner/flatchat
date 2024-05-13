import pandas as pd
import os
import requests
import ast
import shutil


def download_images(df, column):
    for index, row in df.iterrows():
        room_id = row['room_id']
        picture_urls = row[column]

        # Create a directory for the room if it doesn't exist
        if not os.path.exists(f'pictures/{room_id}'):
            os.makedirs(f'pictures/{room_id}')
        actual_list = ast.literal_eval(picture_urls)

        for i, url in enumerate(actual_list):
            # Download the image
            response = requests.get(url, stream=True)
            with open(f'pictures/{room_id}/{i}.jpg', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response


df = pd.read_csv('rooms.csv')

#delete duplicates, if any
df = df.drop_duplicates()
#save the dataframe to a csv file
df.to_csv('rooms.csv', index=False)

download_images(df, 'pictures')

#iterate over column pictures and download the images, the column pictures contains a list of urls
