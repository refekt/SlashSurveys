# SlashSurveys
A survey object that utilizes discord.py and discord-interactions.

# Usage
```py
from discord_surveys import Survey

async def survey(self, ctx: SlashContext, question: str, options: str):
    await Survey(
        bot=ctx.bot,
        ctx=ctx,
        question=question,
        options=options
    ).send()
```
