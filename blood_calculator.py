def interface():
    print("Blood calculator")
    keep_running = True 
    while keep_running:
        print("Options:")
        prtint("9 - Quit")
        choice = input("Select an option:")
        if choice == "9":
            keep_running == False
    print("Program ending")


interface()