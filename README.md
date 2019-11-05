# HERE | Keyboard environment

To run graphical mode from a notebook:

````
from threading import Thread

def run():
    %run -i -m keyboard_environment.main GRAPHIC

t = Thread(target=run)
t.start()
````
