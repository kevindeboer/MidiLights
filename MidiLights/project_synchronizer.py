import sys
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirModifiedEvent
from threading import Thread


class DirectorySynchronizerHandler(FileSystemEventHandler):
    """Synchronize when a file is changed in the source path."""
    def __init__(self, source_path, pi_destination_path):
        self.source_path = source_path
        self.pi_destination_path = pi_destination_path
        self.synchronizer = DirectorySynchronizer(self.source_path, self.pi_destination_path)
        print('Synchronizing source {0} with {1}'.format(self.source_path, self.pi_destination_path))
        self.synchronize()

    def on_any_event(self, event):
        if not isinstance(event, DirModifiedEvent):
            print(event)
        if not self.synchronizer.isAlive():
            self.synchronize()

    def synchronize(self):
        self.synchronizer.start()


class DirectorySynchronizer(Thread):
    """Synchronize my working directory with a directory on the pi."""
    def __init__(self, source_path, pi_destination_path):
        Thread.__init__(self)
        self.source_path = source_path
        self.pi_destination_path = pi_destination_path

    def sync_directories(self):
        print("sync source: '{0}' -> destination '{1}'".format(self.source_path, self.pi_destination_path))
        command = "rsync -avz {0} -e ssh pi@192.168.188.2:{1} --delete".format(self.source_path, self.pi_destination_path)
        os.system(command)

    def run(self):
        print('rsync in 1 second')
        time.sleep(1)
        self.sync_directories()
        print('rsync complete')
        

if __name__ == "__main__":
    current_directory = '.'
    event_handler = DirectorySynchronizerHandler(current_directory, "Projects/MidiLights")
    observer = Observer()
    observer.schedule(event_handler, current_directory, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()