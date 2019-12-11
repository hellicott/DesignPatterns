from singleton_pattern.logger import Logger


class Usage:

    def main(self):
        # do something
        Logger.get_instance().log("a message")
        # do something else


class AnotherUsage:

    def main(self):
        # do stuff
        Logger.get_instance().log("another message")
        # do some other stuff


a = Usage()
b = AnotherUsage()
a.main()
b.main()