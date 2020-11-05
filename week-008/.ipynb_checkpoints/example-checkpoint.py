#print(__name__)


def fn(lst):
    print(" ".join(lst[1:]))
    
if __name__ == '__main__':
    import sys
    fn(sys.argv)
    
    