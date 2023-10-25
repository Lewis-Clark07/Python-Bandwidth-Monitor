import time
import psutil

Last_Received = psutil.net_io_counters().bytes_recv
Last_Sent = psutil.net_io_counters().bytes_sent
Last_Total = Last_Received + Last_Sent

while True:
    Bytes_Received = psutil.net_io_counters().bytes_recv
    Bytes_Sent = psutil.net_io_counters().bytes_sent
    Bytes_Total = Bytes_Received + Bytes_Sent

    New_Received = Bytes_Received - Last_Received
    New_sent = Bytes_Sent - Last_Sent
    New_Total = Bytes_Total - Last_Total

    Mb_New_Recieved = New_Received / 1024 / 1024
    Mb_New_Sent = New_sent / 1024 / 1024
    Mb_New_Total = New_Total / 1024 / 1024

    print(f"{Mb_New_Recieved: .2f} MB recieved, {Mb_New_Sent: .2f} MB sent, {Mb_New_Total: .2f} MB total")

    Last_Received = Bytes_Received
    Last_Sent = Bytes_Sent
    Last_Total = Bytes_Total

    time.sleep(1)