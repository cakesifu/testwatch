from .logger import logger

class FileTester(object):
    def test(self, filename):
        logger.debug("testing file for inclusion %s", filename)
        return True

