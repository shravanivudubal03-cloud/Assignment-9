def calculate_discount(price, discount_percent):
    """Calculate discount amount."""

    if not isinstance(price, (int, float)) or isinstance(price, bool):
        raise TypeError("Price must be a number")

    if price < 0:
        raise ValueError("Price cannot be negative")

    if not isinstance(discount_percent, (int, float)) or isinstance(
        discount_percent, bool
    ):
        raise TypeError("Discount must be a number")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount percentage")

    return price * discount_percent / 100


def calculate_gst(amount, gst_rate=18):
    """Calculate GST amount."""

    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise TypeError("Amount must be a number")

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if not isinstance(gst_rate, (int, float)) or isinstance(gst_rate, bool):
        raise TypeError("GST rate must be a number")

    if gst_rate < 0:
        raise ValueError("GST rate cannot be negative")

    return amount * gst_rate / 100


def calculate_order_total(price, quantity, discount_percent=0, gst_rate=18):
    """Calculate final order total after discount and GST."""

    if not isinstance(quantity, int) or isinstance(quantity, bool):
        raise TypeError("Quantity must be an integer")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    total = price * quantity
    discount = calculate_discount(total, discount_percent)
    discounted_price = total - discount
    gst = calculate_gst(discounted_price, gst_rate)

    return discounted_price + gst


if __name__ == "__main__":
    try:
        result = calculate_order_total(1000, 2, 10)
        print("Final Order Total:", result)

    except (ValueError, TypeError) as error:
        print("Error:", error)
