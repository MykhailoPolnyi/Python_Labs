from DiscountedProduct import DiscountedProduct


def main():
    product_1 = DiscountedProduct("Sandora", "PepsiCo", starting_price=30, discount_in_percents=5, customers_rate=8,
                                  discount_duration_days=10)
    product_2 = DiscountedProduct("Shokoladka", "Svitoch", discount_in_percents=10,
                                  starting_price=30, discount_duration_days=8)
    product_3 = DiscountedProduct("Lvivske Rizdviane", starting_price=40, discount_in_percents=20,
                                  discount_duration_days=7)
    print(product_1, '\n', product_2, '\n', product_3)


if __name__ == "__main__":
    main()
