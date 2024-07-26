import time


class Timer:
    def __init__(self) -> None:
        self.start_time = 0
        self.delta = 0
    
    def announce(self, file):
        pass

    def start(self):
        self.start_time = time.time()
    
    def stop(self):
        self.delta = str(time.time() - self.start_time)
    
    def show(self):
        print(f"[\033[35mTotal Time\033[0m]: \033[31m{self.delta}\033[0m")
