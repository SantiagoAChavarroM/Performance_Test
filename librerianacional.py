# ----------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------Inventory control National Bookstore----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------


inventory = [
    {"title": "EL CLUB DE LAS 5 AM", "author": "ROBIN SHARMA", "category": "CRECIMIENTO PERSONAL", "price": 45000, "stock": 30, "sold": 0},
    {"title": "COMO HACER AMIGOS", "author": "DALE CARNEGIE", "category": "CRECIMIENTO PERSONAL", "price": 67000, "stock": 40, "sold": 0},
    {"title": "HARRY POTTER", "author": "J.K ROWLING", "category": "FICCIÓN", "price": 120000, "stock": 20, "sold": 0},
    {"title": "LA ODISEA", "author": "HOMERO", "category": "ÉPICO", "price": 34000, "stock": 12, "sold": 0},
    {"title": "ENOLA HOLMES", "author": "NANCY SPRINGER", "category": "NOVEL", "price": 52000, "stock": 25, "sold": 0}
]

sales_history = []


def input_int(val):
    while True:
        try:
            value = int(input(val))
            return value
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def input_float(val):
    while True:
        try:
            value = float(input(val))
            return value
        except ValueError:
            print("Entrada no válida. Ingresa un número válido.")

def search_book(title):
    return next((p for p in inventory if p["title"].lower() == title.lower()), None)


def register_book():
    print("\n--- REGISTRAR NUEVO LIBRO ---")

    title = input("Titulo del libro: ").strip()
    if search_book(title):
        print("El libro ya existe.")
        return

    author = input("Autor: ").strip()
    category = input("Categoría: ").strip()
    price = input_float("Precio unitario: ")
    if price <= 0:
        print("El precio debe ser positivo.")
        return

    stock = input_int("Cantidad en stock: ")
    if stock < 0:
        print("El stock no puede ser negativo.")
        return

    book = {
        "title": title,
        "author": author,
        "category": category,
        "price": price,
        "stock": stock,
        "sold": 0
    }

    inventory.append(book)
    print("¡Libro registrado exitosamente!")


def see_inventory():
    print("\n--- LISTADO DE INVENTARIO ---")
    if not inventory:
        print("El inventario está vacío.")
        return

    for p in inventory:
        print(f"{p['title']} | autor: {p['author']} | categoría: {p['category']} | "
              f"precio: ${p['price']} | stock: {p['stock']}")


def update_book():
    print("\n--- ACTUALIZAR LIBRO ---")
    title = input("Ingresa el titulo del libro: ")
    book = search_book(title)

    if not book:
        print("Libro no encontrado.")
        return

    print("Deja el campo en blanco para mantener el valor actual.")

    new_price = input("Nuevo precio: ")
    if new_price.strip():
        book["price"] = float(new_price)

    new_stock = input("Nuevo stock: ")
    if new_stock.strip():
        book["stock"] = int(new_stock)

    print("¡Libro actualizado!")


def delete_book():
    print("\n--- ELIMINAR LIBRO ---")
    title = input("Titulo del libro: ")
    book = search_book(title)

    if not book:
        print("¡Libro no encontrado!.")
        return

    inventory.remove(book)
    print("¡Libro eliminado!.")


def register_sale():
    print("\n--- REGISTRAR VENTA ---")
    customer = input("Nombre del cliente: ")
    type_client = input("Tipo de cliente (REGULAR / FRECUENTE): ")

    title_book = input("Libro vendido: ")
    book = search_book(title_book)

    if not book:
        print("Libro no encontrado.")
        return

    amount = input_int("Cantidad vendida: ")

    if amount > book["stock"]:
        print(f"No hay suficiente stock. Disponible: {book['stock']}")
        return

    discount = input_float("Descuento aplicado (%): ")

    book["stock"] -= amount
    book["sold"] += amount

    total_price = amount * book["price"]
    final_price = total_price - (total_price * discount / 100)

    sale = {
        "customer": customer,
        "type_client": type_client,
        "book": book["title"],
        "amount": amount,
        "discount": discount,
        "bruto": total_price,
        "neto": final_price
    }

    sales_history.append(sale)
    print("¡Venta registrada satisfactoriamente!")


def see_sales_history():
    print("\n--- HISTORIAL DE VENTAS ---")
    if not sales_history:
        print("No se han registrado ventas.")
        return

    for v in sales_history:
        print(f"{v['customer']} | {v['book']} | Cantidad: {v['amount']} | "
              f"Bruto: ${v['bruto']:.2f} | Neto: ${v['neto']:.2f}")



def top_3_report():
    print("\n--- TOP 3  LIBROS MÁS VENDIDOS ---")
    books_order = sorted(inventory, key=lambda p: p["sold"], reverse=True)
    for p in books_order[:3]:
        print(f"{p['title']} - Vendidos: {p['sold']}")


def sales_report_author():
    print("\n--- VENTAS POR AUTOR ---")

    total_sales_author = {}
    for sale in sales_history:
        book = search_book(sale["book"])
        author = book["author"]
        total_sales_author[author] = total_sales_author.get(author, 0) + sale["neto"]

    for author, total in total_sales_author.items():
        print(f"{author}: ${total:.2f}")


def income_report():
    print("\n--- REPORTE DE INGRESOS ---")
    bruto = sum(v["bruto"] for v in sales_history)
    neto = sum(v["neto"] for v in sales_history)
    print(f"Ingreso bruto: ${bruto:.2f}")
    print(f"Ingreso neto: ${neto:.2f}")


def inventory_performance_report():
    print("\n--- RENDIMIENTO DEL INVENTARIO ---")
    for p in inventory:
        percentage_sold = (p["sold"] / (p["sold"] + p["stock"])
                              if p["sold"] + p["stock"] > 0 else 0)
        print(f"{p['title']}: {percentage_sold*100:.1f}% sold")



def main_menu():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Gestionar Inventario")
        print("2. Registrar Venta")
        print("3. Ver Historial de Ventas")
        print("4. Reportes")
        print("5. Salir")
        option = input("Elige una opción: ")

        if option == "1":
            inventory_menu()
        elif option == "2":
            register_sale()
        elif option == "3":
            see_sales_history()
        elif option == "4":
            report_menu()
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


def inventory_menu():
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Registrar Libro")
        print("2. Ver Inventario")
        print("3. Actualizar Libro")
        print("4. Eliminar Libro")
        print("5. Volver")
        option = input("Elige una opción: ")

        if option == "1":
            register_book()
        elif option == "2":
            see_inventory()
        elif option == "3":
            update_book()
        elif option == "4":
            delete_book()
        elif option == "5":
            break
        else:
            print("Opción no válida.")


def report_menu():
    while True:
        print("\n--- MENÚ DE REPORTES ---")
        print("1. Top 3 de Libros Más Vendidos")
        print("2. Ventas por Autor")
        print("3. Reporte de Ingresos")
        print("4. Rendimiento del Inventario")
        print("5. Volver")

        option = input("Elige una opción: ")

        if option == "1":
            top_3_report()
        elif option == "2":
            sales_report_author()
        elif option == "3":
            income_report()
        elif option == "4":
            inventory_performance_report()
        elif option == "5":
            break
        else:
            print("Opción no válida.")


main_menu()