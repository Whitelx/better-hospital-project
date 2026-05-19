from utils.json_utils import load_json, save_json


PRODUCTS_FILE = "data/products.json"
CARTS_FILE = "data/carts.json"


def store_menu(username):
    """
    قائمة المتجر.
    """

    while True:
        print("\n==============================")
        print("Store System")
        print("==============================")
        print("1. Show Products")
        print("2. Search Product")
        print("3. Add to Cart")
        print("4. Show Cart")
        print("5. Clear Cart")
        print("6. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            show_products()

        elif choice == "2":
            search_product()

        elif choice == "3":
            add_to_cart(username)

        elif choice == "4":
            show_cart(username)

        elif choice == "5":
            clear_cart(username)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


def show_products():
    """
    عرض المنتجات.
    """

    print("\n=== Products ===")

    products = load_json(PRODUCTS_FILE)

    if len(products) == 0:
        print("No products found.")
        return

    for product in products:
        print("------------------------------")
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']}")
        print(f"Stock: {product['stock']}")


def search_product():
    """
    البحث عن منتج بالاسم.
    """

    print("\n=== Search Product ===")

    search_name = input("Enter product name: ").strip().lower()

    products = load_json(PRODUCTS_FILE)

    found = False

    for product in products:
        if search_name in product["name"].lower():
            print("------------------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"Stock: {product['stock']}")

            found = True

    if found == False:
        print("No product found.")


def add_to_cart(username):
    """
    إضافة منتج لسلة المستخدم.
    """

    print("\n=== Add to Cart ===")

    products = load_json(PRODUCTS_FILE)
    carts = load_json(CARTS_FILE)

    product_id_input = input("Enter product ID: ").strip()

    if not product_id_input.isdigit():
        print("Product ID must be a number.")
        return

    product_id = int(product_id_input)

    selected_product = None

    for product in products:
        if product["id"] == product_id:
            selected_product = product
            break

    if selected_product is None:
        print("Product not found.")
        return

    if selected_product["stock"] <= 0:
        print("Product is out of stock.")
        return

    user_cart = None

    for cart in carts:
        if cart["username"] == username:
            user_cart = cart
            break

    if user_cart is None:
        user_cart = {
            "username": username,
            "items": []
        }
        carts.append(user_cart)

    cart_item = {
        "product_id": selected_product["id"],
        "name": selected_product["name"],
        "price": selected_product["price"]
    }

    user_cart["items"].append(cart_item)

    selected_product["stock"] = selected_product["stock"] - 1

    save_json(CARTS_FILE, carts)
    save_json(PRODUCTS_FILE, products)

    print("Product added to cart.")


def show_cart(username):
    """
    عرض سلة المستخدم الحالي.
    """

    print("\n=== Your Cart ===")

    carts = load_json(CARTS_FILE)

    user_cart = None

    for cart in carts:
        if cart["username"] == username:
            user_cart = cart
            break

    if user_cart is None or len(user_cart["items"]) == 0:
        print("Your cart is empty.")
        return

    total = 0

    for item in user_cart["items"]:
        print("------------------------------")
        print(f"Product ID: {item['product_id']}")
        print(f"Name: {item['name']}")
        print(f"Price: {item['price']}")

        total = total + item["price"]

    print("------------------------------")
    print(f"Total: {total}")


def clear_cart(username):
    """
    تفريغ سلة المستخدم.
    """

    carts = load_json(CARTS_FILE)

    for cart in carts:
        if cart["username"] == username:
            cart["items"] = []
            save_json(CARTS_FILE, carts)
            print("Cart cleared.")
            return

    print("Your cart is already empty.")