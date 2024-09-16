# file_handling_assignment.py

# File creation and writing
try:
    # Create and open the file in write mode ('w')
    with open("my_file.txt", "w") as file:
        file.write("Hello, I am awesome.\n")
        file.write("Tonight we are having s party.\n")
        file.write("I have 600 shillings.\n")
    print("File 'my_file.txt' created and written successfully.")

    # Reading the file and displaying the contents
    with open("my_file.txt", "r") as file:
        print("\nReading 'my_file.txt' contents:")
        content = file.read()
        print(content)

    # Appending more content to the file
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line 1.\n")
        file.write("My mother is 68 years old.\n")
        file.write("Cows give us milk.\n")
    print("New content appended to 'my_file.txt'.")

    # Reading the file again to display the updated content
    with open("my_file.txt", "r") as file:
        print("\nUpdated 'my_file.txt' contents after appending:")
        updated_content = file.read()
        print(updated_content)

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile handling operation completed.")