import socket
import json
import sys

HOST = '127.0.0.1'
PORT = 9563

try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except (socket.error) as e:
  print("Error1: %s" % e)
  sys.exit(1)

try:
  sock.connect((HOST, PORT))
except (socket.error) as e:
  print("Error2: %s" % e)
  sys.exit(2)

msg = {'@message': 'python test message', '@tags': ['python', 'test']}

sock.send(str.encode(json.dumps(msg)))

sock.close()
sys.exit(0)