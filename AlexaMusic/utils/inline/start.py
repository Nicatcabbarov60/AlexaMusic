from pyrogram.types import InlineKeyboardButton
import config
from AlexaMusic import app


def start_panel(_):
    buttons = [
        [ 
            InlineKeyboardButton(text=_["S_B_3"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_4"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_5"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ]
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ],
        [  
            InlineKeyboardButton(text=_["S_B_1"], callback_data="settings_back_helper"),
            InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_3"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_4"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["S_B_7"], user_id=config.OWNER_ID),
        ],
    ]
    return buttons
