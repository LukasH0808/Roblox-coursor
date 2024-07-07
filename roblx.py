import pyautogui
import time
import keyboard  # Import keyboard module

pyautogui.FAILSAFE = False
# Function to continuously center the cursor
def center_cursor():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    pyautogui.moveTo(center_x, center_y)

# Function to toggle centering based on key press event
def toggle_centering(event):
    global centering_enabled
    if event.name == 'f':
        centering_enabled = not centering_enabled
        if centering_enabled:
            print("\nCursor centering started.")
        else:
            print("\nCursor centering stopped.")

# Main program
if __name__ == "__main__":
    centering_enabled = False  # Flag to toggle centering
    keyboard.on_press(toggle_centering)  # Register the toggle_centering function as a callback for key press events
    
    try:
        while True:
            if centering_enabled:
                center_cursor()
            
            time.sleep(0.1)  # Adjust this delay as needed to control cursor update rate
            
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        keyboard.unhook_all()  # Clean up: unregister all keyboard event hooks
