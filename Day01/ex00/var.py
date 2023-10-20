def my_var():
    
    variables = [42,
                "42",
                "quarante-deux",
                42.0,
                True,
                [42],
                {"42":42},
                (42,),
                set()]

    for v in variables:
        print(v, " has a type ", type(v)) 

if __name__ == '__main__':
    my_var()