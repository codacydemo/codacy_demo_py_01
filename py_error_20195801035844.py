#import lxml

class C20195801035844():
    "This is an example class"
    a = 10
    @classmethod
    def func(self):
        print('Hello Example')
    @classmethod
    def calc(self,number,times):
        print("Sum =", number+times)
        #no need for exec
        for x in range(0, 3):
            print("We're on time %d" % (x))
            y = 1
            while True:
                if(y%2 ==0):
                    print("To infinity and beyond! We're getting close, on %d now!" % (y))
                y += 1
                if(y%10 == 0):
                    break
        return number*times

# Output: 10
print(C20195801035844.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(C20195801035844.func)

# Output: 'This is my second class'
print(C20195801035844.__doc__)

# Code Injection
def GET(self):
    get_input = web.input()
    param1 = get_input['param1'] if 'param1' in get_input else None
    if (param1):
        x = ast.literal_eval(param1)
    return "I'm not vulnerable"+x

# CWE-759
def storePassword(userName,Password):
    hasher = hashlib.new('md5')
    hasher.update(Password)
    hashedPassword = hasher.digest()

    # UpdateUserLogin returns True on success, False otherwise
    return updateUserLogin(userName,hashedPassword)
