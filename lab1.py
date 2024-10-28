def draw_inverted_v():
   

    
    width = 5
    height = 3

    
    rows = []

    
    top_row = " " * (width // 2 - 1) + "*" + " " * (width // 2 - 1)
    rows.append(top_row)

   
    middle_row = " " * (width // 2 - 1) + "*" + " " * (width // 2 - 1)
    rows.append(middle_row)

   
    bottom_row = " " * (width // 2 - 2) + "***" + " " * (width // 2 - 2)
    rows.append(bottom_row)

    
    for row in rows:
        print(row)


draw_inverted_v()
