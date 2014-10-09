from .logger import logger
import subprocess

class TestRunner(object):
    def __init__(self, command):
        self.command = command

    def run(self):
        logger.info("run: %s", " ".join(self.command))
        subprocess.call(self.command)
