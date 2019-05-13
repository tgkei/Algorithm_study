def dec(og_func):
        def ret():
                print("1")
                return og_func()
        return ret

@dec
def bb():
        print("2")

bb()