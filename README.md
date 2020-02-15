# LiveDownload

该项目允许单推的、多推的和干活的、搞事的拉取直播间并存起来以后慢慢看。

配合播放器（如：PotPlayer）可实现边下边播

您亦可运行本程序后将其放在旁边，喝杯茶，等待 TA 的神秘上播

注：该项目拉取的直播内容从您开始运行程序开始

## 依赖

- Python >= 3.6
- Click >= 7.0
- aiohttp >= 3.6.2, < 4.0
- colorlog >= 4.1.0
- dataclasses >= 0.7



## 安装

按照以下方法安装此软件包并开始运行

```shell
pip install livedownload
```

或者下载本项目代码后，在源代码目录执行

``` shell
python setup.py install
```

## 使用

### 拉取单个直播间

在想要下载直播的目录，输入

``` shell
livedownload --bili 1
```

即可拉取 Bilibili 1 号直播间的直播流，并自动存储文件

### 拉取多个直播间

在想要下载直播的目录，输入

``` shell
livedownload --bili 1 --bili 3
```

## 作者

[U2FsdGVkX1](https://github.com/U2FsdGVkX1)

[Guoguo](https://github.com/imguoguo)