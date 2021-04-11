import argparse
import json
import requests


URL = ':1234/'

def main():
    parser = argparse.ArgumentParser(description='Load Scene from object storage')
    parser.add_argument('name', type=string, help='scene name')

    args = parser.parse_args()

    response = requests.get(URL + '?filename=' + args.name)
    if response.status_code != 200:
        print('error')
        return

    meta = json.loads(response.content)

    frames = []
    for frame in meta['frames']:
        response = requests.get(URL + '?filename=' + frame['path'])
        data = requests.get(URL + '?filename=' + args.name)
        filename = ''
        with open(filename, 'w') as f:
            f.write(data)
        frame['path'] = filename



main()
