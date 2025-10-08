import csv
import os

# CSV Files

product_file = "products.csv"
account_file = "accountinfo.csv"

# Create files if they don't exist

if not os.path.exists(account_file):
    with open(account_file, "w", newline="") as file:
        csv_writer = csv.writer(file)
       
        csv_writer.writerow(["Username", "Password"])

if not os.path.exists(product_file):
    with open(product_file, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Product Code", "Product Name", "Price", "Producer", "Recorder"])
      
# Create account
def create_account():
    
    print("\n--- Create Account ---")
    username = input("Username: ")
    password = input("Password: ")
    with open(account_file, "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([username, password])
    print("Account created successfully!\n")
  
# Login check

def login_check():
    
    print("\n--- Login ---")
    inusername = input("Username: ")
    inpassword = input("Password: ")
    with open(account_file, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        
        for row in csv_reader:
            dbusername, dbpassword = row
            if inusername == dbusername and inpassword == dbpassword:
                print("Login successful!\n")
                return dbusername
    

    print("Wrong username or password!\n")
    return None
  
# Add new product

def product_writer(recorder_username):
    
    print("\n--- Add New Product ---")
    
    
    try:
        pcode = input("Product code: ")
        pname = input("Product name: ")
        pprice = float(input("Price: ")) 
        pproducer = input("Producer: ")
    except ValueError:
        print("Invalid price entered! Please enter a number for the price.")
        return

    with open(product_file, "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([pcode, pname, pprice, pproducer, recorder_username])
    print(f"Product '{pname}' added successfully!\n")
  
# View products

def product_viewer(display_mode):
    
    print("\n--- Product List ---")
    try:
        with open(product_file, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader) # Başlığı atla

            
            product_found = False
            for row in csv_reader:
                product_found = True
                pcode, pname, price_str, producer, recorder = row
                
                
                try:
                    price = float(price_str)
                except ValueError:
                    price = 0.0 
                
                if display_mode == "simple":
                    print(f"Code: {pcode} | Name: {pname} | Price: ${price:.2f}")
                elif display_mode == "detailed":
                    print(f"Code: {pcode} | Name: {pname} | Price: ${price:.2f} | Producer: {producer} | Recorder: {recorder}")
            
            if not product_found:
                print("No products found in the inventory.")

    except FileNotFoundError:
        print("Product file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main Menu

while True:
    
    choice = input("\nSelect an option:\n1. Login\n2. Create Account\n3. View Our Products (Public)\n4. Exit\nChoice: ")
    
    if choice == "1":
        
        logged_in_user = login_check()
    
        
        if logged_in_user:
            while True:
                choice2 = input(f"\nWelcome {logged_in_user}!\n1. Add a Product\n2. View All Product Details\n3. Logout\nChoice: ")
                if choice2 == "1":
                    
                    product_writer(logged_in_user)
                elif choice2 == "2":
                    product_viewer("detailed")
                elif choice2 == "3":
                    print("Logged out.")
                    break
                else:
                    print("Invalid choice!")
    
    elif choice == "2":
        create_account()
    
    elif choice == "3":
        product_viewer("simple") 
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice! Please select a valid option.")
