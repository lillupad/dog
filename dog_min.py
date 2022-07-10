import sys, os
if(len(sys.argv)<2):
    while True:print(input())
else:
    try: 
        f=open(os.path.join(os.getcwd(),sys.argv[1]),'r').read()
        print(f)
    except FileNotFoundError:
        print('dog: %s: No such file or directory'%sys.argv[1])
    except IsADirectoryError:
        print('dog: %s: Is a directory'%sys.argv[1])