from datetime import datetime, timedelta

def read_product_changes(filename, product_name):
    today = datetime.today()
    last_month = today - timedelta(days=30)

    price_changes = []

    with open(filename, 'r',encoding="UTF-8") as file:
        for line in file:
            parts = line.strip().split(', ')
            name = parts[0]
            date_str = parts[1]
            price = float(parts[2])
            if product_name.lower() in name.lower():
                date = datetime.strptime(date_str, '%Y-%m-%d')
                if date >= last_month:
                    price_changes.append((date, price))

    return price_changes

def calculate_price_change(price_changes):
    if not price_changes:
        return None

    first_price = price_changes[0][1]
    last_price = price_changes[-1][1]
    price_change = last_price - first_price

    return price_change


if __name__ == '__main__':
    filename = 'products'
    product_name = input("Введіть назву товару для перевірки цінових змін: ")

    product_changes = read_product_changes(filename, product_name)

    if product_changes:
        price_change = calculate_price_change(product_changes)
        if price_change is not None:
            print(f"Зміна ціни для товару '{product_name}' за останній місяць: {price_change:.2f}")
    else:
        print(f"Дані про зміну ціни для товару '{product_name}' за останній місяць не знайдено.")
