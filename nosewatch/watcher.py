import pyinotify
import time

from .logger import logger
class Watcher(object):

    mask = pyinotify.IN_DELETE  \
         | pyinotify.IN_CREATE \
         | pyinotify.IN_MODIFY

    # poll rate(in Hz) for I/O events
    poll_rate = 8

    def __init__(self, handler, path):
        self.wm = pyinotify.WatchManager()
        self.handler = handler
        self.notifier = pyinotify.Notifier(self.wm, handler, timeout=10)
        self.wd = self.wm.add_watch(path, self.mask, rec=True)

    def check(self):
        self.notifier.process_events()
        while self.notifier.check_events():
            self.notifier.read_events()
            self.notifier.process_events()

    def loop(self):
        try:
            while True:
                self.check()
                self.handler.process_queue()
                time.sleep(1 / self.poll_rate)

        except KeyboardInterrupt:
            return
