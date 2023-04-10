from singleton import LoggerSingleton

if __name__ == "__main__":
    obj1 = LoggerSingleton.create()
    obj2 = LoggerSingleton.create()

    print("Are they same? ", obj1 is obj2)

    #Runtime error
    #obj1 = LoggerSingleton()