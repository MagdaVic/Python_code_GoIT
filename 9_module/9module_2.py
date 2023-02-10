DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    try:
        customer_discount = customer["discount"]
    except KeyError:
        customer_discount = DEFAULT_DISCOUNT
    return price*(1-customer_discount)
