import os
import json


dir = os.path.split(os.path.realpath(__file__))[0]
path = os.path.join(dir, 'reservation.json')


def read_data():
    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()
            data = json.loads(content)
    else:
        data = {}
    return data


def write_data(data):
    content = json.dumps(data, indent=4)
    with open(path, 'w') as f:
        f.write(content)


def format_qnode(latest):
    if latest < 100000:
        temp = "%06d" % latest
    else:
        temp = str(latest)
    return 'Q' + temp


def get_qnode(namespace) -> dict():
    data = read_data()
    if not data or namespace not in data.keys():
        return None
    if namespace in data.keys():
        latest = data[namespace]['latest']
        data[namespace]['latest'] += 1
    write_data(data)
    return format_qnode(latest)


def register(namespace, uri):
    data = read_data()
    if not data or namespace not in data.keys():
        data[namespace] = {'uri': uri, 'latest': 1}
        write_data(data)
        return True
    if namespace in data.keys():
        return False

# if __name__ == "__main__":
#     namespace = 'dm'
#     outputs = get_qnode(namespace)
#     print(outputs)
