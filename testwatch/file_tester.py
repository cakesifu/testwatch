from .logger import logger

class FileTester(object):
    def __init__(self, **options):
        self.options = options

    def test(self, filename):
        out = not filename.endswith(".pyc") \
              and filename.endswith(".py")
        logger.debug("testing file for inclusion %s: %s", filename, out)
        return out

