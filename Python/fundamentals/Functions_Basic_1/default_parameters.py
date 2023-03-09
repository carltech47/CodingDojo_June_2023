def be_cheerful(name='', repeat=2):
    print(f"Good Morning {name}\n " * repeat)
    return name

be_cheerful("Torrey")
be_cheerful()
be_cheerful("Missy")
be_cheerful("Nilla")
be_cheerful(repeat=10)
be_cheerful(name="Lil Bro", repeat=3)
be_cheerful(repeat=4, name="test")