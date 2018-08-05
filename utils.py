import json

def dict_to_bytes(data):
    js_message = json.dumps(data)
    byte_message = js_message.encode('utf-8')
    return byte_message

def bytes_to_dict(data):
    decoded_message = data.decode('utf-8')
    js_message = json.loads(decoded_message)
    return js_message

def get_message(sock):
    message = sock.recv(1024)
    decoded_message = bytes_to_dict(message)
    return decoded_message

def send_message(sock, message):
    encoded_message = dict_to_bytes(message)
    sock.send(encoded_message)

