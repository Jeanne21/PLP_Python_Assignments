def modify_file():
    try:
        # Ask user for input file name
        input_file = input("Enter the name of the file to read: ")
        output_file = input("Enter the name of the new file to write modified content: ")

        # Open and read the input file
        with open(input_file, "r") as infile:
            content = infile.read()

        # Example modification: make text uppercase
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"\n✅ Modified content written to '{output_file}' successfully!")

    except FileNotFoundError:
        print("⚠️ Error: The file you entered does not exist.")
    except PermissionError:
        print("⚠️ Error: You don’t have permission to read or write this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


def read_file_with_handling():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, "r") as file:
            print("\n📂 File contents:")
            print(file.read())

    except FileNotFoundError:
        print("⚠️ Error: The file does not exist.")
    except PermissionError:
        print("⚠️ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# ---------------- MAIN PROGRAM ----------------
print("📌 File Handling & Exception Handling Program")
print("1. Read a file")
print("2. Modify a file and write to a new file")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    read_file_with_handling()
elif choice == "2":
    modify_file()
else:
    print("⚠️ Invalid choice. Please enter 1 or 2.")
