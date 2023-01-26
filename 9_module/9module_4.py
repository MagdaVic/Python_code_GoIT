

def discount_price(discount):
    def cost(price):
        return price*(1-discount)
    return cost
