import nose

from .logger import logger
class TestRunner(object):
    def run(self):
        logger.info("Starting tests.")
        nose.main(exit=False)
