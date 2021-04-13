import argparse
import json
import requests


URL = 'http://84.201.174.97:1234/'

def reformat_intrinsics(old_intrinsics):
    answer = list()
    num = 0
    for i in range(3):
        cur = list()
        for j in range(3):
            cur.append(old_intrinsics[num])
            num += 1
        answer.append(cur)
    return answer

def reformat_pose(old_pose):
    answer = list()
    num = 0
    for i in range(4):
        cur = list()
        for j in range(4):
            cur.append(old_pose[num])
            num += 1
        answer.append(cur)
    return answer


def main():
    parser = argparse.ArgumentParser(description='Load Scene from object storage')
    parser.add_argument('name', help='scene name')

    args = parser.parse_args()

    response = requests.get(URL + '?filename=' + args.name)
    if response.status_code != 200:
        print('error')
        return

    meta = json.loads(response.content)

    meta['scene'] = args.name
    meta['dataset'] = 'sample'
    meta['path'] = '.'


    frames = []
    for frame in meta['frames']:
        response = requests.get(URL + '?filename=' + frame['file_name_image'])
        data = response.content
        filename = frame['file_name_image']
        with open(filename, 'wb') as f:
            f.write(data)
        frame['path'] = filename
        frame['pose'] = reformat_pose(frame['pose'])
        frame['intrinsics'] = reformat_intrinsics(frame['intrinsics'])
        
    with open(args.name + '.json', 'w') as f:
        f.write(json.dumps(meta))


main()
