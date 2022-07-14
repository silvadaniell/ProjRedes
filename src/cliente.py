
import socket
import threading
# '''
# accept() aceita uma conexão do cliente
# bind()  associa meu servidor a um endereço 
# close() fecha
# connect() faz conexão do cliente a um endereço
# listen() escuta
# recv(tamahp do pacote), passa a receber a mensagem
# '''

address = ('localhost', 45000)
def msg_servidor(cliente):
    while True:
        mensagem = cliente.recv(2048).decode('utf-8')
        if mensagem !='':
            nome = mensagem.split("~")[0]
            depois_nome = mensagem.split('~')[1]
            print(f"[{nome}] {depois_nome} ")

        else:
            print('')
            print("Mensagem recebida do cliente está vazia")
            break

def enviar_msg_servidor(cliente):
    while True:
        mensagem = input('Mensagem: ')
        if mensagem != '':
            cliente.sendall(mensagem.encode())
        else:
            print('Mensagem Vazia')
            exit()

def conexao_servidor(cliente):
    nome = input(">>>>> Digite o nome do usuário: ")
    if nome != '':
        cliente.sendall(nome.encode())
    else:
        print(">>>>> Nome do usuário não encontrado")
        exit(0)
        
    threading.Thread(target=msg_servidor, args=(cliente,)).start()

    enviar_msg_servidor(cliente)


def main():

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((address))
        print('='*70)
        print("\t\tServidor conectado com sucesso")
        print('='*70)
        print('\n')
    except:
        print('='*70)
        print("\t\tNão foi possível veicular o host e porta {}".format(address))
        print('='*70)
        print('\n')
    conexao_servidor(cliente)

if __name__ == '__main__':
    main()
