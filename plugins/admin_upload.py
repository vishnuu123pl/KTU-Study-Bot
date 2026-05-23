from pyrogram import Client, filters
from config import ADMINS
from database.db import (
    save_resource,
    delete_resource,
    list_keys,
    total_resources
)

temp = {}

@Client.on_message(
    filters.command("upload") &
    filters.user(ADMINS)
)
async def upload(_, message):

    try:
        _, category, year, branch, sem, subject = message.text.split(maxsplit=5)

        temp[message.from_user.id] = (
            category,
            year,
            branch,
            sem,
            subject
        )

        await message.reply_text(
            "📄 𝘕𝘰𝘸 𝘴𝘦𝘯𝘥 𝘗𝘋𝘍"
        )

    except:
        await message.reply_text(
            "Usage:\n/upload notes 2024 cse sem1 gymat101"
        )


@Client.on_message(
    filters.document &
    filters.user(ADMINS)
)
async def save(_, message):

    if message.from_user.id not in temp:
        return

    category, year, branch, sem, subject = temp[message.from_user.id]

    save_resource(
        category,
        year,
        branch,
        sem,
        subject,
        message.document.file_id,
        message.document.file_name
    )

    await message.reply_text(
        "✅ Saved Successfully"
    )


@Client.on_message(
    filters.command("done") &
    filters.user(ADMINS)
)
async def done(_, message):

    if message.from_user.id in temp:
        del temp[message.from_user.id]

    await message.reply_text(
        "✅ Upload Completed"
    )


@Client.on_message(
    filters.command("delete") &
    filters.user(ADMINS)
)
async def delete_file(_, message):

    try:
        _, category, year, branch, sem, subject = message.text.split(maxsplit=5)

        delete_resource(
            category,
            year,
            branch,
            sem,
            subject
        )

        await message.reply_text(
            "🗑 Deleted Successfully"
        )

    except:
        await message.reply_text(
            "Usage:\n/delete notes 2024 cse sem1 gymat101"
        )


@Client.on_message(
    filters.command("list") &
    filters.user(ADMINS)
)
async def list_files(_, message):

    data = list_keys()

    if not data:
        await message.reply_text(
            "📂 No Files Uploaded"
        )
        return

    text = "📚 Uploaded Files:\n\n"

    for row in data:

        category, year, branch, sem, subject = row

        text += (
            f"• {category}_{year}_{branch}_{sem}_{subject}\n"
        )

    await message.reply_text(text)


@Client.on_message(
    filters.command("stats") &
    filters.user(ADMINS)
)
async def stats(_, message):

    total = total_resources()

    await message.reply_text(
        f"📊 Total Resources: {total}"
    )
