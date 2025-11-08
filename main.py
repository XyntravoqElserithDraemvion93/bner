import os
import sys
import asyncio
import requests
import nextcord
from nextcord.ext import commands
from asyncio_throttle.throttler import Throttler
from datetime import datetime, timedelta, timezone
from collections import deque, defaultdict
import re


# トークンを環境変数から取得
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
if not BOT_TOKEN:
    print("エラー: トークン入ってないよぉ")
    sys.exit(1)


# ===============================
# 基本設定
# ===============================
AUTO_ROLE_ID = 1429379213814796399
GUILD_ID = 1427160712475836508       
CHANNEL_ID = 1434245647762067497     
VERIFY_ROLE_ID = 1429379212489523340 

# ===============================
# スパム検出設定
# ===============================
SPAM_LIMIT = 4
TIME_WINDOW = 20
TIMEOUT_SPAM = timedelta(days=1)
TIMEOUT_LINK = timedelta(hours=1)
DELETE_DELAY = 5
TARGET_CHANNEL_ID = 1434216894373560471


intents = nextcord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

msg_history = defaultdict(lambda: deque(maxlen=30))
url_pattern = re.compile(r"(https?://[^\s]+)")


# ===============================
# ヘルパー関数
# ===============================
async def send_temp_message(channel, content):
    try:
        msg = await channel.send(content)
        await asyncio.sleep(DELETE_DELAY)
        await msg.delete()
    except Exception as e:
        print(f"一時メッセージ送信エラー: {e}")


def is_admin_or_owner(member: nextcord.Member):
    if not member or not member.guild:
        return False
    return member.guild_permissions.administrator or member == member.guild.owner


# ===============================
# イベントハンドラー
# ===============================
@bot.event
async def on_ready():
    print(f"Botログインせいこー: {bot.user}")
    await bot.change_presence(
        activity=nextcord.Game(name="/Vexelのbotを使お！"),
        status=nextcord.Status.online
    )
    print("スラッシュこまんどかんりょーう！")


@bot.event
async def on_member_join(member: nextcord.Member):
    role = member.guild.get_role(AUTO_ROLE_ID)
    if role:
        try:
            await member.add_roles(role, reason="自動ロール付与")
            print(f"{member.name} にロール {role.name} を付与しました")
        except nextcord.Forbidden:
            print(f"{member.name} へのロール付与失敗: 権限不足")
        except nextcord.HTTPException as e:
            print(f"{member.name} へのロール付与失敗: {e}")
    else:
        print(f"ロールID {AUTO_ROLE_ID} が見つかりません")

    try:
        message = (
            f"### {member.name} さん、/Vexelにようこそ!\n"
            "ようこそ/Vexelサーバーへ!\n\n"
            "**サーバーのルール**\n"
            "1️他のサーバにここを宣伝すること！\n"
            "2️他のサーバーで/Vexelのbotを使うこと！\n"
            "3️/Vexelが作ったサイトを開くこと！便利なサイトがあるから使ってみてね！\n\n"
            "楽しんでいってね！"
        )
        await member.send(message)
        print(f"{member.name} にDM送信完了")
    except nextcord.Forbidden:
        print(f"{member.name} にDMを送れません（DM拒否設定）")
    except nextcord.HTTPException as e:
        print(f"{member.name} へのDM送信失敗: {e}")


@bot.event
async def on_message(message: nextcord.Message):
    # DMは処理しない
    if not message.guild:
        return
    
    user = message.author
    
    # ===============================
    # スパム対策（TARGET_CHANNEL_ID）
    # ===============================
    if message.channel.id == TARGET_CHANNEL_ID:
        # Bot/Webhookのメッセージはスパム対策しない
        if message.author.bot or message.webhook_id:
            await bot.process_commands(message)
            return
            
        print(f"[スパム検出チャンネル] {user.name}: {message.content[:50]}")
        
        # 管理者チェック
        if is_admin_or_owner(user):
            print(f"  → 管理者なのでスキップ")
            await bot.process_commands(message)
            return
        
        now = datetime.now().timestamp()
        dq = msg_history[user.id]
        dq.append((now, message))
        
        # 古いメッセージを削除
        while dq and now - dq[0][0] > TIME_WINDOW:
            dq.popleft()
        
        print(f"  → 過去{TIME_WINDOW}秒のメッセージ数: {len(dq)}")
        
        # スパム検出
        if len(dq) >= SPAM_LIMIT:
            until = datetime.now(timezone.utc) + TIMEOUT_SPAM
            try:
                await user.timeout(until, reason="スパム検出")
                print(f"  → タイムアウト実行: {user.name}")
                
                # 最近のメッセージを削除
                messages_to_delete = list(dq)[-10:]
                for _, msg in reversed(messages_to_delete):
                    try:
                        await msg.delete()
                    except Exception as e:
                        print(f"    メッセージ削除失敗: {e}")
                
                dq.clear()
                
                await send_temp_message(
                    message.channel,
                    f"{user.mention} がスパムしたと思うからタイムアウトする！"
                )
                return
            except nextcord.Forbidden:
                print(f"  → タイムアウト失敗: 権限不足")
            except Exception as e:
                print(f"  → タイムアウト失敗: {e}")
        
        # リンクスパム検出
        links = url_pattern.findall(message.content)
        if len(links) >= 3:
            print(f"  → リンク数: {len(links)} - リンクスパム検出")
            until = datetime.now(timezone.utc) + TIMEOUT_LINK
            try:
                await message.delete()
                await user.timeout(until, reason="リンクスパム")
                print(f"  → リンクスパムタイムアウト実行: {user.name}")
                
                # 最近のメッセージを削除
                messages_to_delete = list(dq)[-10:]
                for _, msg in reversed(messages_to_delete):
                    try:
                        await msg.delete()
                    except Exception as e:
                        print(f"    メッセージ削除失敗: {e}")
                
                await send_temp_message(
                    message.channel,
                    f"{user.mention} がリンクをいっぱい書いたからタイムアウトー！"
                )
                dq.clear()
                return
            except nextcord.Forbidden:
                print(f"  → リンクスパムタイムアウト失敗: 権限不足")
            except Exception as e:
                print(f"  → リンクスパムタイムアウト失敗: {e}")
    
    # ===============================
    # 認証チャンネル処理（CHANNEL_ID）
    # ===============================
    if message.channel.id == CHANNEL_ID:
        print(f"[認証チャンネル] メッセージ検出: {message.content[:100]}")
        
        guild = bot.get_guild(GUILD_ID)
        if not guild:
            print("  → ギルドが見つかりません")
            await bot.process_commands(message)
            return
        
        role = guild.get_role(VERIFY_ROLE_ID)
        if not role:
            print(f"  → ロールID {VERIFY_ROLE_ID} が見つかりません")
            await bot.process_commands(message)
            return
        

        
        target_member = None
        content = message.content
        
        # パターンマッチング
        # "- ユーザー名#0" or "- ユーザー名" の形式を検出
        dash_match = re.search(r'-\s*(.+?)(?:#\d+)?
    
    await bot.process_commands(message)


# ===============================
# スラッシュコマンド
# ===============================
@bot.slash_command(name="verify", description="リンク紹介！")
async def verify(
    interaction: nextcord.Interaction,
    title: str = nextcord.SlashOption(description="リンクのタイトル"),
    description: str = nextcord.SlashOption(description="リンク招待の文明をぉ決めろ"),
    button_label: str = nextcord.SlashOption(description="ボタンの絵文字はなんだ？"),
    link: str = nextcord.SlashOption(description="実行のリンクをよこせ！"),
    image_url: str = nextcord.SlashOption(description="画像張りたいならどーぞ", required=False)
):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("君には権限がぁない！", ephemeral=True)
        return

    try:
        embed = nextcord.Embed(
            title=title,
            description=description,
            color=nextcord.Color.red()
        )

        if image_url:
            embed.set_image(url=image_url)

        view = nextcord.ui.View()
        view.add_item(nextcord.ui.Button(label=button_label, url=link))

        await interaction.response.defer(ephemeral=True)
        await asyncio.sleep(0.3)
        await interaction.channel.send(embed=embed, view=view)
        await interaction.followup.send("送信かんりょーう！", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"エラーが出たよ。: {e}", ephemeral=True)


# ===============================
# プレフィックスコマンド
# ===============================
@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    """いらないメッセージ削除削除！！！"""
    if amount <= 0:
        return
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"{len(deleted)} 件のメッセージを削除しました。！", delete_after=3)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("君には権限がぁない！", delete_after=3)


# ===============================
# 実行
# ===============================
if __name__ == "__main__":
    try:
        print("=== Discord Bot 起動中 ===")
        token = os.getenv("DISCORD_TOKEN")
        if not token:
            print("❌ トークンが見つかりません")
            sys.exit(1)
        bot.run(token)
    except Exception as e:
        print(f"❌ エラー発生: {e}")
    finally:
        print("🔄 Bot終了: GitHub Actionsが再起動を担当します")
        sys.stdout.flush()
        sys.exit(0)
, content)
        if dash_match:
            username = dash_match.group(1).strip()
            print(f"  → 「-」の後からユーザー名検出: '{username}'")
            
            # ギルド内のメンバーと照合
            for member in guild.members:
                member_name_lower = member.name.lower()
                member_display_lower = member.display_name.lower()
                username_lower = username.lower()
                
                # 完全一致または部分一致
                if (username_lower == member_name_lower or 
                    username_lower == member_display_lower or
                    username_lower in member_name_lower or
                    username_lower in member_display_lower or
                    member_name_lower in username_lower or
                    member_display_lower in username_lower):
                    target_member = member
                    print(f"  → メンバー発見: {member.name} (表示名: {member.display_name})")
                    break
        
        # パターン1で見つからなかった場合、メッセージ全体から検索
        if not target_member:
            print("  → パターンマッチ失敗、全文検索開始")
            # 特殊文字を除去してクリーンなテキストに
            clean_content = re.sub(r"[^\w\sぁ-んァ-ヶー一-龠々]", " ", content).lower().strip()
            print(f"  → クリーン化テキスト: '{clean_content}'")
            
            # 全メンバーと照合
            for member in guild.members:
                member_name_lower = member.name.lower()
                member_display_lower = member.display_name.lower()
                
                # メンバー名がメッセージ内に含まれているか
                if (member_name_lower in clean_content or 
                    member_display_lower in clean_content):
                    target_member = member
                    print(f"  → メンバー発見（全文検索）: {member.name} (表示名: {member.display_name})")
                    break
        
        # メンバーが見つかった場合、ロールを付与
        if target_member:
            try:
                if role not in target_member.roles:
                    await target_member.add_roles(role, reason="認証完了")
                    print(f"  ✅ ロール付与成功: {target_member.name}")
                    
                    # 成功メッセージを送信（オプション）
                    try:
                        await message.channel.send(
                            f"✅ {target_member.mention} に認証ロールを付与しました！",
                            delete_after=5
                        )
                    except:
                        pass
                else:
                    print(f"  → {target_member.name} は既にロールを持っています")
            except nextcord.Forbidden:
                print(f"  ❌ ロール付与失敗: 権限不足")
            except Exception as e:
                print(f"  ❌ ロール付与エラー: {e}")
        else:
            print(f"  ❌ メッセージからユーザーを特定できませんでした: '{content}'")
    
    await bot.process_commands(message)


# ===============================
# スラッシュコマンド
# ===============================
@bot.slash_command(name="verify", description="リンク紹介！")
async def verify(
    interaction: nextcord.Interaction,
    title: str = nextcord.SlashOption(description="リンクのタイトル"),
    description: str = nextcord.SlashOption(description="リンク招待の文明をぉ決めろ"),
    button_label: str = nextcord.SlashOption(description="ボタンの絵文字はなんだ？"),
    link: str = nextcord.SlashOption(description="実行のリンクをよこせ！"),
    image_url: str = nextcord.SlashOption(description="画像張りたいならどーぞ", required=False)
):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("君には権限がぁない！", ephemeral=True)
        return

    try:
        embed = nextcord.Embed(
            title=title,
            description=description,
            color=nextcord.Color.red()
        )

        if image_url:
            embed.set_image(url=image_url)

        view = nextcord.ui.View()
        view.add_item(nextcord.ui.Button(label=button_label, url=link))

        await interaction.response.defer(ephemeral=True)
        await asyncio.sleep(0.3)
        await interaction.channel.send(embed=embed, view=view)
        await interaction.followup.send("送信かんりょーう！", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"エラーが出たよ。: {e}", ephemeral=True)


# ===============================
# プレフィックスコマンド
# ===============================
@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    """いらないメッセージ削除削除！！！"""
    if amount <= 0:
        return
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"{len(deleted)} 件のメッセージを削除しました。！", delete_after=3)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("君には権限がぁない！", delete_after=3)


# ===============================
# 実行
# ===============================
if __name__ == "__main__":
    try:
        print("=== Discord Bot 起動中 ===")
        token = os.getenv("DISCORD_TOKEN")
        if not token:
            print("❌ トークンが見つかりません")
            sys.exit(1)
        bot.run(token)
    except Exception as e:
        print(f"❌ エラー発生: {e}")
    finally:
        print("🔄 Bot終了: GitHub Actionsが再起動を担当します")
        sys.stdout.flush()
        sys.exit(0)
