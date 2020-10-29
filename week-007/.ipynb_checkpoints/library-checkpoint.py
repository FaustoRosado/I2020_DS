def hello_world():
    print("hello")
    
def func(arg):
    return 100 * arg

# if call python file directly, setting name attr to be value name, have an effect with larger 
# standard to use in scripts, like global attr, calling file or calling script, called __main__
# internally, name set to main when directly running the file, use the statement whenever file  # is directly called, this part not executed when importing into the jupyter notebook

if __name__ == "__main__":     
        #print(__name__)
        #print(func(100))
        #hello_world()
        #print(func(100))
        
       
        import sys
        print(sys.argv)
        
# thats how you get 
        
#hello_world() -> would interfere with execution, trying to make a script like in the terminal