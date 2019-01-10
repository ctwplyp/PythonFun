def print_args(**args):
    for arg in args:
        print(arg)

print_args(red ="red",blue ="blue",green ="greem")

def normal_function(a,b,c):
        print("a: {} b:{} c:{}".format(a,b,c))

numbers = (7,5,3)

normal_function(*numbers)

itemGroup =[1,2]
def max_by_abs(items):
    biggest =items[0]
    for item in items[1:]:
        if abs(items)> abs(biggest):
            biggest = item
    return biggest

max_by_abs(itemGroup)


