import os
from pathlib import Path

# Ruta de acceso a la carpeta de recetas
recipes_folder = Path("Recetas")  # Cambia esta ruta según tu sistema

# Función para limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para contar todas las recetas
def count_recipes():
    return sum(1 for _ in recipes_folder.glob("**/*.txt"))

# Función para mostrar las categorías con números
def show_categories():
    categories = [folder.name for folder in recipes_folder.iterdir() if folder.is_dir()]
    if categories:
        print("\nCategorías disponibles:")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")
    else:
        print("\nNo hay categorías disponibles.")
    return categories

# Función para mostrar las recetas en una categoría específica con números
def show_recipes_in_category(category):
    category_path = recipes_folder / category
    recipes = [file.name for file in category_path.glob("*.txt")]
    if recipes:
        print("\nRecetas disponibles:")
        for i, recipe in enumerate(recipes, start=1):
            print(f"{i}. {recipe}")
    else:
        print("\nNo hay recetas en esta categoría.")
    return recipes

# Función para leer el contenido de una receta
def read_recipe(category, recipe_name):
    recipe_path = recipes_folder / category / recipe_name
    with open(recipe_path, 'r') as file:
        return file.read()

# Función para crear una nueva receta
def create_recipe(category, recipe_name, content):
    category_path = recipes_folder / category
    recipe_path = category_path / f"{recipe_name}.txt"
    with open(recipe_path, 'w') as file:
        file.write(content)

# Función para crear una nueva categoría
def create_category(category_name):
    category_path = recipes_folder / category_name
    category_path.mkdir(exist_ok=True)

# Función para eliminar una receta
def delete_recipe(category, recipe_name):
    recipe_path = recipes_folder / category / recipe_name
    recipe_path.unlink()

# Función para eliminar una categoría
def delete_category(category_name):
    category_path = recipes_folder / category_name
    for file in category_path.glob("*.txt"):
        file.unlink()
    category_path.rmdir()

# Función principal del menú
def main_menu():
    while True:
        clear_screen()
        print("¡Bienvenido al gestor de recetas!")
        print(f"Ruta de recetas: {recipes_folder}")
        print(f"Cantidad de recetas disponibles: {count_recipes()}")
        
        print("\nSeleccione una opción:")
        print("1. Leer una receta")
        print("2. Crear una receta")
        print("3. Crear una categoría")
        print("4. Eliminar una receta")
        print("5. Eliminar una categoría")
        print("6. Salir")
        
        choice = input("Ingrese su elección: ")
        
        if choice == '1':
            # Leer receta
            categories = show_categories()
            category_index = int(input("\nSeleccione una categoría por número: ")) - 1
            if 0 <= category_index < len(categories):
                selected_category = categories[category_index]
                recipes = show_recipes_in_category(selected_category)
                recipe_index = int(input("Seleccione una receta por número: ")) - 1
                if 0 <= recipe_index < len(recipes):
                    selected_recipe = recipes[recipe_index]
                    print("\nContenido de la receta:")
                    print(read_recipe(selected_category, selected_recipe))
                else:
                    print("Número de receta no válido.")
            else:
                print("Número de categoría no válido.")
            
        elif choice == '2':
            # Crear receta
            categories = show_categories()
            category_index = int(input("\nSeleccione una categoría por número: ")) - 1
            if 0 <= category_index < len(categories):
                selected_category = categories[category_index]
                recipe_name = input("Ingrese el nombre de la nueva receta: ")
                content = input("Escriba el contenido de la receta: ")
                create_recipe(selected_category, recipe_name, content)
                print("Receta creada exitosamente.")
            else:
                print("Número de categoría no válido.")
                
        elif choice == '3':
            # Crear categoría
            new_category = input("Ingrese el nombre de la nueva categoría: ")
            create_category(new_category)
            print("Categoría creada exitosamente.")
            
        elif choice == '4':
            # Eliminar receta
            categories = show_categories()
            category_index = int(input("\nSeleccione una categoría por número: ")) - 1
            if 0 <= category_index < len(categories):
                selected_category = categories[category_index]
                recipes = show_recipes_in_category(selected_category)
                recipe_index = int(input("Seleccione una receta por número para eliminar: ")) - 1
                if 0 <= recipe_index < len(recipes):
                    selected_recipe = recipes[recipe_index]
                    delete_recipe(selected_category, selected_recipe)
                    print("Receta eliminada exitosamente.")
                else:
                    print("Número de receta no válido.")
            else:
                print("Número de categoría no válido.")
                
        elif choice == '5':
            # Eliminar categoría
            categories = show_categories()
            category_index = int(input("\nSeleccione una categoría por número para eliminar: ")) - 1
            if 0 <= category_index < len(categories):
                selected_category = categories[category_index]
                delete_category(selected_category)
                print("Categoría eliminada exitosamente.")
            else:
                print("Número de categoría no válido.")
        
        elif choice == '6':
            # Salir
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
        
        input("\nPresione una tecla para volver al menú...")

# Ejecutar el menú principal
main_menu()
