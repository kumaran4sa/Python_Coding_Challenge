try:    
    a = int(input())
    b = int(input())
    print(b/a)
    print(d)
except ZeroDivisionError as e:
    print("Zero division error..")
except Exception:
    print("Something wrong....")
