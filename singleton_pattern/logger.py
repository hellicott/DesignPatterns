class Logger:
    _logger_instance = None

    @staticmethod
    def get_instance():
        if Logger._logger_instance is None:
            print("creating new instance")
            Logger._logger_instance = Logger()
        return Logger._logger_instance

    def log(self, message):
        # save message to file
        print("logging: {}".format(message))
