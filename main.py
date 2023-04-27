import asyncio
import websockets
import time

import utils, config
from serial_io import Kyle

# WS Server
async def hello(websocket):
    # Validation
    name = await websocket.recv()
    print(time.strftime("%X") + f'{" <<":4} {name}')

    await websocket.send(f"你好 {name}!")
    print(time.strftime("%X") + f'{" >>":4} Hello {name}!')
    # Listen Message from Front-End｜
    while True:
        msg = await websocket.recv()
        if utils.isCMDLegal(msg):
            print(time.strftime("%X") + f'{" <<":4} {msg}')
            kyle.msg_list.append(msg)
            await websocket.send(f'Legal MSG: {msg}')
        elif msg == 'q':
            kyle.msg_list.append(msg)
            websocket.send(f'Disconnect')
            break
        else:
            print(time.strftime("%X") + \
                  ' ##', 'Illegal MSG')
            await websocket.send(f'Illegal MSG: {msg}')


async def main():
    async with websockets.serve(hello, config.WS_URL, config.WS_PORT):
        await asyncio.Future()  # run forever


def run_server():
    asyncio.run(main())


# Main Part
kyle = Kyle()
if kyle.start(run_server):
    kyle.waiting()
    kyle.stop()