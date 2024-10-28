import os
import time

SET_COLOR = "\x1b[48;5;196m"  
END = "\x1b[0m"               
CLEAR = "\033[H"              

def draw_pattern():
    """
    Draws the pattern to match the image, with two outward-facing arcs.
    """

    
    pattern = [
        "       █████████       █████████       ",
        "               ███   ███               ",
        "                 █████                 ",
         
    ]

    for line in pattern:
        for char in line:
            if char == '█':
                print(f"{SET_COLOR} {END}", end='')
            else:
                print(" ", end='')  
        print() 

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        draw_pattern()  
        time.sleep(0.5) 

if __name__ == "__main__":
    main()
