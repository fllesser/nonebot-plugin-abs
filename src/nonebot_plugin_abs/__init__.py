from nonebot import logger, require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_alconna")

__plugin_meta__ = PluginMetadata(
    name="抽象",
    description="抽象",
    usage="abs 愤怒的分奴",
    type="application",  # library
    homepage="https://github.com/fllesser/nonebot-plugin-abs",
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
    extra={"author": "fllesser <fllesser@gmail.com>"},
)

from arclet.alconna import Alconna, StrMulti
from nonebot.matcher import Matcher
from nonebot_plugin_alconna import Args, Match, on_alconna
from nonebot_plugin_alconna.builtins.extensions.reply import ReplyMergeExtension

abs = on_alconna(
    Alconna("abs", Args["content", StrMulti]),
    aliases={"抽象"},
    priority=5,
    block=True,
    extensions=[ReplyMergeExtension()],
    use_cmd_start=True,
)


@abs.handle()
async def _(matcher: Matcher, content: Match[str]):
    await matcher.finish(text_to_emoji(content.result))


import jieba
import pinyin

from .emoji import emoji_cn, emoji_en, emoji_pinyin


def text_to_emoji(text: str) -> str:
    word_lst = jieba.lcut(text)
    emoji_str = ""
    for word in word_lst:
        # logger.debug(f"word: {word}")
        if word in emoji_cn:
            emoji_str += emoji_cn[word]
            logger.debug(f"[1] 中文 {word} ->  {emoji_cn[word]}")
        elif word in emoji_en:
            emoji_str += emoji_en[word]["char"]
            logger.debug(f"[1] 英文 {word} -> {emoji_en[word]['char']}")
        elif (word_pinyin := pinyin.get(word, format="strip")) in emoji_pinyin:
            emoji_str += emoji_pinyin[word_pinyin]
            logger.debug(f"[1] 拼音 {word_pinyin} -> {emoji_pinyin[word_pinyin]}")
        else:
            if len(word) == 1:
                emoji_str += word
                continue
            for char in word:
                if (char_pinyin := pinyin.get(char, format="strip")) in emoji_pinyin:
                    emoji_str += emoji_pinyin[char_pinyin]
                    logger.debug(f"[2] 拼音 {char_pinyin} -> {emoji_pinyin[char_pinyin]}")
                else:
                    emoji_str += char

    return emoji_str
