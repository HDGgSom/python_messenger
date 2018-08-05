
import json
import logging

class Log:

    def __init__(self, show_params=True):
        self.show_params = show_params

    def __call__(self, func):

        def new_log(*args, **kwargs):

            log = logging.getLogger('basic')

            if self.show_params:
                logging.basicConfig(
                    filename='server_log.log',
                    format='%(levelname)-10s %(asctime)s    function name: {}    аргументы функции: {}  %(message)s'.format(
                        func.__name__, (args, kwargs)),
                    level=logging.DEBUG
                )
                log.info(func)
            else:
                logging.basicConfig(
                    filename='server_log.log',
                    format='%(levelname)-10s %(asctime)s    function name: {} %(message)s'.format(func.__name__),
                    level=logging.DEBUG
                )
                log.info(func)
            result = func(*args, **kwargs)
            return result

        return new_log

log = Log()

@Log(show_params=False)
def dict_to_bytes(data):
    jmessage = json.dumps(data)
    bytemessage = jmessage.encode('utf-8')
    return bytemessage

@Log(show_params=False)
def bytes_to_dict(data):
    decoded_message = data.decode('utf-8')
    js = json.loads(decoded_message)
    return js

class JIM:

    @log
    def get_message(sock):
        message = sock.recv(1024)
        dec_msg = bytes_to_dict(message)
        return dec_msg

    @log
    def send_message(message, client):
        bytemessage = dict_to_bytes(message)
        client.send(bytemessage)

    @log
    def send_responce(client, responce):
        js_responce = json.dumps(responce)
        client.send(js_responce.encode('utf-8'))