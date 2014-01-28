import sys
import nose

class Logger(object):

    def info(self, message):
        print message


class TestRunner(object):
    def run(self):
        nose.main()


from pyinotify import WatchManager, Notifier, EventsCodes, ProcessEvent

def run():
    logger = Logger()
    runner = TestRunner()
    logger.info('Starting watcher with args: %s' % sys.argv[1:])
    runner.run()

# watcher
