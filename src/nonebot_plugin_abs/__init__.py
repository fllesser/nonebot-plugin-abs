from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="",
    description="描述",
    usage="用法",
    type="application",  # library
    homepage="https://github.com/fllesser/nonebot-plugin-abs",
    # supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna", "nonebot_plugin_uninfo"),
    supported_adapters=None,
    extra={"author": "fllesser <fllesser@gmail.com>"},
)
from nonebot import logger, require

require("nonebot_plugin_alconna")

from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import ArgStr, CommandArg
from nonebot.typing import T_State
from nonebot_plugin_alconna.uniseg import Reply, UniMsg

# abs = on_command("abs", aliases={"抽象"}, priority=5, block=True)


# @abs.handle()
# async def _(event: Event, state: T_State, arg: Message = CommandArg()):
#     if plain_text := arg.extract_plain_text().strip():
#         state["abs"] = plain_text


# @abs.got("abs", prompt="你要抽象什么？")
# async def _(target_text: str = ArgStr("abs")):
#     abs_res = text_to_emoji(target_text)
#     await abs.send(abs_res)

abs = on_command("abs", aliases={"抽象"}, priority=5, block=True)


@abs.handle()
async def _(msg: UniMsg, state: T_State, arg: Message = CommandArg()):
    for seg in msg:
        logger.info(f"seg: {seg}")
    if msg.has(Reply):
        reply = msg[Reply, 0]
        logger.debug(f"reply: {reply}")
        reply_msg = reply.msg
        if isinstance(reply_msg, str):
            await abs.finish(text_to_emoji(reply_msg))
        else:
            await abs.finish()
    else:
        state["abs"] = arg.extract_plain_text().strip()


@abs.got("abs", prompt="你要抽象什么？")
async def _(target_text: str = ArgStr("abs")):
    abs_res = text_to_emoji(target_text)
    await abs.send(abs_res)


def text_to_emoji(text: str) -> str:
    import jieba
    from nonebot import logger
    import pinyin

    from .emoji import emoji_chinese, emoji_english, emoji_pinyin

    word_lst: list[str] = jieba.lcut(text)

    for idx, word in enumerate(word_lst):
        # logger.debug(f"word: {word}")
        if word in emoji_chinese:
            word_lst[idx] = emoji_chinese[word]
            logger.debug(f"[1] 中文 {word} ->  {emoji_chinese[word]}")
        elif word in emoji_english:
            word_lst[idx] = emoji_english[word]
            logger.debug(f"[1] 英文 {word} -> {emoji_english[word]}")
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
