#decorator = a function that extends the behavior of another fucntion
# w/o modifying the base fucntion 
# pass the base function as an argument to the decorator




def add_sprinkles(func):
    def wrapper(*args , **kwargs):
        print("*You add sprinkle*")
        func(*args , **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args , **kwargs):
        print("*You add fudge*")
        func(*args , **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your ice cream {flavour} ")
    
    
get_ice_cream("Vanilla")