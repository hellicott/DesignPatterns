class Logger:
    _logger_instance = None

    @staticmethod
    def get_instance():
        if Logger._logger_instance is None:
            Logger._logger_instance = Logger()
        return Logger._logger_instance

    def log(self, message):
        # save message to file
        pass
