import random

from pyrogram.types import InlineKeyboardButton

selections = [
    "▁▄▂▇▄▅▄▅▃",
    "▁▃▇▂▅▇▄▅▃",
    "▃▁▇▂▅▃▄▃▅",
    "▃▄▂▄▇▅▃▅▁",
    "▁▃▄▂▇▃▄▅▃",
    "▃▁▄▂▅▃▇▃▅",
    "▁▇▄▂▅▄▅▃▄",
    "▁▃▅▇▂▅▄▃▇",
    "▃▅▂▅▇▁▄▃▁",
    "▇▅▂▅▃▄▃▁▃",
    "▃▇▂▅▁▅▄▃▁",
    "▅▄▇▂▅▂▄▇▁",
    "▃▅▂▅▃▇▄▅▃",
]


def stream_markup_timer(_, videoid, chat_id, played, dur):
    bar = random.choice(selections)
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text=_["PL_B_3"], switch_inline_query_current_chat=""
            ),
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    bar = random.choice(selections)
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_3"], switch_inline_query_current_chat=""
            ),
        ],
    ]
    return buttons


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="❮𝙊𝙒𝙉𝙀𝙍❯", url=f"https://t.me/anjali_m_pRoJeCt"),
            InlineKeyboardButton(text="❮𝙂𝙍𝙊𝙐𝙋❯", url=f"https://t.me/+VfYbz3mFdD9iNjVh"),
        ], 
    ]
    return buttons

def stream_markup(_, videoid):
    buttons = [
        [
            InlineKeyboardButton(text="❮𝙊𝙒𝙉𝙀𝙍❯", url=f"https://t.me/anjali_m_pRoJeCt"),
            InlineKeyboardButton(text="❮𝙂𝙍𝙊𝙐𝙋❯", url=f"https://t.me/+VfYbz3mFdD9iNjVh"),
        ], 
    ]
    return buttons


def telegram_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text="❮𝙊𝙒𝙉𝙀𝙍❯", url=f"https://t.me/anjali_m_pRoJeCt"),
            InlineKeyboardButton(text="❮𝙂𝙍𝙊𝙐𝙋❯", url=f"https://t.me/+VfYbz3mFdD9iNjVh"),
        ], 
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="❮𝙊𝙒𝙉𝙀𝙍❯", url=f"https://t.me/anjali_m_pRoJeCt"),
            InlineKeyboardButton(text="❮𝙂𝙍𝙊𝙐𝙋❯", url=f"https://t.me/+VfYbz3mFdD9iNjVh"),
        ], 
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="❮𝙊𝙒𝙉𝙀𝙍❯", url=f"https://t.me/anjali_m_pRoJeCt"),
            InlineKeyboardButton(text="❮𝙂𝙍𝙊𝙐𝙋❯", url=f"https://t.me/+VfYbz3mFdD9iNjVh"),
        ], 
    ]
    return buttons


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
