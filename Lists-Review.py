inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# step 1
inventory_len = len(inventory)

# step 2
first = inventory[0]

# step 3
last = inventory[-1]

# step 4
inventory_2_6 = inventory[2:6]

# step 5
first_3 = inventory[:3]

# step 6
twin_beds = inventory.count("twin bed")

# step 7
removed_item = inventory.pop(4)

# step 8
inventory.insert(10, "19th Century Bed Frame")

# step 9
inventory = sorted(inventory)
print(inventory)
