from collections.abc import Sequence
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
    emj_lst: list[str] = []
    for word in word_lst:
        if bool(re.fullmatch(r"^[a-zA-Z0-9]+$", word)):
            emj_lst.extend(en2emoji(word))
        else:
            emj_lst.extend(zh2emoji(word))

    return "".join(emj_lst)


def en2emoji(en_num: str) -> Sequence[str]:
    if emj := en_emj_map.get(en_num):
        logger.debug(f"[en] 英文 {en_num} -> {emj}")
        return emj

    if emj := py_emj_map.get(en_num):
        logger.debug(f"[en] 拼音 {en_num} -> {emj}")
        return emj

    emj_lst: list[str] = []
    for char in en_num:
        if char.isdigit() and (emj := num_emj_map.get(char)):
            emj_lst.append(emj)
            logger.debug(f"[en] 数字 {char} -> {emj}")
        else:
            emj_lst.append(char)
            logger.debug(f"[en] 忽略 {char}")
    # logger.debug(f"[en] 其他 {en_num} -> {emjs}")
    return emj_lst


def zh2emoji(zh: str) -> Sequence[str]:
    if emj := zh_emj_map.get(zh):
        logger.debug(f"[zh] 中文 {zh} -> {emj}")
        return emj

    if (zh_py := pinyin.get(zh, format="strip")) and (emj := py_emj_map.get(zh_py)):
        logger.debug(f"[zh] 拼音 {zh} -> {zh_py} -> {emj}")
        return emj

    if len(zh) == 1:
        logger.debug(f"[zh] 忽略 {zh}")
        return zh

    emj_lst: list[str] = []
    for char in zh:
        char_py = pinyin.get(char, format="strip")
        if emj := py_emj_map.get(char_py):
            emj_lst.append(emj)
            logger.debug(f"[zh] 拼音 {char} -> {char_py} -> {emj}")
        else:
            emj_lst.append(char)
            logger.debug(f"[zh] 忽略 {char}")
    # logger.debug(f"[zh] 单合 {zh} -> {emjs}")
    return emj_lst
