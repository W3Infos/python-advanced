def mydecorator(function):

    def wrapper():
        function()
        print('I am decorating your function')
        return wrapper

    @mydecorator
    def hello_world():
        print('Hello World')
    #mydecorator(hello_world)() 
    hello_world()