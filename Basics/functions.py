# in python a function is declared wiht DEF prefix
def hello_world() :
    print("Hello World")



def cmmdc(a, b):
    if b == 0:
        return a
    else:
        return cmmdc(b, a%b)
def main():
    hello_world()
    print(cmmdc(8,4))

# with this code we use the main function()
if __name__ == "__main__":
    main()