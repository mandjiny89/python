var_1 = 50

def global_var(var_1):
    print(var_1)
    def enclosed_var():
        var_1 = '100'
        print(var_1)
    enclosed_var()

global_var(var_1)
