# break and continue statement
# Break: it terminates the flow from the inner loop
# Continue:It skips all the conditions written after it in that loop and reaches back to the starting of that loop in which continue is written
i = 7
if i > 0:
    while i > 6:
        if i % 7 == 0:
            print(i)
        while i == 7:
            print("hurray")
            print("inner loop")
            i = i - 1
        print("inside for loop")
        continue
        print(i)  # is never executed
        i -= 1
        print(i)
    print("outside every loop")
