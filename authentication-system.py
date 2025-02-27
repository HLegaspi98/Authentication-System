# Basic Authentication System 
user_credentials = {}

# Function to register the user
def register_user():
  
  username = input("Enter your username: ")

  # Check to see if the username already exists
  if username in user_credentials:
    print("Username already exists. Please choose a different username.")
  else: 
    password = input("Enter a password: ")
    # Create the key-value pair for the username and password
    user_credentials[username] = password
  print("Registration successful!")

# Function to login an existing user
def login_user():
  username = input("Enter your username: ")
  password = input("Enter your password: ")

  # Check the username and password matches
  if username in user_credentials and user_credentials[username] == password:
    print("Login successful! Welcome back!")
  else: 
    print("Invalid username or password. Please try again. ")

# Function to run the authentication system
def authentication_system():
  while True:
    # Prompt the user to either register, login, or exit.
    print("Welcome to the Basic Authentication System!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
  
    option = input("Enter your choice (1/2/3): ")
  
    if option == "1":
      # Call the register_user function
      register_user()
    elif option == "2":
      # Call the login_user function
      login_user()
    elif option == "3":
      print("Exiting the program. Goodbye!")
      # End the program.
      break
    else: 
      print("Invalid option. Please choose from options 1, 2, or 3.")

# Run the basic authentication system program 
authentication_system()