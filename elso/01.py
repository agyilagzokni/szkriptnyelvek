#linux: #!/usr/bin/env python3

import sys

def main():
    #if True:
    #    print("hello world")
    #else:
    #    print("nem helo")
    if sys.argv[1] == "batman" or sys.argv[1] == "robin":
        print("denevér veszély")
    else:
        print("üdvözöljük " + sys.argv[1])

if __name__ == "__main__":
    main()