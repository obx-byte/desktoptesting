import socket

HOST="172.21.2.100"
PORT=5000



server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.settimeout(10)
server.bind((HOST,PORT))
server.listen(1)


conn,addr=server.accept()



if conn is not None:
        print(conn)



socket.close()
server.close()
