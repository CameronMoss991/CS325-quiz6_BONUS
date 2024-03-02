from abc import ABC, abstractmethod

# Abstract logging interface
class Logger(ABC):
    @abstractmethod
    def debug(self, message):
        print("logger debug")

    @abstractmethod
    def info(self, message):
        print("logger info")

    @abstractmethod
    def warning(self, message):
        print("login warning")

    @abstractmethod
    def error(self, message):
        print("logger error")

# Implementation of the abstract logging interface using the logging library
class LoggingLibraryLogger(Logger):
    def debug(self, message):
        print("logger library_debug")

    def info(self, message):
        print("logger library_info")

    def warning(self, message):
        print("logger library_warning")

    def error(self, message):
        print("logger library_error")

# Application logic that depends on the abstract logging interface
class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def do_something(self):
        self.logger.info("Doing something...")

# Configuration
def get_logger() -> Logger:
    # Decide which logging library implementation to use. Designed for flexibility
    return LoggingLibraryLogger()

def main():
    logger = get_logger()
    app = Application(logger)
    app.do_something()

if __name__ == "__main__":
    main()
