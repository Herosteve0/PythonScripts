IP = '62.74.9.219'

from pyartnet import ArtNetNode
import asyncio

from Par0 import Par0

async def main():
    node = ArtNetNode(IP, 6454)
    light1 = Par0(node, 0, 0)
    node.start_refresh()

    light1.setFade(255, 1)
    light1.setColor(red=255, timespan=5)
    await asyncio.sleep(3)
    light1.setColor(blue=255, timespan=2)

    await asyncio.sleep(2)

    light1.blackout()

    node.stop_refresh()

asyncio.run(main())