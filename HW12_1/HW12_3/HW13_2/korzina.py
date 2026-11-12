
class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name} - {self.price} грн, {self.description}, Розміри: {self.dimensions}"


class Customer:
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}, Телефон: {self.phone}"


class Order:
    def __init__(self, customer, address):
        self.customer = customer
        self.address = address
        self.products = {}

    def add_product(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Кількість товару має бути додатною")
        self.products[product] = self.products.get(product, 0) + quantity

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.products.items())

    def __str__(self):
        result = f"Замовлення\nПокупець: {self.customer}\nАдреса: {self.address}\nТовари:\n"

        for product, quantity in self.products.items():
            result += f"{product.name} - {quantity} шт. x {product.price} грн = {product.price * quantity} грн\n"

        result += f"Загальна вартість: {self.total_price()} грн"
        return result


product1 = Product("Ноутбук", 25000, "Ігровий ноутбук", "35x25x2 см")
product2 = Product("Мишка", 800, "Бездротова мишка", "12x6x4 см")
product3 = Product("Клавіатура", 1500, "Механічна клавіатура", "45x15x4 см")

customer1 = Customer("Іваненко", "Іван", "Іванович", "+380991234567")
customer2 = Customer("Петренко", "Олег", "Петрович", "+380671234567")

order1 = Order(customer1, "м. Київ, вул. Шевченка, 10")
order1.add_product(product1, 1)
order1.add_product(product2, 2)

order2 = Order(customer2, "м. Запоріжжя, вул. Центральна, 5")
order2.add_product(product3, 2)
order2.add_product(product2, 1)

print("Товари:")
print(product1)
print(product2)
print(product3)

print("\nПокупці:")
print(customer1)
print(customer2)

print("\nЗамовлення:")
print(order1)
print()
print(order2)
