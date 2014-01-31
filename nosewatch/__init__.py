import sys
import os

from .file_tester import FileTester
from .test_runner import TestRunner
from .event_handler import FileEventHandler
from .watcher import Watcher
from .logger import logger

def run():

    logger.debug('Starting watcher with args: %s' % sys.argv[1:])
    path = os.getcwd()

    runner = TestRunner()
    tester = FileTester()
    handler = FileEventHandler(runner, tester)

    logger.info("Starting watcher in: %s", path)
    Watcher(handler, path).loop()
