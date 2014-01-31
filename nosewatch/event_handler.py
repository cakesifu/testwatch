import pyinotify
import time

from .logger import logger
def now():
    return int(round(time.time() * 1000))

class FileEventHandler(pyinotify.ProcessEvent):

    delay = 400

    def __init__(self, runner, tester):
        self.runner = runner
        self.tester = tester
        self.queue = {}
        self._last_change = 0

    def process_default(self, event):
        logger.debug("file event caught %s - %s", event.pathname, event.maskname)
        if self.tester.test(event.pathname):
            self._process_file(event.pathname, event.maskname)

    def _process_file(self, filename, event):
        if filename in self.queue:
            existing_events = self.queue[filename]
            if 'IN_CREATE' in existing_events and event == 'IN_DELETE':
                logger.debug("create delete in same cycle: %s", filename)
                del(self.queue[filename])
            else:
                self.queue[filename].append(event)
                self._reset_clock()
        else:
            self.queue[filename] = [event]
            self._reset_clock()

    def process_queue(self):
        if len(self.queue):
            time_delta = self._time_since_last_change()
            if time_delta >= self.delay:
                logger.debug("time(ms) since last change: %d", time_delta)
                self._print_files()
                self.queue = {}
                self._reset_clock()
                self.runner.run()

    def _reset_clock(self):
        self._last_change = now()

    def _time_since_last_change(self):
        return (now() - self._last_change)

    def _print_files(self):
        for filename in self.queue:
            action = "changed"
            logger.info("file %s - %s", filename, action)
