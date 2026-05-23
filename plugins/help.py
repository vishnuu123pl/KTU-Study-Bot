from pyrogram import Client, filters


HELP_TEXT = """
❓ <b>𝘒𝘛𝘜 𝘚𝘵𝘶𝘥𝘺 𝘉𝘰𝘵 — 𝘏𝘦𝘭𝘱 𝘎𝘶𝘪𝘥𝘦</b>

<b>𝘏𝘰𝘸 𝘵𝘰 𝘶𝘴𝘦 𝘵𝘩𝘦 𝘣𝘰𝘵?</b>

📚 <b>𝘉𝘳𝘰𝘸𝘴𝘦 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦𝘴</b>

𝘎𝘦𝘵 𝘕𝘰𝘵𝘦𝘴 / 𝘗𝘠𝘘
→ 𝘚𝘤𝘩𝘦𝘮𝘦
→ 𝘚𝘦𝘮𝘦𝘴𝘵𝘦𝘳
→ 𝘉𝘳𝘢𝘯𝘤𝘩
→ 𝘚𝘶𝘣𝘫𝘦𝘤𝘵
→ 𝘊𝘩𝘰𝘰𝘴𝘦 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦

🔎 <b>𝘘𝘶𝘪𝘤𝘬 𝘚𝘦𝘢𝘳𝘤𝘩</b>

Examples:

search dbms
search gamat101
search java

📩 <b>𝘔𝘪𝘴𝘴𝘪𝘯𝘨 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦?</b>

Use the <b>Request Resource</b> button.

<b>𝘜𝘴𝘦𝘳 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴</b>

start - 𝘚𝘵𝘢𝘳𝘵 𝘵𝘩𝘦 𝘣𝘰𝘵 & 𝘰𝘱𝘦𝘯 𝘮𝘢𝘪𝘯 𝘮𝘦𝘯𝘶

search - 𝘚𝘦𝘢𝘳𝘤𝘩 𝘴𝘶𝘣𝘫𝘦𝘤𝘵𝘴 𝘲𝘶𝘪𝘤𝘬𝘭𝘺

help - 𝘚𝘩𝘰𝘸 𝘵𝘩𝘪𝘴 𝘩𝘦𝘭𝘱 𝘨𝘶𝘪𝘥𝘦
"""


@Client.on_message(
    filters.command("help")
)
async def help_cmd(_, message):

    await message.reply_text(
        HELP_TEXT
    )
