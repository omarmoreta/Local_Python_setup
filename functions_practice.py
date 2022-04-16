def hello():
    print("Greeting!")
hello()

def pack(one, two, three):
    print([one, two, three])
pack("onepack", "Tupac" , "threepack")

def eat_lunch(grocery_list):
    if len(grocery_list) != 0:
        for i in range(len(grocery_list)):
            if i == 0:
                print(f"First I eat {grocery_list[0]}")
            else:
                print(f"Next I eat {grocery_list[i]}")
    else: 
        print("My lunchbox is empty!")
eat_lunch(["bread", "grapes", "samich"])