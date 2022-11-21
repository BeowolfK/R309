import socket


serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("", 55555))
serveur.listen(5)
print("Start listening")
while True:
    client, infosClient = serveur.accept()
    print("Accept client: " + infosClient[0])
    data = client.recv(255)
    Type = data.decode("utf8")
    print("Receive type " + Type)
    flag = int(Type) == 0

    client.send("TYPE".encode("utf-8"))

    data = client.recv(2048)
    data = data.decode("utf8")
    if flag:
        with open("etudiant.html", "w+") as html_file:
            html_file.write(data)
    else:
        with open("etudiant.json", "w+") as json_file:
            json_file.write(data)

    print("Receive value, ending connexion")
    client.send("END".encode("utf-8"))
    client.close()
