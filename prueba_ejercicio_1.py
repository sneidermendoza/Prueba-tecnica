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
            
            events.append(dic)

            if len(events) == 100:
                break
        print(events)
       
        for n in events:
            if is_even(n["b"]):
                even +=1
                
        for n in events:
            if is_prime(n["b"]):
                prime += 1
                
        for n in events:
            if is_odd(n["b"]):
                odd +=1
                
            
    
        minimo = min(events, key=lambda k:k["b"])
        min_number = minimo["b"]

        maximo = max(events, key=lambda k:k["b"])
        max_number = maximo["b"]

        primero = events[0]
        first_number = primero["b"]
            
        ultimo  = events[99]
        last_number = ultimo["b"]

        struct = {
        "max_number": max_number,
        "min_number": min_number,
        "first_number": first_number,
        "last_number": last_number,
        "number_of_prime_numbers": prime,
        "number_of_even_numbers": even,
        "number_of_odd_numbers": odd,
        }
        
        
        print("--------------------------------------------------------------------------------------------------------------------------------")
        for s,m in struct.items():
            print(f"{s}: {m}")

def is_even(n):
    if n %2 == 0:
        return True
    else:
        return False

def is_prime(dic):
    if dic < 2:
        return False
    raiz = int(math.sqrt(dic)) + 1
    for i in range(2, raiz):
        if dic % i == 0:
            return False
        else:
            return True
        
def is_odd(dic):
    if dic %2 != 0:
        return True
    else:
        return False

asyncio.run(hello())
