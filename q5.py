x= int(input("Enter a number of repetitions: "))


# Write your decorator here
def repeat(x):
    def repeat_func(func):
          def wrapper(* args,** kwargs):
                for i in range(x):
                      func()
          return wrapper
    return repeat_func
                    

@repeat(x)
def hello():
       print ('Hello')


hello()
