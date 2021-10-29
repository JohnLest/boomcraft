# Importing the relevant libraries
import websockets
import asyncio

PORT = 7890



print("Server listening on Port " + str(PORT))

async def echo(websocket, path):
    print("A client just connected")
    try:
        async for message in websocket:
            
            
            

            print("Received message from client: " + message)
            
            await websocket.send("Pong: " + message)



    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
        print(websocket.remote_address)


async def receiveMsgFromWsToAnalyze(websocket, path):
    print("A client just connected")
    try:
        async for message in websocket:
            
           await analyzeMsg(websocket, message)

    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
        print(websocket.remote_address)


async def analyzeMsg(websocket, message):
    counter = 0   
    address = "127.0.0.2"
    port =  "8092" 
    clientIpPort =  address+":"+port 
    for item in websocket.remote_address:
        if(counter == 0) : 
            address = str(item)
            print("Client IP address -->" + address)
            counter+=1

        elif(counter == 1) :
            port = str(item)
            print("PORT -->" + str(item))
    clientIpPort = address+":"+port 
    print(clientIpPort +"with the message " + message)
    await websocket.send("Pong: " + message)





    

            

    


start_server = websockets.serve(receiveMsgFromWsToAnalyze, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()