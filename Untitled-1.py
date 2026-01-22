import time

def countdown_timer():
    try:
        # Get input from the user
        seconds = int(input("Enter time in seconds: "))
        
        print(f"\nStarting timer for {seconds} seconds...")
        
        # Loop until seconds reaches 0
        while seconds > 0:
            print(f"Time remaining: {seconds}s", end="\r")
            time.sleep(1) # Wait for 1 second
            seconds -= 1
            
        print("Time's up! 🚀")
        
    except ValueError:
        print("Please enter a valid whole number.")

if __name__ == "__main__":
    countdown_timer()