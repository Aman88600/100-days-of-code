try:
    file = open("data.txt")
except FileNotFoundError as error_message:
    print(f"{error_message}")
    print("Now Creating...")
    file = open("data.txt", "w")
    print("File Created Successfully...")
    file.write("Data")
    print("Data Written to File...")
else:
    data = file.read()
    print(data)
finally:
    file.close()