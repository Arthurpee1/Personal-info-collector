Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Simple Console-Based Program for Storing and Displaying Personal Details
... 
... def collect_user_details():
...     # Prompt the user for personal details
...     print("Please enter your personal details below:")
...     
...     name = input("Name: ")
...     age = int(input("Age: "))
...     email = input("Email: ")
...     phone = input("Phone Number: ")
...     address = input("Address: ")
...     
...     # Store the details in a dictionary
...     user_details = {
...         "Name": name,
...         "Age": age,
...         "Email": email,
...         "Phone": phone,
...         "Address": address
...     }
...     return user_details
... 
... def display_user_details(user_details):
...     # Display the user details in a formatted way
...     print("\n--- User Details ---")
...     for key, value in user_details.items():
...         print(f"{key}: {value}")
... 
... def main():
...     user_details = collect_user_details()
...     display_user_details(user_details)
... 
... if __name__ == "__main__":
