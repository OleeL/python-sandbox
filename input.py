
try:
    myInput = input("Enter something: ")
    print('hello')
except KeyboardInterrupt:
    print("Gracefully exiting...")
    exit(0)
    

print("You entered:", myInput)
