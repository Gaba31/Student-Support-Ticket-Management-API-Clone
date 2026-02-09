from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    format='{time:YYYY-MM-DD HH:MM:SS} | {level} | {message}',
    level='INFO'
)

logger.add(
    "logs/app.log",
    rotation='1 MB',
    retention='7 days',
    level='INFO'

)