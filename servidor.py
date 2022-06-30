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
limite = 5
lista_clientes = [] #coloca nomes do clientes conectados

def prox_mensagem(cliente, nome):
    while 1:
        mensagem = cliente.recv(2048).decode('utf-8')
        if mensagem !='':

            mensagem_final = nome + '~' + mensagem
            enviar_mensagem(mensagem_final)

        else:
            print('')
            print(f"A mensagem enviada para o cliente {nome} é vazia")
            break

#função envia mensagem para apenas um cliente      
def mensagem_cliente(cliente, mensagem):

    cliente.sendall(mensagem.encode())
#função para enviar mensagem para todos que  estão conectados
def enviar_mensagem(mensagem):
    for i in lista_clientes:

        mensagem_cliente(i[1], mensagem)
        
def manipular_cliente(cliente):
    #servidor vai ouvir a mesangem do cliente
    while 1:

        nome = cliente.recv(2048).decode('utf-8')
        if nome != '':
            lista_clientes.append((nome, cliente))
            usuarioEntra = 'SERVIDOR~' + f"{nome} Entrou no Chat"
            enviar_mensagem(usuarioEntra)

            break
        else:
            print(">>>> Nome do cliente está vazio")
            break;
    threading.Thread(target=prox_mensagem, args=(cliente, nome, )).start()


def main():

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Familia de endereço :AF_INET = endereço IPv4/ AF_INET6 - endereço IPv6
    #Tipo de Socket: SOCK_STREAM
    try:
        servidor.bind(address)
        print('='*70)
        print("\tFoi veicular o host e porta {}".format(address))
        print('='*70)
        print('')
    except:
        print('='*70)
        print("\tNão foi possível veicular o host e porta {}".format(address ))
        print('='*70)
        print('')

    servidor.listen(limite)
  
    while True:
        cliente, endereco = servidor.accept()
        print(">>> Cliente conectado com sucesso {}, {} ".format(endereco[0], endereco[1]))

        threading.Thread(target=manipular_cliente, args=(cliente,)).start()

if __name__ == '__main__':
    main()
