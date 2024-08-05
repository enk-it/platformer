import curses
import asyncio

from modules.Application import Application

app = Application()

if __name__ == '__main__':
    asyncio.run(curses.wrapper(app.main))
