def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
   
    print(f"{kwargs.get('street')} {kwargs.get('state')}")
    print(f"{kwargs.get('city')}")

shipping_label("Dr","Spongebob","Sqaurepants","III",
               street="123 Fake St",
               apt="100"
               ,city="Detroit",
               state="MI"
               ,zip="54321")