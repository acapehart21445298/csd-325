# Arrington Capehart
# Module 1.3 Assignment
# 8/13/2026

# Counts down number of bottles

bottles = int(input("Enter number of bottles: "))

def countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles = bottles - 1
        
        print(f"Take one down and pass it around, {bottles} bottle(s) of beer on the wall.")
        print()
    
    print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
    print(f"Take one down and pass it around, 0 bottle(s) of beer on the wall.")
    print()
    
countdown(bottles)

print("Time to buy more bottles of beer.")