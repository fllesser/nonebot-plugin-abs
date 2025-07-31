from arclet.alconna import Alconna
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

from nonebot.matcher import Matcher
from nonebot_plugin_alconna import Args, Match, on_alconna
from nonebot_plugin_alconna.builtins.extensions.reply import ReplyMergeExtension

abs = on_alconna(
    Alconna("abs", Args["content", str]),
    aliases={"抽象"},
    priority=5,
    block=True,
    extensions=[ReplyMergeExtension()],
    use_cmd_start=True,
)


@abs.handle()
async def _(matcher: Matcher, content: Match[str]):
    await matcher.finish(text_to_emoji(content.result))


def text_to_emoji(text: str) -> str:
    import jieba
    import pinyin

    from .emoji_cn import emoji_cn, emoji_pinyin
    from .emoji_en import emoji_en

    word_lst: list[str] = jieba.lcut(text)

    for idx, word in enumerate(word_lst):
        # logger.debug(f"word: {word}")
        if word in emoji_cn:
            word_lst[idx] = emoji_cn[word]
            logger.debug(f"[1] 中文 {word} ->  {emoji_cn[word]}")
        elif word in emoji_en:
            word_lst[idx] = emoji_en[word]["char"]
            logger.debug(f"[1] 英文 {word} -> {emoji_en[word]['char']}")
        elif (word_pinyin := pinyin.get(word, format="strip")) in emoji_pinyin:
            word_lst[idx] = emoji_pinyin[word_pinyin]
            logger.debug(f"[1] 拼音 {word_pinyin} -> {emoji_pinyin[word_pinyin]}")
        else:
            pass

    char_lst = list("".join(word_lst))
    for idx, char in enumerate(char_lst):
        # logger.debug(f"char: {char}")
        if (char_pinyin := pinyin.get(char, format="strip")) in emoji_pinyin:
            char_lst[idx] = emoji_pinyin[char_pinyin]
            logger.debug(f"[2] 拼音 {char_pinyin} -> {emoji_pinyin[char_pinyin]}")

    return "".join(char_lst)
