import logging
from discord.ext import commands
from discord import app_commands, Interaction

logger = logging.getLogger("command.general")


class CommandGroup(commands.Cog):
    @app_commands.command(name="deployup", description="Deploy Application Whatever")
    async def ping(self, interaction: Interaction) -> None:
        ...




async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CommandGroup(bot))
    logger.info("CommandGroup cog loaded successfully.")
