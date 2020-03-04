# coding=utf-8
import click
import asyncio
import multiprocessing
import time
import logging
from pathlib import Path
from multiprocessing.pool import ApplyResult
from colorlog import ColoredFormatter
from typing import Set, Type, Callable, Optional

from .parsers import BaseParse
from .parsers.bilibili import Bilibili
from .downloader import BaseDownloader
from .downloader.aiodown import AioDown


def download(downloader: Type[BaseDownloader], link: str, path: Path,
             callback: Callable[[], None]) -> ApplyResult:
    symbols = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    name = path.name
    for symbol in symbols:
        name = name.replace(symbol, '-')
    path = path.with_name(name)
    index = 2
    while path.exists():
        path = path.with_name(f"{index} - {name}")
        index += 1
    path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.info(f"文件 {path} 开始下载")
    down = downloader(link, path)
    return pool.apply_async(down.start, callback=callback)


async def add_room(room: BaseParse, downloader: Type[BaseDownloader]) -> None:
    def downloaded(filename):
        file = Path(filename)
        if not file.stat().st_size:
            file.unlink()
            logger.error(f"{filename} 文件为空，下载失败")
            return
        logger.info(f"{filename} 房间下载完成")

    logger = logging.getLogger(__name__)
    while True:
        logger.info(f"开始检测 {room} 号房间")
        link = await room.link()
        info = await room.info()
        path = Path('{}/{}/{}.{}'.format(
            info.uname,
            time.strftime("%Y/%m/%d", time.localtime()),
            info.title,
            info.suffix
        ))
        task = download(downloader, link, path, downloaded)
        while not (task.ready() and task.successful()):
            await asyncio.sleep(30)


@click.command()
@click.option('--bili', required=True, help="Bilibili Live Room ID", type=int, multiple=True)
@click.option('--quality', help="Live Quality", type=int, default=4)
def main(bili: Set[int], quality: int):
    global pool
    stream = logging.StreamHandler()
    stream.setFormatter(ColoredFormatter(
        fmt='%(purple)s%(asctime)s %(yellow)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s',
        datefmt='%H:%M:%S'
    ))
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(stream)

    pool = multiprocessing.Pool(5)
    rooms = []
    for room_id in bili:
        room = Bilibili(room_id, quality)
        rooms.append(room)

    loop = asyncio.get_event_loop()
    tasks = asyncio.gather(*[add_room(room, AioDown) for room in rooms])
    try:
        loop.run_forever()
    except KeyboardInterrupt as e:
        tasks.cancel()
    finally:
        loop.close()
        pool.terminate()


if __name__ == '__main__':
    main()
