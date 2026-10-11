import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def display_help():
    print("\nAvailable Commands:")
    print(" help                -Show available commands")
    print(" clear               -Clear the terminal screen")
    print(" exit                -Shut down MiniOS")
    
    #Under File Management
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    
    #Under Process Management
    print("")
    print("")
    print("")
    print("")
    
    #Under Memory Management
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

def exit_os():
    print("\nMiniOSMTB is shutting down... \nBye, I'll miss you")
    sys.exit(0)
    
#Brain of our code, means your logic is supposed to be inserted under defmain() 
def main():
    clear_screen()
    print("========================================================================================================================")
    print("                                                       MINIOS MTB                                                                                            ")
    print("========================================================================================================================")
    print("\nWelcome to MiniOSMTB!\n")
    
    while True:
        try:
            user_input = input("MiniOSMTB>").strip()
            if not user_input:
                continue
            
            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:]
        
            if command == "exit":
                exit_os()
            elif command == "help":
                display_help()
            elif command == "clear":
                clear_screen()
        
        
        
        
        
            else:
                print(f"\nUnknown command: '{command}'.")
                print("Type 'help' to see the available commands\n")
        
        except KeyboardInterrupt:
            exit_os()   

if __name__ == "__main__":
    main()