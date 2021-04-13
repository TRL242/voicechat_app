from vidstream import AudioSender
from vidstream import AudioReceiver
import threading
import socket

local_ip = socket.gethostname(socket.gethostname())

receiver = AudioReceiver(local_ip, 9999)
receive_thread = threading.Thread(target=receiver.start_server)

other_ip = #ip from other computer using the same script.
#sender should use other local ip but i have mine twice
sender = AudioSender(other_ip, 5545)
sender_thread = threading.Thread(target=sender.start_stream)

receive_thread.start()
sender_thread.start()