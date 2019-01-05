
def args_test1(*args):
    for arg in args:
        print(arg)

def args_test2(arg, *args):

    print("Arg: ",arg)

    print("\nArgs..",sep="\n")
    for i in args:
        print(i)

def kwargs_test1(**kwargs):
    for k,v in kwargs.items():
        print("{0} --> {1}".format(k,v))

def arg_args_kwargs(arg, *args, **kwargs):
    print("\nArg, args and kwargs examples..",sep="\n")
    print("Arg..", arg)

    print("Args..")
    for i in args:
        print(i)

    print("Kwargs..")
    for k,v in kwargs.items():
        print("{0} --> {1}".format(k,v))

if __name__ == "__main__":

    kwargs = {"country": "USA", "state": "Texas", "city": "Dallas"}

    args = ('first','second','third')

    #AGRS
    args_test1('a','b','c')

    args_test2('a','b','c')

    args_test1(*args)

    # KWARGS
    #kwargs run 1
    kwargs_test1(a=1, b='c')

    print("\n")
    # kwargs run 2
    kwargs_test1(**kwargs)


    #Arg, args and kwargs
    arg_args_kwargs(*args, **kwargs)