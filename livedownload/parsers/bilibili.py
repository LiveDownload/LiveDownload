import asyncio
import aiohttp
from . import BaseParse, LiveInfo


class Bilibili(BaseParse):
    API_LIVE = 'https://api.live.bilibili.com/xlive/web-room/v1/index/getRoomPlayInfo?room_id={}&play_url=1&qn={}'
    API_INFO = 'https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id={}'

    def __init__(self, room_id: int, quality: int):
        super(Bilibili, self).__init__()
        self.room_id = room_id
        self.quality = quality

    def __str__(self) -> str:
        return str(self.room_id)

    async def link(self) -> str:
        url = self.API_LIVE.format(self.room_id, self.quality)
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(url) as response:
                    live = await response.json()
                    if live['data']['play_url']:
                        return live['data']['play_url']['durl'][0]['url']
                await asyncio.sleep(30)

    async def info(self) -> LiveInfo:
        url = self.API_INFO.format(self.room_id)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                info = await response.json()
                return LiveInfo(
                    info['data']['anchor_info']['base_info']['uname'],
                    info['data']['room_info']['title'],
                    'flv'
                )

