
def args_test1(*args):

    for arg in args:
        print(arg)

def args_test2(arg, *args):

    print("Arg.. ",arg)

    print("Args..")
    for i in args:
        print(i)

def kwargs_test1(**kwargs):

    for k,v in kwargs.items():
        print("{0} --> {1}".format(k,v))

def arg_args_kwargs(arg, *args, **kwargs):

    print("Arg.. ", arg)

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
    print("Args test 1!")
    args_test1('inline 1', 'inline 2', 'inline 3')

    print("\nArgs test 2!")
    args_test1(*args)

    print("\nArgs test 3!",sep="\n")
    args_test2(*args)

    # KWARGS
    print("\nKwargs test 1!", sep="\n")
    kwargs_test1(a=1, b='c')

    print("\nKwargs test 2!", sep="\n")
    # kwargs run 2
    kwargs_test1(**kwargs)


    #Arg, args and kwargs
    print("\nArg, args and kwargs test!", sep="\n")
    arg_args_kwargs(*args, **kwargs)