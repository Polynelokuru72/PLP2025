def read_and_modify_file(input_filename, output_filename):
    
    try:

        with open(input_filename, "r") as file:
            content = file.read()

        modified_content = content.upper()

        with open(output_filename, "w") as file:
            file.write(modified_content)

        print(f"✅ File '{input_filename}' has been modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read/write this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


def error_handling_lab():
   
    filename = input("📂 Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n📄 File Content:\n")
            print(content)

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

print("\n=== File Read & Write Challenge ===")
read_and_modify_file("input.txt", "output.txt")

print("\n=== Error Handling Lab ===")
error_handling_lab()
