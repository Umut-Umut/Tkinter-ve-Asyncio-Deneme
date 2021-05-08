from interface import win
from timer import *

widgets = win.children

async def render():
    timer = Timer(entry = widgets['!entry'])

    widgets['!frame'].children['!button'].config(
        text="Start",
        command=lambda: asyncio.create_task(timer.start())
        )

        # MAIN LOOP
    while True:
        await asyncio.sleep(0)

        widgets['!label'].config(text=timer.time_now)
        if timer.is_over:
            win.geometry("500x500")
            widgets['!label'].config(text="Sure Bitti Mod Damn")

        # UPDATE WIDGETS
        for i in widgets.values():
            i.update()
        
        win.update()


async def main():
    await asyncio.create_task(render())


asyncio.run(main())