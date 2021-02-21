class DiscountedProduct:
    __discounted_products_counter = 0

    def __init__(self, /, product_name="", producer="not specified", *, starting_price=0,
                 discount_in_percents=0, discount_duration_days=0, customers_rate="unknown"):
        self.name = product_name
        self.producer = producer
        self.starting_price = starting_price
        self.discount_in_percents = discount_in_percents
        if self.starting_price != 0:
            self.price_with_discount = starting_price * (1 - discount_in_percents / 100)
        self.discount_duration_days = discount_duration_days
        self.customers_rate = customers_rate
        DiscountedProduct.__discounted_products_counter += 1

    def __str__(self):
        return f"Product name: {self.name}\n\
Discount: {self.discount_in_percents}%\n\
Starting Price: {self.starting_price} \n\
Price with discount: {self.price_with_discount}\n\
Producer: {self.producer} \n\
Duration of discount: {self.discount_duration_days} days\n\
Customers rate of this product: {self.customers_rate}\n"

    def __del__(self):
        del self
        DiscountedProduct.__discounted_products_counter -= 1
        print(f"Object Deleted\n\
Objects left: {DiscountedProduct.__discounted_products_counter}")

    @staticmethod
    def get_disc_product_counter():
        return DiscountedProduct.__discounted_products_counter
