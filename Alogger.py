#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ahmet KÖKEN
# Email       : ahmetkkn07@gmail.com
# GitHub      : https://github.com/ahmetkkn07
# =============================================================================
"""The Module Has Been Build for Python3.6+"""
# =============================================================================
# Imports
# =============================================================================
import inspect

# #282A36


class LogLevel:
    ALL = 1000
    FATAL = 900
    ERROR = 800
    WARNING = 700
    INFO = 600
    DEBUG = 500
    TRACE = 400
    TEST = 100


class Term:
    BOLD = '\033[1m'
    REVERSE = "\033[;7m"
    CLEAR = '\033[0m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    # unused
    CYAN = '\033[96m'


class Alogger:
    def __init__(self, log_level=LogLevel.ERROR, log_to_file=False, log_name=None) -> None:
        """Constructor of Alogger class.

        Args:
            log_level (LogLevel, optional): Set level to log. Defaults to .
            log_to_file (bool, optional): Set True if you want to save logs to file. Defaults to False.
            log_name (str, optional): Custom file name for log file. Defaults to caller filename.
        """
        caller = inspect.stack()[1]    # 0 represents this line
        frame = caller[0]
        info = inspect.getframeinfo(frame)
        self.caller_filename = f"{inspect.stack()[1].filename.split('.py')[0]}"
        self.caller_lineno = info.lineno
        self.caller_function = info.function

        self.log_level = log_level
        if log_to_file:
            self.log_to_file = log_to_file
            if log_name is not None:
                self.log_name = log_name
            else:
                self.log_name = f"{self.caller_filename}.log.html"

    def fatal(self, *messages) -> None:
        if self.log_level <= LogLevel.FATAL:
            messages = [str(message) for message in messages]
            print(f"{Term.REVERSE}{Term.RED}FATAL: {' '.join(messages)}.{Term.CLEAR}")
            message = f'<div style="background-color:#FF5C57; color: #282A36;">FATAL: {" ".join(messages)}. </div>'
            self.writeToFile(message)

    def error(self, *messages) -> None:
        if self.log_level <= LogLevel.ERROR:
            messages = [str(message) for message in messages]
            print(f"{Term.RED}{Term.BOLD}ERROR: {' '.join(messages)}.{Term.CLEAR}")
            message = f'<div style="background-color:#282A36; color: #FF5C57;">ERROR: {" ".join(messages)}. </div>'
            self.writeToFile(message)

    def warning(self, *messages) -> None:
        if self.log_level <= LogLevel.WARNING:
            messages = [str(message) for message in messages]
            print(
                f"{Term.YELLOW}{Term.BOLD}WARNING: {' '.join(messages)}.{Term.CLEAR}")
            message = f'<div style="background-color:#282A36; color: #ECF299;">WARNING: {" ".join(messages)}. </div>'
            self.writeToFile(message)

    def info(self, *messages) -> None:
        if self.log_level <= LogLevel.INFO:
            messages = [str(message) for message in messages]
            print(f"{Term.GREEN}{Term.BOLD}INFO: {' '.join(messages)}.{Term.CLEAR}")
            message = f'<div style="background-color:#282A36; color: #58F18B;">INFO: {" ".join(messages)}. </div>'
            self.writeToFile(message)

    def debug(self, *messages) -> None:
        if self.log_level <= LogLevel.DEBUG:
            messages = [str(message) for message in messages]
            print(f"{Term.BLUE}{Term.BOLD}DEBUG: {' '.join(messages)}.{Term.CLEAR}")
            message = f'<div style="background-color:#282A36; color: #53BBF0;">DEBUG: {" ".join(messages)}. </div>'
            self.writeToFile(message)

    def trace(self, *messages) -> None:
        if self.log_level <= LogLevel.TRACE:
            messages = [str(message) for message in messages]
            print(f"{Term.PURPLE}{Term.BOLD}TRACE: {' '.join(messages)}.{Term.CLEAR}")
            message = f'<div style="background-color:#282A36; color: #F566BA;">TRACE: {" ".join(messages)}. </div>'
            self.writeToFile(message)

    def test(self, *messages) -> None:
        if self.log_level <= LogLevel.TEST:
            messages = [str(message) for message in messages]
            print(f"{Term.REVERSE}{Term.BOLD}TEST: {' '.join(messages)}.{Term.CLEAR}")
            message = f'<div style="background-color:#CCCCCC; color: #282A36;">TEST: {" ".join(messages)}. </div>'
            self.writeToFile(message)

    def writeToFile(self, message: str):
        with open(self.log_name, "a+") as file:
            file.write(f"{message}\n")


logger = Alogger(log_to_file=True)
logger.fatal("deneme")
logger.error("error")
logger.warning("error")