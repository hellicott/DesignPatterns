from builder.sandwich import Sandwich


def create_blt():
    blt = Sandwich.SandwichBuilder("wholemeal")\
        .add_filling("bacon")\
        .add_filling("lettuce")\
        .add_filling("tomato")\
        .with_butter()\
        .build()
    print(blt)


def create_my_sandwich():
    my_sandwich = Sandwich.SandwichBuilder("brown baguette")\
        .add_filling("sausages")\
        .build()
    print(my_sandwich)


create_blt()
create_my_sandwich()
