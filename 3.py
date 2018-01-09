def main():
    """
    The main function. Displays a data entry request and
    displays the result of the program
    """
    print("Welcome!/ Ласкаво просимо!")
    l =int(input("Please enter a length (n)/ Будь ласка введіть довжину (n): "))
    len_lst = l**2
    lst = [0 for i in range(len_lst)]
    count = 0

    for i in range(0, 2*(len_lst)):
        #check row and print it
        if check(lst,l) == True:
            for j in range(0, len_lst, l):
                for k in range(j, j + l):
                    print(lst[k], end="")
                print()
            print("---------")
            count +=1
        #create new row
        for m in range(len_lst - 1, -1, -1):
            if lst[m] != 1:
                lst[m] = 1
                for j in range(m + 1, len_lst):
                    lst[j] = 0
                break
    print("Ammount of transitive/Кількість транзитивних відношень = ", count)

def check(lst, n):
    """
    Checks whether the list is a transitive relation or not
    >>>check([0, 0, 1, 0, 0, 0, 0, 1, 0],3)
    True
    >>>check([0, 0, 1, 0, 0, 0, 0, 0, 0],3)
    True
    """
    for i in range(n**2):
        r = i // n
        col = i - (r * n)
        if lst[i] == 1:
            for k in range(col * n, (col * n)+n):
                a = (r - col) * n + k
                if lst[a] != 1 and lst[k] == 1 :
                    return (False)
                else:
                    return (True)
print(check([0, 0, 0, 0, 1, 1, 0, 0, 0],3))
main()
