def generator_func():
    yield "Yield"
    yield "keyword"
    yield "in"
    yield "python"



generator_object = generator_func()
print( type(generator_object) )
for i in generator_object:
    print( i )
