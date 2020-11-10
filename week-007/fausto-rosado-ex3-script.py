import sys

def html_func(args):
   
    with open('output.html', 'w') as filename:
        filename.write(f"<body>\n")
        for arg in args:
            filename.write(arg)
            filename.write(" ")
        filename.write(f"\n<\body>")
           
    #return args

    
if __name__ == "__main__":
    args = sys.argv[1:]
    html_func(args)
    
    
    