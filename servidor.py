import socket
import threading
'''
accept() aceita uma conexão do cliente
bind()  associa meu servidor a um endereço 
close() fecha
connect() faz conexão do cliente a um endereço
listen() escuta
recv(tamahp do pacote), passa a receber a mensagem
'''

# address = ('localhost', 50000)
HOST = '127.0.0.1'
PORT = 1234
limite =5
lista_clientes = [] #coloca nomes do clientes conectados

def prox_mensagem(cliente, nome):
    while 1:

        mensagem = cliente.recv(2048).decode('utf-8')
        if mensagem !='':
            mensagem_final = nome + '~' + mensagem
            enviar_mensagem(mensagem_final)

        else:
            print("A mensagem foi enviada para o cliente {} é vazia".format(nome))
#função envia mensagem para apenas um cliente      
def mensagem_cliente(cliente, mensagem):

    cliente.sendall(mensagem.encode())
#função para enviar mensagem para todos q estão conectados
def enviar_mensagem(mensagem):
    for i in lista_clientes:

        enviar_mensagem(i[1], mensagem)
        
def manipular_cliente(cliente):
    #servidor vai ouvir a mesangem do cliente
    while 1:

        nome = cliente.recv(2048).decode('utf-8')
        if nome != '':
            lista_clientes.append((nome, cliente))
            break
        else:
            print("Nome do cliente está vazio: ")

    threading.Thread(target=prox_mensagem, args=(cliente, nome, )).start()


def main():

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Familia de endereço :AF_INET = endereço IPv4/ AF_INET6 - endereço IPv6
    #Tipo de Socket: SOCK_STREAM
    try:
        servidor.bind((HOST, PORT))
        print("Foi veicular o host {} e porta {}".format(HOST, PORT))
    except:
        print("Não foi possível veicular o host {} e porta {}".format(HOST, PORT))

    servidor.listen(limite)
  
    while 1:
        cliente, endereco = servidor.accept()
        print("Cliente conectado com sucesso {}, {} ".format(endereco[0], endereco[1]))

        threading.Thread(target=manipular_cliente, args=(cliente,)).start()

main()
