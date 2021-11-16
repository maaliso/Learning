order= input()
state= "stand by"
while order != "quit":
    if order == "open":
      if state == "open":
       print ("Car is already", state)
       order = input()
      else:
          state = "open"
          print ("Car is now", state)
          order = input()
    elif order == "start":
        state = "started"
        print("Engine is now", state)
        order = input()
    elif order =="help":
        print ("""Type 'start' to start the car
Type 'quit' to exit the game
Type 'help' to get help""""")
        order = input()
    else:
        break
print ("Game is now exited")