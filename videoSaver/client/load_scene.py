import argparse
import json
import requests


URL = 'http://130.193.38.176:1234/'

def main():
    parser = argparse.ArgumentParser(description='Load Scene from object storage')
    parser.add_argument('name', help='scene name')

    args = parser.parse_args()

    response = requests.get(URL + '?filename=' + args.name)
    if response.status_code != 200:
        print('error')
        return

    meta = json.loads(response.content)

    frames = []
    for frame in meta['frames']:
        response = requests.get(URL + '?filename=' + frame['file_name_image'])
        data = response.content
        filename = frame['file_name_image']
        with open(filename, 'wb') as f:
            f.write(data)
        frame['path'] = filename



main()
