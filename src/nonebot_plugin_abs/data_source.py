import re

import jieba
from nonebot import logger
import pinyin

from .emoji import emoji_en, emoji_num, emoji_py, emoji_zh

jieba.initialize()


def text_to_emoji(text: str) -> str:
    word_lst: list[str] = jieba.lcut(text)
    emoji_str = ""
    for word in word_lst:
        if bool(re.fullmatch(r"^[a-zA-Z0-9]+$", word)):
            emoji_str += en_to_emoji(word)
        else:
            emoji_str += zh_to_emoji(word)

    return emoji_str


def en_to_emoji(en_num: str) -> str:
    if en_num in emoji_en:
        logger.debug(f"[en] 英文 {en_num} -> {emoji_en[en_num]['char']}")
        return emoji_en[en_num]["char"]

    elif (en_py := pinyin.get(en_num, format="strip")) in emoji_py:
        logger.debug(f"[en] 拼音 {en_py} -> {emoji_py[en_py]}")
        return emoji_py[en_py]

    else:
        logger.debug(f"[en] {en_num}")
        en_in_emoji = ""
        for char in en_num:
            if char.isdigit():
                en_in_emoji += emoji_num[char]
            else:
                en_in_emoji += char
        return en_in_emoji


def zh_to_emoji(zh: str) -> str:
    if zh in emoji_zh:
        logger.debug(f"[zh] 中文 {zh} -> {emoji_zh[zh]}")
        return emoji_zh[zh]

    elif (zh_py := pinyin.get(zh, format="strip")) in emoji_py:
        logger.debug(f"[zh] 拼音 {zh_py} -> {emoji_py[zh_py]}")
        return emoji_py[zh_py]

    else:
        if len(zh) == 1:
            return zh

        zh_in_emoji = ""
        for char in zh:
            if (char_py := pinyin.get(char, format="strip")) in emoji_py:
                logger.debug(f"[zh] 拼音 {char_py} -> {emoji_py[char_py]}")
                zh_in_emoji += emoji_py[char_py]
            else:
                zh_in_emoji += char
        return zh_in_emoji


# def py_to_emoji(zh_or_py: str) -> str:
#     py = pinyin.get(zh_or_py, format="strip")
#     return emoji_py.get(py, py)


# def en_to_emoji(en: str) -> str:
#     return emoji_en.get(en, {"char": en})["char"]


# def zh_to_emoji(zh: str) -> str:
#     return emoji_zh.get(zh, zh)
