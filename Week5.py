filename = "notes.txt"

try:
    file = open(filename, 'r')
    content = file.read()
    file.close()

    print("Hello, this is an amazing program!\n")
    print(content)

    modified_content = content.upper()

    new_file = open("modified_" + filename, 'w')
    new_file.write(modified_content)
    new_file.close()

    print("Hey, this is really amazing!")
    print(modified_content)

except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print("Error:", e)






