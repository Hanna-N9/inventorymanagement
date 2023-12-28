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

def menu():
#User Prompt to display menu to the user and asking them to make an option
    #print('\n' + '-' * 45 + '\n')
    
    print(Fore.BLUE, "Welcome to our interactive program!", Style.RESET_ALL)
    print("You can manage categories and products by selecting a number from the menu.\n")
    print("To exit the program, enter '0'.")
    
    print(Fore.BLUE, "\nFor Categories Table", Style.RESET_ALL)
    print(Fore.CYAN, "  1. Display all categories", Style.RESET_ALL)
    print(Fore.CYAN, "  2. Find a category by name", Style.RESET_ALL)
    print(Fore.CYAN, "  3. Find a category by ID", Style.RESET_ALL)
    print(Fore.CYAN, "  4. View all products in a category table", Style.RESET_ALL)
    print(Fore.CYAN, "  5. Create a new category to the database", Style.RESET_ALL)
    print(Fore.CYAN, "  6. Delete a category", Style.RESET_ALL)
    print(Fore.BLUE, "\nFor Products Table", Style.RESET_ALL)
    print(Fore.CYAN, "  7. Display all products", Style.RESET_ALL)
    print(Fore.CYAN, "  8. Find a product by name", Style.RESET_ALL)
    print(Fore.CYAN, "  9. Find a product by ID", Style.RESET_ALL)
    print(Fore.CYAN, "  10. Create a new product to the database", Style.RESET_ALL)
    print(Fore.CYAN, "  11. Delete a product", Style.RESET_ALL)

def main():
#A while loop to keep the user in the application until they choose to exit
    #print('\n' + '-' * 45 + '\n')
    while True:
        menu()
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
           view_products_of_category()
        elif choice == "5":
           create_category()
        elif choice == "6":
           delete_category()
           
        elif choice == "7":
            list_products()
        elif choice == "8":
           find_product_by_name()
        elif choice == "9":
           find_product_by_id()
        elif choice == "10":
           create_product()
        elif choice == "11":
           delete_product()
        else:
           print(Fore.RED, "Invalid choice. Please choose a number between 0 and 11.", Style.RESET_ALL)

if __name__ == "__main__":
    main()

