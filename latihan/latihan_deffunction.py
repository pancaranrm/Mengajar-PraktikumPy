
kalimat = input("Maukkan kalimat")

def deteksi(kalimat):
    if 'Python' in kalimat:
        print(True)
    elif 'python' in kalimat:
        print(True)
    else:
        print(False)
    
deteksi(kalimat)


# def display(**kwargs):
#     for i in kwargs:
#         print(i)
        
# display(emp="Kelly", sallery=100)

# def display_person(*args):
#     for i in args:
#         print(i)

# display_person(name="Emma", age="25")


# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d
#     return inner_fun(a, b)

# res = outer_fun(5, 10)
# print(res)


def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)
    return a

result = outer_fun(5, 10)
print(result)
# jadi intinya si outer fun itu didefinisikan oleh inner fun
# bakal nambahin var a+b = c+d

# ngetes apa ini bakal error
	
# def my_func(*args key=None,):
#     print("hello world", args)

# my_func("abc", "abc", 123, "abc", key=123) #invalid syntax

def my_func(*args, **kwargs):
    print("hello world", args, kwargs)

my_func("abc", "abc", 123, "abc", key=123, abc=123)


# def my_func(abc=None, *args, **kwargs):
#     print("hello world", args, kwargs)

# my_func("abc", abc=123)
# got multiple value for argument abc


def my_func(abc=None, *args, **kwargs): 
    print("Hello world is",args,kwargs) # sudah diset none jadi engga bisa tuh yang namanya diganti 3>   print("hello world", args, kwargs)

my_func(122) #ga berlaku

def myrand(request, **kwargs):
    print(kwargs)
    # Product.objects.get(id=kwargs.get('id'))

# path('my-product/:id')
myrand("request", id=12345)


# def apa(param1,paramb):
#     if param1 == 'Pukis':
#         print(f"{param1} kamu sekolah dimana?")
#     elif paramb == 'Cudu':
#         print(f"{paramb} kamu sekolah dimana?")
        
# hasil = apa("Pukis","Cudu")
# print(f"hasilnya coba = {hasil}")
