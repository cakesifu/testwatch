import sys
import os
import argparse

from .file_tester import FileTester
from .test_runner import TestRunner
from .event_handler import FileEventHandler
from .watcher import Watcher
from .logger import logger

parser = argparse.ArgumentParser(description="Testwatch")
parser.add_argument("-c", "--command", nargs="+")

def run():
    args = parser.parse_args()
    command = args.command
    logger.debug('starting testwatch with command: %s', command)

    path = os.getcwd()

    runner = TestRunner(command)
    tester = FileTester()
    handler = FileEventHandler(runner, tester)

    logger.info("starting watcher in: %s", path)
    runner.run()
    Watcher(handler, path).loop()

