
def html_output(func):
    def wrapper(*args):
        
        output = open("outfile.txt", "w") 

        output.write("<body>")
        outfile.write("\n")
        outfile.write(func(args "$@"))
        outfile.write("</body>")
        outfile.close()
    return wrapper

@html_output
def html_func(args):
    return args
    
if __name__ == "__main__":
    args = sys.argv[1:]
    html_func(args)
    
    