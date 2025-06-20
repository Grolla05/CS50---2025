#n = input("input: ")
#if n.isnumeric():
#    print("Interger.")
#else:
#    print("Not Interger")


try:
    n = int(input("Input: "))
    print("Integer")

except ValueError:
    print("Not integer")
