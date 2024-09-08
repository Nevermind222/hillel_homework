"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging


def log_event(username: str, status: str):
    # statuses: success, expired, failed

    log_message = f"Login event - Username: {username}, Status: {status}"

    logging.basicConfig(
        filename='../lesson_11/login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )
    logger = logging.getLogger("log_event")

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


log_event("user", "status")
