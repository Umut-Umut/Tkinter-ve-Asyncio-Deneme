import asyncio

class Timer:
    def __init__(self, start=0, stop=0, entry=0):
        self.time_start = start
        self.time_stop  = stop
        self.time_now   = start
        self.is_over    = False
        self.entry      = entry


    async def start(self):
        if self.time_now != self.time_start:
            return 0
        else:
            time = self.entry.get()
            if time == "": time = 0
            else:
                self.time_start = int(time)
                self.time_now   = int(time)

            while not self.is_over:
                await asyncio.sleep(1)
                if self.time_now == self.time_stop:
                    self.is_over = True
                    break
                else: self.time_now -= 1