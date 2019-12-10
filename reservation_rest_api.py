from flask import Flask, request
from reservation_service import get_qnode, read_data, register, delete_namespace
import json
import logging
from tabulate import tabulate


app = Flask(__name__)
ALLOWED_EXTENSIONS = {'xls', 'yaml', 'csv', 'json'}

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# logging.basicConfig(format=FORMAT, stream=sys.stdout, level=logging.DEBUG)
# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s [%(levelname)s] %(name)s %(lineno)d -- %(message)s",
                    datefmt='%m-%d %H:%M:%S',
                    filename='reservation_rest_api.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# # set a format which is simpler for console use
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s %(lineno)d -- %(message)s", '%m-%d %H:%M:%S')
# # tell the handler to use this format
console.setFormatter(formatter)
# # add the handler to the root logger
logging.getLogger('').addHandler(console)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/<namespace>', methods=['GET'])
def get_ns_list(namespace):
    data = read_data()
    if data:
        table = []
        headers = ['Satellite', 'Satellite URI', 'Latest qnode number', 'Prefix', 'num_of_0']
        if namespace == 'all':
            logger.debug('return all namespaces')
            for k, v in data.items():
                table.append([k, v['uri'], v['latest'], v['prefix'], v['num_of_0']])
        else:
            if namespace in data.keys():
                logger.debug('return ' + namespace + ' namespace')
                table.append([namespace, data[namespace]['uri'], data[namespace]['latest'],
                              data[namespace]['prefix'], data[namespace]['num_of_0']])
            else:
                raise Exception('Namespace does not exist in satellite.')
        return tabulate(table, headers, tablefmt="psql")

    return 'There is no satellite. Please register your satellite at first.'


@app.route('/<namespace>/reservation', methods=['GET', 'POST'])
def get_qnode_by_ns(namespace):
    if namespace:
        data = get_qnode(namespace)
        if data:
            logger.debug('reserve a qnode in ' + namespace + ' namespace')
            return json.dumps({'Latest qnode': data}, indent=2)
        else:
            raise Exception('Please register your satellite at first.')

    return 'Welcome to the reservation service.'


@app.route('/delete', methods=['GET', 'POST'])
def delete_ns():
    namespace = request.values.get('namespace')
    if namespace:
        flag = delete_namespace(namespace)
        if flag:
            logger.debug('delete ' + namespace + ' namespace success.')
            return 'Success'
        else:
            raise Exception('Namespace does not exist in satellite.')

    return 'Welcome to the reservation service.'


@app.route('/register', methods=['GET', 'POST'])
def register_ns():
    namespace = request.values.get('namespace')
    uri = request.values.get('uri')
    prefix = request.values.get('prefix')
    num_of_0 = request.values.get('num_of_0')
    if not num_of_0:
        num_of_0 = 7

    if namespace and uri and prefix:
        flag = register(namespace, uri, prefix, num_of_0)
        if flag:
            logger.debug('register ' + namespace + ' namespace success.')
            return 'Register successfully and you are ready to use this satellite. '
        else:
            raise Exception('This satellite already exists.')

    return 'Welcome to the reservation service.'


if __name__ == '__main__':
    app.run()