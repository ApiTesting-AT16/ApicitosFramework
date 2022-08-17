import inspect
import logging


class CustomLogger:

    def logger(self, logLevel=logging.DEBUG):
        # Set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        # Create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        # Create console handler or file handler and set the log level
        log_file = logging.FileHandler("automation.log")
        # Create formatter how you want your logs to be formatted
        formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # Add formatter to console or file handler
        log_file.setFormatter(formatter)
        # Add console handler to logger
        logger.addHandler(log_file)
        return logger
