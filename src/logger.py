import logging


class Logger:
    def __init__(self, debug=False, write=False):
        self.debug = debug
        self.is_write = write
        self.console = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

        if self.is_write:
            file_handler = logging.FileHandler('app.log')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        elif self.debug:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

        return logger

    def log(self, _type, message):
        if not self.debug:
            return

        getattr(self.console, _type)(message)
