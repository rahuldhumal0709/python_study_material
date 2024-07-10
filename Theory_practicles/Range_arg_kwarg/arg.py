def users(*args):
    print(args)
    print(type(args))
users(10,"KL",101.5)

def myFun(**kwargs):
    print(kwargs)
    print(type(kwargs))
myFun(first='KL', last='Rahul')