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
    print(clientIpPort +" with the message " + message)
    await websocket.send("Pong: " + message)





    

            

    


start_server = websockets.serve(receiveMsgFromWsToAnalyze, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()













import asyncio
import signal
import websockets

class Server(object):

    def __init__(self, host, port):
        self.host, self.port = host, port
        self.loop = asyncio.get_event_loop()

        self.stop = self.loop.create_future()
        self.loop.add_signal_handler(signal.SIGINT, self.stop.set_result, None)

        self.loop.run_until_complete(self.server())

    async def server(self):
        async with websockets.serve(self.ws_handler, self.host, self.port):
            await self.stop

    async def ws_handler(self, websocket, path):
        msg = await websocket.recv()
        print(f'Received: {msg}')

        await websocket.send(msg)
        print(f'Sending: {msg}')


if __name__ == '__main__':
    server = Server(host='localhost', port=6789)