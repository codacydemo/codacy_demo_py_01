import lxml

class C20190221100206():
    "This is an example class"
    a = 10
    def func(self):
        print('Hello Example')

# Output: 10
print(C20190221100206.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(C20190221100206.func)

# Output: 'This is my second class'
print(C20190221100206.__doc__)

# Code Injection
def GET(self):
    get_input = web.input()
    param1 = get_input['param1'] if 'param1' in get_input else None
    if (param1):
        x = eval(param1)
    return "I'm vulnerable"

# CWE-759
def storePassword(userName,Password):
    hasher = hashlib.new('md5')
    hasher.update(Password)
    hashedPassword = hasher.digest()

    # UpdateUserLogin returns True on success, False otherwise
    return updateUserLogin(userName,hashedPassword)


def calc(number,times):
    program = 'a = 5\nb=10\nprint("Sum =", a+b)'
    exec(program)
    for x in range(0, 3):
        print("We're on time %d" % (x))
        y = 1
        while True:
            if(y%2 ==0):
                print("To infinity and beyond! We're getting close, on %d now!" % (y))
            y += 1
    return number*times