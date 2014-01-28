import sys
import nose

class Logger(object):

    def info(self, message):
        print message

logger = Logger()

class TestRunner(object):
    def run(self):
        nose.main()

runner = TestRunner()

def run():
    logger.info('Starting watcher with args: %s' % sys.argv)
    runner.run()
