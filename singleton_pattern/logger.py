class Logger:
    logger_instance = None

    def get_instance(self):
        if self.logger_instance is None:
            self.logger_instance = Logger()
        return self.logger_instance

    def log(self, message):
        # save message to file
        pass
