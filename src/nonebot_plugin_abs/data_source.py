import re

import jieba
from nonebot import get_driver, logger
import pinyin

from .emoji import emoji_en, emoji_num, emoji_py, emoji_zh


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
    if (item := emoji_en.get(en_num)) and (emj := item.get("char")):
        logger.debug(f"[en] 英文 {en_num} -> {emj}")
        return emj

    elif emj := emoji_py.get(en_num):
        logger.debug(f"[en] 拼音 {en_num} -> {emj}")
        return emj

    else:
        en_in_emoji = ""
        for char in en_num:
            if char.isdigit():
                en_in_emoji += emoji_num[char]
            else:
                en_in_emoji += char
        logger.debug(f"[en] {en_num} -> {en_in_emoji}")
        return en_in_emoji


def zh2emoji(zh: str) -> str:
    if emj := emoji_zh.get(zh):
        logger.debug(f"[zh] 中文 {zh} -> {emj}")
        return emj

    elif (zh_py := pinyin.get(zh, format="strip")) and (emj := emoji_py.get(zh_py)):
        logger.debug(f"[zh] 拼音 {zh_py} -> {emj}")
        return emj

    else:
        if len(zh) == 1:
            return zh

        zh_in_emoji = ""
        for char in zh:
            char_py = pinyin.get(char, format="strip")
            if emj := emoji_py.get(char_py):
                logger.debug(f"[zh] 拼音 {char_py} -> {emj}")
                zh_in_emoji += emj
            else:
                zh_in_emoji += char
        logger.debug(f"[zh] {zh} -> {zh_in_emoji}")
        return zh_in_emoji


# def py_to_emoji(zh_or_py: str) -> str:
#     py = pinyin.get(zh_or_py, format="strip")
#     return emoji_py.get(py, py)


# def en_to_emoji(en: str) -> str:
#     return emoji_en.get(en, {"char": en})["char"]


# def zh_to_emoji(zh: str) -> str:
#     return emoji_zh.get(zh, zh)
