from pyrogram import Client, filters


HELP_TEXT = """
❓ <b>𝘒𝘛𝘜 𝘚𝘵𝘶𝘥𝘺 𝘉𝘰𝘵 — 𝘏𝘦𝘭𝘱 𝘎𝘶𝘪𝘥𝘦</b>

📚 <b>𝘏𝘰𝘸 𝘵𝘰 𝘶𝘴𝘦 𝘵𝘩𝘦 𝘣𝘰𝘵?</b>

𝘎𝘦𝘵 𝘕𝘰𝘵𝘦𝘴 / 𝘗𝘠𝘘
→ 𝘚𝘤𝘩𝘦𝘮𝘦
→ 𝘚𝘦𝘮𝘦𝘴𝘵𝘦𝘳
→ 𝘉𝘳𝘢𝘯𝘤𝘩
→ 𝘚𝘶𝘣𝘫𝘦𝘤𝘵
→ 𝘊𝘩𝘰𝘰𝘴𝘦 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦

🔎 <b>𝘘𝘶𝘪𝘤𝘬 𝘚𝘦𝘢𝘳𝘤𝘩</b>

/search dbms
/search gymat101
/search java

📩 <b>𝘔𝘪𝘴𝘴𝘪𝘯𝘨 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦?</b>

Use the Request Resource button.

<b>𝘜𝘴𝘦𝘳 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴</b>

/start — Start the bot & open main menu

/search — Search subjects quickly

/help — Show this help guide
"""


@Client.on_message(
    filters.command("help")
)
async def help_command(client, message):

    await message.reply_text(
        HELP_TEXT
    )
