import re

import jieba
from nonebot import get_driver, logger
import pinyin

from .emoji import en_emj_map, num_emj_map, py_emj_map, zh_emj_map


@get_driver().on_startup
async def init_jieba():
    import asyncio

    await asyncio.to_thread(jieba.initialize)


def text2emoji(text: str) -> str:
    word_lst: list[str] = jieba.lcut(text)
    emoji_str = ""
    for word in word_lst:
        if bool(re.fullmatch(r"^[a-zA-Z0-9]+$", word)):
            emoji_str += en2emoji(word)
        else:
            emoji_str += zh2emoji(word)

    return emoji_str


def en2emoji(en_num: str) -> str:
    if emj := en_emj_map.get(en_num):
        logger.debug(f"[en] 英文 {en_num} -> {emj}")
        return emj

    elif emj := py_emj_map.get(en_num):
        logger.debug(f"[en] 拼音 {en_num} -> {emj}")
        return emj

    else:
        emjs = ""
        for char in en_num:
            if char.isdigit() and (emj := num_emj_map.get(char)):
                emjs += emj
                logger.debug(f"[en] 数字 {char} -> {emj}")
            else:
                emjs += char
                logger.debug(f"[en] 忽略 {char}")
        # logger.debug(f"[en] 其他 {en_num} -> {emjs}")
        return emjs


def zh2emoji(zh: str) -> str:
    if emj := zh_emj_map.get(zh):
        logger.debug(f"[zh] 中文 {zh} -> {emj}")
        return emj

    elif (zh_py := pinyin.get(zh, format="strip")) and (emj := py_emj_map.get(zh_py)):
        logger.debug(f"[zh] 拼音 {zh} -> {zh_py} -> {emj}")
        return emj

    else:
        if len(zh) == 1:
            logger.debug(f"[zh] 忽略 {zh}")
            return zh

        emjs = ""
        for char in zh:
            char_py = pinyin.get(char, format="strip")
            if emj := py_emj_map.get(char_py):
                emjs += emj
                logger.debug(f"[zh] 拼音 {char} -> {char_py} -> {emj}")
            else:
                emjs += char
                logger.debug(f"[zh] 忽略 {char}")
        # logger.debug(f"[zh] 单合 {zh} -> {emjs}")
        return emjs
