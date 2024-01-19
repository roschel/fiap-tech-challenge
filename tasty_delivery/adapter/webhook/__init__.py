from discordwebhook import Discord


def send_webhook(msg):
    discord = Discord(
        url="https://discord.com/api/webhooks/1197697614121009193/SVdkwy3TndRDmY_xnBjr6_QLYiiJ-gps99ANPYzZ9T8Mj65HlmUBEAmAbmKhrorXwnYv")
    discord.post(content=msg)
