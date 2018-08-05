from socket import *
from utils import JIM
from select import *

def new_listen_socket(address):
    sock = socket()
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(0.2)
    return sock

def mainloop():
    address = ('', 9090)
    clients = []
    server = new_listen_socket(address)

    while True:


        try:
            client, addr = server.accept()

            msg = JIM.get_message(client)

            responce_200 = {
                'responce': 200,
                'alert': 'Соединение с сервером установлено успешно. Привет, {}!'.format(msg['user'])
            }

            responce_400 = {

                'responce': 400,
                'alert': '------ОШИБКА!------Некорректное действие со стороны клиента!'
            }

            print(msg)

            if msg['action'] == 'presence':
                JIM.send_responce(client, responce_200)

            else:
                JIM.send_responce(client, responce_400)

        except OSError as e:
            pass
        else:
            print('Получен запрос на соединение от {}'.format(addr))
            clients.append(client)
        finally:
            r = []
            w = []
            try:
                r, w, e = select(clients, clients, [], 0)
            except Exception as e:
                pass
            for some_client in r:
                try:
                    client_msg = JIM.get_message(some_client)
                    print(client_msg)
                    for some_client in w:
                        JIM.send_responce(some_client, client_msg)

                except:
                    print('Клиент {} отключился'.format(client.getpeername()))
                    clients.remove(some_client)

print('----------------------------СЕРВЕР ЗАПУЩЕН------------------------------')
mainloop()

