import asyncio
import websockets
import json
import math


async def hello():
    prime = 0
    even = 0
    odd = 0
    events = []
    async with websockets.connect("ws://209.126.82.146:8080") as websocket:
        while True:        
            dic = await websocket.recv()
            dic = json.loads(dic)

            # if is_prime(dic["b"]):
            #     prime += 1

            if is_even(dic["b"]):
                even += 1

            # if is_odd(dic["b"]):
            #     odd +=1

            events.append(dic)

            if len(events) == 100:
                break
        print(events)
        minimo = min(events, key=lambda k:k["b"])
        min_number = minimo["b"]
        print(minimo)
        print(min_number)

        maximo = max(events, key=lambda k:k["b"])
        max_number = maximo["b"]
        print(maximo)
        print(max_number)

        primero = events[0]
        first_number = primero["b"]
        print(primero)
        print(first_number)
            
        ultimo  = events[99]
        last_number = ultimo["b"]
        print(ultimo)
        print(last_number)

        struct = {
        "max_number": max_number,
        "min_number": min_number,
        "first_number": first_number,
        "last_number": last_number,
        # "number_of_prime_numbers": prime,
        "number_of_even_numbers": even,
        # "number_of_odd_numbers": odd,
        }
        print(struct)
        
asyncio.run(hello())

# def is_prime(dic):
#     if dic < 2:
#         return False
#     raiz = int(math.sqrt(dic)) + 1
#     for i in range(2, raiz):
#         if dic % i == 0:
#             return False
#         else:
#             return True

def is_even(n):
    if n %2 == 0:
        return True
    else:
        return False
    
# def is_odd(dic):
#     if dic %2 != 0:
#         return True
#     else:
#         return False
    

