#Victor Casado
#The Flying Mice
#SoftDev
#K14 -- Understanding code
#2024-10-8
#time spent: .5 hours

def goo():
    return "this is return string from goo() in test module"

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("this print statement came from test module")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__": #false if this file imported as module
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("this CONDITIONAL print statement came from test module")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
