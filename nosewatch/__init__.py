import sys
import os
import nose
import pyinotify
import logging

class Logger(object):

    def info(self, message):
        print message

class TestRunner(object):
    def run(self):
        logging.info("Starting tests.")
        nose.main(exit=False)

class FileTester(object):
    def test(self, filename):
        logging.debug("Start testing %s", filename)
        return True


class FileEventHandler(pyinotify.ProcessEvent):
    def __init__(self, runner, tester):
        self.runner = runner
        self.tester = tester

    def process_default(self, event):
        logging.debug("Event caught %s - %s", event.pathname, event.maskname)
        self.process_file(event.pathname)

    def process_file(self, filename):
        if self.tester.test(filename):
            logging.info("File %s changed", filename)
            self.runner.run()

def run():
    if os.environ.get('DEBUG', False):
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info('Starting watcher with args: %s' % sys.argv[1:])

    MASK = pyinotify.IN_DELETE  \
         | pyinotify.IN_CREATE \
         | pyinotify.IN_MODIFY

    path = os.getcwd()
    logging.debug("Current working dir: %s", path)

    runner = TestRunner()
    tester = FileTester()

    watch_manager = pyinotify.WatchManager()
    handler = FileEventHandler(runner, tester)
    notifier = pyinotify.Notifier(watch_manager, handler)
    watch_descriptor = watch_manager.add_watch(path, MASK, rec=True)

    notifier.loop()
