from .logger import logger

class FileTester(object):
    def test(self, filename):
        logger.debug("testing file %s", filename)
        return True

