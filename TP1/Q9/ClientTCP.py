import socket


class ClientTCP:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_etudiant(self, Type, value):
        try:
            self.client.connect(("", 55555))
            print("Connected")
            if Type == "HTML":
                self.client.send("0".encode("utf-8"))
            else:
                self.client.send("1".encode("utf-8"))

            data = self.client.recv(255)
            data = data.decode("utf-8")
            print("receive " + data)

            self.client.send(value.encode("utf-8"))
            print("Send value")

            data = self.client.recv(255)
            data = data.decode("utf-8")
            print("receive " + data)
            if data == "END":
                print("Transfer successful")
                self.client.close()
                print("closing")

        finally:
            self.client.close()
