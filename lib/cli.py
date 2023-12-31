from colorama import Fore, Style

from helpers import (
    exit_program,
    
    list_categories,
    find_category_by_name,
    find_category_by_id,
    view_products_of_category,
    create_category,
    delete_category,
    
    list_products,
    find_product_by_name,
    find_product_by_id,
    create_product,
    delete_product
)

#User Prompt to display menu to the user and asking them to make an option
def menu():
    print(Fore.CYAN, "\n   0. Exit the program", Style.RESET_ALL)
    print(Fore.BLUE, "For Categories Table", Style.RESET_ALL)
    print(Fore.CYAN, "  1. Display all categories", Style.RESET_ALL)
    print(Fore.CYAN, "  2. Find a category by name", Style.RESET_ALL)
    print(Fore.CYAN, "  3. Find a category by ID", Style.RESET_ALL)
    print(Fore.CYAN, "  4. Create a new category to the database", Style.RESET_ALL)
    print(Fore.CYAN, "  5. Delete a category", Style.RESET_ALL)
    print(Fore.BLUE, "\nFor Products Table", Style.RESET_ALL)
    print(Fore.CYAN, "  6. Display all products", Style.RESET_ALL)
    print(Fore.CYAN, "  7. Find a product by name", Style.RESET_ALL)
    print(Fore.CYAN, "  8. Find a product by ID", Style.RESET_ALL)
    print(Fore.CYAN, "  9. View all products in a category table", Style.RESET_ALL)
    print(Fore.CYAN, "  10. Create a new product to the database", Style.RESET_ALL)
    print(Fore.CYAN, "  11. Delete a product", Style.RESET_ALL)

#A while loop to keep the user in the application until they choose to exit
def main():
    print(Fore.BLUE + Style.BRIGHT, "\n --------------------| Welcome to InventoryManagement! |--------------------", Style.RESET_ALL)
    print(Fore.MAGENTA, "You can manage categories and products by selecting a number from the menu below to get started!\n", Style.RESET_ALL)
    print(Fore.YELLOW, "To exit the program, enter '0'.", Style.RESET_ALL)

    while True:
        menu()
        print("-" * 45) # Add a separator line
        choice = input(Fore.YELLOW + "\nSelect a Prompt: " + Style.RESET_ALL)
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_categories()
        elif choice == "2":
            find_category_by_name()
        elif choice == "3":
           find_category_by_id()
        elif choice == "4":
            create_category()
        elif choice == "5":
           delete_category()
           
        elif choice == "6":
            list_products()
        elif choice == "7":
           find_product_by_name()
        elif choice == "8":
           find_product_by_id()
        elif choice == "9":
           view_products_of_category()
        elif choice == "10":
           create_product()
        elif choice == "11":
           delete_product()
        else:
           print(Fore.RED, "Invalid choice. Please choose a number between 0 and 11.", Style.RESET_ALL)

if __name__ == "__main__":
    main()



