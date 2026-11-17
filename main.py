import asyncio

from bot_core.scripts.core.config import TOKEN
from bot_core.scripts.debug_manager import LoggerManager
from bot_core.scripts.packages import PackageManager


# Initialize logger
logger_manager = LoggerManager("discord_bot")
logger = logger_manager.get_logger()


async def run_bot():
    from bot_core.scripts.core.core import DiscordBot

    logger.info("Initializing main bot...")

    bot = DiscordBot(logger=logger)

    await bot.start(TOKEN)


if __name__ == "__main__":

    try:
        logger.info("Initializing needed components...")

        manager = PackageManager(logger=logger)
        manager.check_and_install_packages()

        logger.info("Successfully loaded all packages...")

        asyncio.run(run_bot())

    except KeyboardInterrupt:
        logger.info("Bot shutdown requested by user.")

    except Exception:
        logger.exception("Fatal application error.")

    finally:
        logger.info("Bot shutdown completed.")
        logger_manager.close()
