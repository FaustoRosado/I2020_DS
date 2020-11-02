import sys



user_list = input("Enter numbers to sum separated by spaces: ")
user_list = [int(num) for num in user_list.split(" ")]

def add(*args):
    total = 0
    for num in args:
        total += num
    
    print(f"The sum of the numbers in your list is {total}")






if __name__ == "__main__":     
       
        add(*user_list)
        
        

        
        
