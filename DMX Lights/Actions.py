IP = '127.0.0.1'

from pyartnet import ArtNetNode
import asyncio

from Par0 import Par0

async def instance():
    global node
    node = ArtNetNode(IP, 6454)

async def program1():
    global node

    node = ArtNetNode(IP, 6454)
    light1 = Par0(node, 0, 363)
    node.start_refresh()

    light1.setFade(255, 1)
    light1.setColor(red=255, timespan=5)
    await asyncio.sleep(3)
    light1.setColor(green=255, timespan=2)

    await asyncio.sleep(2)

    light1.blackout()

    node.stop_refresh()
async def program2():
    global node

    node = ArtNetNode(IP, 6454)
    light1 = Par0(node, 0, 0)
    node.start_refresh()

    light1.setFade(255, 1)
    light1.setColor(green=255, timespan=5)
    await asyncio.sleep(3)
    light1.setColor(blue=255, timespan=2)

    await asyncio.sleep(2)

    light1.blackout()

    node.stop_refresh()
async def program3():
    global node

    node = ArtNetNode(IP, 6454)
    light1 = Par0(node, 0, 0)
    node.start_refresh()

    light1.setFade(255, 1)
    light1.setColor(blue=255, timespan=5)
    await asyncio.sleep(3)
    light1.setColor(red=255, timespan=2)

    await asyncio.sleep(2)

    light1.blackout()

    node.stop_refresh()

asyncio.run(instance())

exeprogram = program1

print("program start")
asyncio.run(exeprogram())
print("program finished")