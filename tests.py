from data import data

# list of dictionaries
products = data



def test1():
    print("Print each product title")

    for prod in products:
        title = prod["title"]
        print(title)


def test2():
    print("Print the Sum of all prices")

    sum = 0
    for prod in products:
        price = prod["price"]
        sum += price
    
    print(f"The Sum is: {sum}")

def test3():
    print("Print the title of the products with the price greater than 11")

    for prod in products:
        title = prod["title"]
        price = prod["price"]
        if price > 11 :
            print(title)

def test4():
    print("Print the total stock value ( price * stock)")

    sum = 0
    for prod in products:
        val = prod["price"] * prod["stock"]
        sum += val

    print(f"The value fo the stock is: {sum}")

def test5():
    print("** unique categories")

    unique_categories = []
    for prod in products:
        cat = prod["category"]

        #how to check if an element exists inside a list in python
        if cat not in unique_categories:
            unique_categories.append(cat)
            print(cat)

def run_tests():
    print("Starting tests")

    #test1()
    #test2()
    #test3()
    #test4()
    test5()



run_tests()



# test 4
# print the total stock value ( price * stock)