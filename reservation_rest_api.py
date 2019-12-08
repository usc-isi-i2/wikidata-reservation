from flask import Flask, request
from reservation_service import get_qnode, read_data, register
import json
from tabulate import tabulate


app = Flask(__name__)
ALLOWED_EXTENSIONS = {'xls', 'yaml', 'csv', 'json'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def get_ns_list():
    data = read_data()
    if data:
        table = []
        headers = ['Satellite', 'Satellite URI', 'Latest qnode']
        for k, v in data.items():
            table.append([k, v['uri'], v['latest']])
        return tabulate(table, headers, tablefmt="psql")

    return 'There is no satellite. Please register your satellite at first.'


@app.route('/reservation', methods=['GET', 'POST'])
def get_qnode_by_ns():
    namespace = request.values.get('namespace')
    if namespace:
        data = get_qnode(namespace)
        if data:
            return json.dumps({'Latest qnode': data}, indent=2)
        else:
            return 'Please register your satellite at first.'

    return 'Welcome to the reservation service.'


@app.route('/register', methods=['GET', 'POST'])
def register_ns():
    namespace = request.values.get('namespace')
    uri = request.values.get('uri')
    if namespace and uri:
        flag = register(namespace, uri)
        if flag:
            return 'Register successfully and you are ready to use this satellite. '
        else:
            return 'This satellite already exists.'

    return 'Welcome to the reservation service.'


if __name__ == '__main__':
    app.run()