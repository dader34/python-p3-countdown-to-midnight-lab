import time
def countdown(f):
    for i in range(f,0,-1):
        print(f'{i} SECOND(S)!')

    print("HAPPY NEW YEAR!")

def countdown_with_sleep(f):
    for i in range(f,0,-1):
        print(f'{i} SECOND(S)!')
        time.sleep(1)
    print("HAPPY NEW YEAR!")