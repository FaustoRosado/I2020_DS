import sys

def html_output(func):
    def wrapper(args):
        with open('output.html', w) as filename:
            filename.write("<body>")
            filename.write(func(args))
            filename.write("<\body>")
           
    return wrapper

@html_output
def html_func(args):
    return args
    
if __name__ == "__main__":
    args = sys.argv[1:]
    html_func(args)
    
    