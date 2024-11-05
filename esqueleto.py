import os
from pathlib import Path

# Ruta de acceso a la carpeta de recetas
recipes_folder = Path("Recetas")

# Función para limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para contar todas las recetas
def count_recipes():
    return sum(1 for _ in recipes_folder.glob("**/*.txt"))

# Función para mostrar las categorías
def show_categories():
    return [folder.name for folder in recipes_folder.iterdir() if folder.is_dir()]

# Función para mostrar las recetas en una categoría específica
def show_recipes_in_category(category):
    category_path = recipes_folder / category
    return [file.name for file in category_path.glob("*.txt")]

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
            category = input("Seleccione una categoría: ")
            if category in show_categories():
                recipe = input("Ingrese el nombre de la receta: ")
                print(read_recipe(category, recipe))
            else:
                print("Categoría no encontrada.")
            
        elif choice == '2':
            # Crear receta
            category = input("Seleccione una categoría: ")
            if category in show_categories():
                recipe_name = input("Ingrese el nombre de la nueva receta: ")
                content = input("Escriba el contenido de la receta: ")
                create_recipe(category, recipe_name, content)
                print("Receta creada exitosamente.")
            else:
                print("Categoría no encontrada.")
                
        elif choice == '3':
            # Crear categoría
            new_category = input("Ingrese el nombre de la nueva categoría: ")
            create_category(new_category)
            print("Categoría creada exitosamente.")
            
        elif choice == '4':
            # Eliminar receta
            category = input("Seleccione una categoría: ")
            if category in show_categories():
                recipe_name = input("Ingrese el nombre de la receta a eliminar: ")
                delete_recipe(category, recipe_name)
                print("Receta eliminada exitosamente.")
            else:
                print("Categoría no encontrada.")
                
        elif choice == '5':
            # Eliminar categoría
            category_name = input("Ingrese el nombre de la categoría a eliminar: ")
            delete_category(category_name)
            print("Categoría eliminada exitosamente.")
        
        elif choice == '6':
            # Salir
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
        
        input("Presione una tecla para volver al menú...")

# Ejecutar el menú principal
main_menu()
1