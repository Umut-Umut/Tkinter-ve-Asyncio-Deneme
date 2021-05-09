import asyncio
from interface import main_label

class Timer:
    def __init__(self, start=0, entry=0):
        self.time_start = start
        self.time_now = 0
        self.entry = entry
        self.is_start = False
        self.is_over = False


    async def start(self):
        if self.is_start:
            return 0
        else:
            time = self.entry.get()
            if time == "": time = 0
            else:
                self.time_start = int(time)
                self.time_now   = int(time)

            self.is_start = True
            for _i in range(self.time_start):
                main_label.config(text=self.time_now)
                await asyncio.sleep(1)
                self.time_now -= 1

            self.is_over = True