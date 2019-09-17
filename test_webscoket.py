import asyncio
import logging
from datetime import datetime
from aiowebsocket.converses import AioWebSocket

import json


async def startup(uri):
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        # 客户端给服务端发送消息

        await converse.send('{"event":"pusher:subscribe","data":{"channel":"exchange_market"}}')  # 监听所有市场
        await converse.send('{"event":"pusher:subscribe","data":{"channel":"exchange_market_bid_ask"}}')  #

        # 监听btc_usdt webscoket
        # await converse.send('{"event":"pusher:subscribe","data":{"channel":"exchange_ticker"}}')
        # await converse.send('{"event":"pusher:subscribe","data":{"channel":"exchange_eth-usdt"}}')
        # await converse.send('{"event":"pusher:subscribe","data":{"channel":"exchange_bqqq-usdt"}}')
        # await converse.send('{"event":"pusher:subscribe","data":{"auth":"5174598ab656e4da66dc:1c303fad7f188e3a9f130235ecffc1a2052da5bd9645d572b8b6020f1d154032","channel":"private-exchange==abbd73ed-2cde-416f-8ce1-3217e0472205"}}')  # 监听所有市场

        while True:
            mes = await converse.receive()
            print('{time}-Client receive: {rec}'
                  .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))
            print(type(mes))

            # 解包，获取想要的数据
            # mes = json.loads(mes.decode("utf-8"))
            # print(mes)
            # if mes["data"]["marketPriceDto"]["marketSymbol"]=="NEO-BTC":
            # print(mes["data"])
            # m1 = json.loads(mes["data"])
            # print(m1.get("message").get("marketPriceDto").get("volume"))
            # print(m1)
            # if m1.get("message")!=None:
            #     if m1["message"]["marketPriceDto"]["marketSymbol"]==market:
            #         print("{0}:市场:{1},chang24：{2}, percentageChange24：{3}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),m1["message"]["marketPriceDto"]["marketSymbol"],m1["message"]["marketPriceDto"]["change24"],m1["message"]["marketPriceDto"]["percentageChange24"]))



if __name__ == '__main__':
    # remote = 'wss://wssprod.bitsdaq.com/app/167bca97db7a84f1c98b?protocol=7&client=js&version=4.3.1&flash=false'  # 线上环境
    market = "ETH-BTC" # 配置需要监听的市场/币对
    remote ="wss://wss-dev-15.bitsdaq.io/app/d4796efce047f9e6443a?protocol=7&client=js&version=4.4.0&flash=false"   # dev环境通用
    try:
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except KeyboardInterrupt as exc:
        logging.info('Quit.')