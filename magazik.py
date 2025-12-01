products = {
	"Фрукты": [("Яблоки", 15, 60), ("Бананы", 10, 80)],
	"Овощи": [("Морковь", 8, 30)],
	"Напитки": [("Какола", 20, 90), ("Ессентуки", 10, 49)]
}

for category, items in products.items():
    print(f"{category}:")
    for item in items:
        name, quantity, price = item
        print(f"\t{name} - Цена: {price} руб., Количество: {quantity}\n")

most_expensive = max((item for sublist in products.values() for item in sublist), key=lambda x: x[2])
max_category = max(products, key=lambda k: len(products[k]))
total_sum = sum(price * count for sublist in products.values() for _, count, price in sublist)

print(f"Самый дорогой товар: {most_expensive[0]}, цена: {most_expensive[2]} руб.")
print(f"Категория с наибольшим количеством товаров: {max_category}, количество товаров: {len(products[max_category])}.")
print(f"Общая сумма всех товаров: {total_sum} руб.")

input("")