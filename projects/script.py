var=10

def func(x):
    global var
    print(var)
    var=10
    print(var)

func(20)