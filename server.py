import socket
from _thread import *
import pickle
from game import Game

server = '192.168.43.35'
port = 8754

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

games = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    print("sending....info")
    conn.send(str.encode(str(p)))
    conn.recv(4096).decode()
    conn.sendall(pickle.dumps(games[gameId]))
    while True:
        try: 
            data = conn.recv(4096).decode()
            if gameId in games:
                if data == "SEND_ME":
                    conn.send(pickle.dumps(games[gameId]))
                if data == "CLOSE":
                    break
                if data == "POST":
                    gameData = pickle.loads(conn.recv(4098))
                    games[gameId].update(gameData)
                    conn.send(pickle.dumps(games[gameId]))
            else:
                break
        except socket.error as e:
            print(e)
            break
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()    

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))