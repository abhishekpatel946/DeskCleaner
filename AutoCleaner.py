from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from EventHandler import EventHandler

if __name__ == '__main__':
    watch_path = Path.home()    # root
    watch_path = watch_path / 'Desktop' / 'AREA51'
    destination_root = Path.home()      # root
    destination_root = destination_root / 'Desktop' / 'DeskCleaner'
    event_handler = EventHandler(watch_path = watch_path, destination_root = destination_root)
    observer = Observer()
    observer.schedule(event_handler, f'{watch_path}', recursive=True)
    observer.start()

    try:    
        while True:
            sleep(60)
    except KeyboardIntrrupt:
        observer.stop()
    observer.join()
