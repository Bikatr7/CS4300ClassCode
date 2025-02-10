def calculate_discount(price, discount_percent):
    """Calculate final price after discount using duck typing"""
    return price - (price * (discount_percent / 100)) 

## calculates the final price after a discount is applied
## uses duck typing to ensure the price and discount_percent are numbers
## uses formula from homework 1 pdf