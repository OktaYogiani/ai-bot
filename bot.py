import discord
from discord.ext import commands
from ai import check

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

SAVE_FOLDER = "saved_images"

@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")

@bot.command()
async def save_image(ctx):
    # Pastikan ada lampiran
    if not ctx.message.attachments:
        await ctx.send("Tidak ada attachment pada pesan.")
        return

    saved_files = []

    # Loop semua attachment
    for attachment in ctx.message.attachments:
        file_path = f"images/{attachment.filename}"

        # Simpan file
        await attachment.save(file_path)
        saved_files.append(attachment.filename)

        hasil=check(file_path)
        if hasil=="organik":
            await ctx.send("Ini sampah organik, ayo olah dia menjadi pupuk kompos!")
        else:
            await ctx.send("Ini sampah anorganik, ayo daur ulang menjadi barang yang lebih berguna!")


    # Pesan sukses
    await ctx.send(
        f"Berhasil menyimpan {len(saved_files)} file:\n" +
        "\n".join(f"• `{name}`" for name in saved_files)
    )

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("TOKEN")