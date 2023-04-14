import asyncio
import websockets
import time

import utils, config

# WS Server
async def hello(websocket):
    # Validation
    name = await websocket.recv()
    print(time.strftime("%X") + \
          ' << ', name)

    await websocket.send(f"Hello {name}!")
    print(time.strftime("%X") + \
          ' >>', f"Hello {name}!")
    # Listen Message from Front-End
    while True:
        msg = await websocket.recv()
        if utils.isCMDLegal(msg):
            print(time.strftime("%X") + \
                  ' <<', msg)
            await websocket.send(f'Legal MSG: {msg}')
        elif msg == 'q':
            websocket.send(f'Disconnect')
            break
        else:
            print(time.strftime("%X") + \
                  ' ##', 'Illegal MSG')
            await websocket.send(f'Illegal MSG: {msg}')


async def main():
    async with websockets.serve(hello, config.WS_URL, config.WS_PORT):
        await asyncio.Future()  # run forever

asyncio.run(main())