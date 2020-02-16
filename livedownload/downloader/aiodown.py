import asyncio
import aiohttp
import logging
from . import BaseDownloader


class AioDown(BaseDownloader):
    HEADERS = {'User-Agent': 'Chrome/80.0 (Windows NT 10.0; Win64; x64)'}

    async def download(self) -> str:
        logger = logging.getLogger(__name__)
        try:
            file = open(self.path, 'wb')
            async with aiohttp.ClientSession(headers=self.HEADERS, timeout=aiohttp.ClientTimeout()) as session:
                async with session.get(self.link) as response:
                    while True:
                        data = await response.content.read(1024**2)
                        if not data:
                            break
                        file.write(data)

            file.close()
        except Exception as e:
            logger.error(e)
        return self.path

    def start(self) -> str:
        loop = asyncio.new_event_loop()
        result = loop.run_until_complete(self.download())
        loop.close()
        return result
