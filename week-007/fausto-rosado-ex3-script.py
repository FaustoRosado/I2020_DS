import sys

def html_output(func):
    def wrapper(args):
        out = open('output.html', 'w') 
        out.write("<body>")
        out.write("\n")
        out.write(func(args)
        out.write("</body>")
        #out.close()
    return wrapper

@html_output
def html_func(args):
    return args
    
if __name__ == "__main__":
    args = sys.argv[1:]
    html_func(args)
    
    