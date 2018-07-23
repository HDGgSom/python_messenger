from socket import *
from utils import *

client = socket()

client.connect(('localhost', 9090))
print('\n------СОЕДИНЕНИЕ С СЕРВЕРОМ УСТАНОВЛЕНО--------\n')

message = {
    'user': 'gSom',
    'action': 'presence'
}

send_message(client, message)

server_answer = get_message(client)
print('Код ответа сервера:', server_answer['responce'], '\nСообщение: ', server_answer['alert'])

client.close