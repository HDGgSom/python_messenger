from socket import *
from utils import *

server = socket()
server.bind(('', 9090))
server.listen(5)
print('\n-------------СЕРВЕР ЗАПУЩЕН--------------\n')



while True:
    client, addr = server.accept()
    print(f'Получен запрос на соединение от {addr}')

    client_message = get_message(client)
    print(client_message)

    responce_200 = {
        'responce': 200,
        'alert': 'cоединение с сервером установлено успешно. Привет, {}!'.format(client_message['user'])
    }

    responce_400 = {
        'responce': 400,
        'alert': 'ОШИБКА: неизвестное действией со стороны клиента!'
    }

    if client_message['action'] == 'presence':
        send_message(client, responce_200)
    else:
        send_message(client, responce_400)


