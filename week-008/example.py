def fn(lst):
    
    with open("", "w") as filename:
        print(" ".join(lst[1:]))
    
if __name__ == '__main__':
    import sys
    fn(sys.argv)
    
    