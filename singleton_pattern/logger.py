class Logger:
    _logger_instance = None

    @staticmethod
    def get_instance():
        if Logger._logger_instance is None:
            Logger._logger_instance = Logger()
            print("new Logger instance: {}".format(Logger._logger_instance))
        return Logger._logger_instance

    def log(self, message):
        # save message to file
        print("{} logging: {}".format(self, message))
