# -*- coding: utf-8 -*-

# Importa módulo socket, que forma base das comunicações em rede em Python
import socket as sk

#Diretório que contem o arquivo para a transição
Diretorio = 'M:/Documentos/EE P14 - 21.1/Redes de Computadores'
Tipo = '.txt'

# Define número de porta do processo servidor
serverPort = 12000 #8081

# Cria soquete TCP do servidor
serverSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM) 
serverSocket.bind(('', serverPort))  

# Servidor aguarda requisições de conexão TCP de cliente (parâmetro especifica número máximo de conexões em fila)
serverSocket.listen(10)

print('Servidor pronto para receber!')


while True:
    # accept() aceita conexão com cliente e cria soquete provisório
	connectionSocket, addr = serverSocket.accept()
    print ('Conexao Realizada!')
    
    try:
        
        #Linhas de cabeçalho
        linha1 = 'Conexao: '
        linha2 = 'Servidor: Server_Carlos'
        linha3 = 'Tipo de Conteudo: text/html'
    
	    # recv() recebe mensagem pelo soquete
	    message = connectionSocket.recv(4096) 
	    # Coloca string em formato enviado
	    decodePacote = message.decode(format(message)).upper()
        print(DecodPacote)
        # Seleciona o nome do arquivo
        NomeArquivo = decodePacote.split()[0][0:]
        # Abrir o arquivo solicitado
        Arquivo = open(Diretorio + NomeArquivo + Tipo, 'r')     
        # Leitura do arquivo
        Conteudo = Arquivo.read()         
        # Resposta para o cliente
        Mensagem = '\n Mensagem'+linha1+'\n'+linha2+'\n'+linha3
        Conteudo1 = bytes(Conteudo, 'utf-8')
        Mensagem1 = bytes(Mensagem, 'utf-8')
        
	    # send() envia mensagem para o cliente pelo soquete, contendo conteudo e arquivo
        connection.send(Conteudo1)
        connection.send(Mensagem1)
        print(Conteudo)
        print(Mensagem)
        Arquivo.close() 
	    # Fecha soquete provisório de conexão com cliente
	    connectionSocket.close()
        
    except IOError:
        
        #Mensagem de erro
        erro = '\n 404 Not Found'             
        MensRespost=bytes(erro, 'utf-8')
        
        # Envia mensagem de erro
        connectionSocket.send(MensRespost)
        print(MensRespost)
        connectionSocket.close()
    
print('Servidor encerrando...')
serverSocket.close()
