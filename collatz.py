

def collatz(num):
    try:
        terms = []
        while num != 1:
            if num % 2 == 0:
                num = num / 2
                terms.append(int(num))
            else:
                num = 3 * num + 1
                terms.append(int(num))
            print(terms)
        return terms
    except:
        print("Input is a non-intenger")

print(collatz(1000000))