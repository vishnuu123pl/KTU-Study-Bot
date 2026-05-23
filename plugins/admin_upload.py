from pyrogram import Client, filters
from config import ADMINS
from database.models import (
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
            "📄 Send PDF\n🎥 For video category, send link"
        )

    except:
        await message.reply_text(
            "Usage:\n/upload notes 2024 cse sem1 gymat101"
        )


@Client.on_message(
    filters.text &
    filters.user(ADMINS)
)
async def save_video(_, message):

    if message.from_user.id not in temp:
        return

    category, year, branch, sem, subject = temp[message.from_user.id]

    if category != "video":
        return

    try:

        await save_resource(
            category,
            year,
            branch,
            sem,
            subject,
            message.text,
            "Video Link"
        )

        await message.reply_text(
            "✅ Video Link Saved"
        )

    except Exception as e:

        print("VIDEO SAVE ERROR:", e)

        await message.reply_text(
            f"❌ DB Error:\n{e}"
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

        await delete_resource(
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

    data = await list_keys()

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

    resources = await total_resources()

    users = await get_users()

    await message.reply_text(
        f"📊 Bot Statistics\n\n"
        f"👥 Total Users: {len(users)}\n"
        f"📚 Total Resources: {resources}"
    )
