import logging

logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)

logger = logging.getLogger(__name__)


def process_order(price, quantity):
    """Process an order and record log messages."""

    logger.debug("Starting order processing")

    try:
        if price <= 0:
            logger.error("Invalid product price")
            raise ValueError("Price must be positive")

        if quantity <= 0:
            logger.warning("Invalid product quantity")
            raise ValueError("Quantity must be positive")

        total = price * quantity

        logger.info("Order processed successfully")
        logger.info("Total order amount: %s", total)

        return total

    except ValueError as error:
        logger.error("Order failed: %s", error)
        raise


if __name__ == "__main__":
    try:
        result = process_order(500, 2)
        print("Order Total:", result)

        process_order(0, 2)

    except ValueError as error:
        print("Error:", error)
