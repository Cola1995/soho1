import asyncio
import logging
from datetime import datetime
from aiowebsocket.converses import AioWebSocket


async def startup(uri):
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        # 客户端给服务端发送消息

        await converse.send('{"H":"c2","M":"SubscribeToSummaryLiteDeltas","A":[],"I":0}')  # 监听所有市场
        await converse.send('{"H":"c2","M":"SubscribeToExchangeDeltas","A":["BTC-MANA"],"I":1}')  #
        await converse.send('{"H":"c2","M":"QueryExchangeState","A":["BTC-MANA"],"I":2}')


        while True:
            mes = await converse.receive()
            print('{time}-Client receive: {rec}'
                  .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))


if __name__ == '__main__':
    remote = 'wss://socket.bittrex.com/signalr/connect?transport=webSockets&clientProtocol=1.5&connectionToken=kRQKZJ65rW1MLfZZBD2GTuqxuB0%2FYdUl8WuzniPfRcDgd%2FRR5ZImcFdmQfGYbMLKyV4atzKVzjqDFb8bGjOqCorxScBOQT%2B1q2ihOAF4gNGIpq0Z&connectionData=%5B%7B%22name%22%3A%22c2%22%7D%5D&tid=8'
    try:
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except KeyboardInterrupt as exc:
        logging.info('Quit.')