import asyncio
import websockets
import json
from helper import *

async def tom():
    prime = 0
    even = 0
    odd = 0
    events = []
    async with websockets.connect("ws://209.126.82.146:8080") as websocket:
        while True:        
            dic = json.loads(await websocket.recv())
            
            if is_even(dic["b"]):
                even +=1
            
            if is_prime(dic["b"]):
                prime += 1

            if is_odd(dic["b"]):
                odd +=1
            
            events.append(dic)

            if len(events) == 100:
                break
        
        
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
        
        print(events)
        print("x" * 150)
        for s,m in struct.items():
            print(f"{key}: {value}")



asyncio.run(tom())