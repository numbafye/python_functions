def hello(): 
    print("Greetings")

hello()

def pack(arg1, arg2, arg3):
   return [arg1, arg2, arg3]

print(pack(1, 2, 3))

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")
eat_lunch(["cake", "apple", "cookie"])
eat_lunch([])
