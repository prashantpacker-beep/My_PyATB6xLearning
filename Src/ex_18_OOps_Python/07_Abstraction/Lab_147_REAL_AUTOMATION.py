from abc import ABC, abstractmethod
from webbrowser import Chrome


class BrowserManager(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Stop Command, common")

class ChromeBrowser(BrowserManager):
    def start(self):
        print("We are starting the chrome browser")

tc=ChromeBrowser()
tc.start()
tc.stop()