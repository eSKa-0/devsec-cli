
import time
from tcpchatOk import Tcpchat

try:
    tcp = Tcpchat()
    while True:
        time.sleep(1)
        try:
            tcp.check()
        except:
            time.sleep(1)
            print("")
except Exception as e:
    print(e)
    time.sleep(100)