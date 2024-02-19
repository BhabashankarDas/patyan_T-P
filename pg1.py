def outer():
    name = "Dharani"
    def inner():
        nonlocal name
        print(name)
        name = "Gowtham"
        return name
    

    inner()
    print(name)

outer()