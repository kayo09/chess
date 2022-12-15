class book: #moves vert + horz infinitely

    def __init__(self, location, is_alive, name, team):
            
                self.location = location
                self.is_alive = is_alive
                self.name = name
                self.team = team
    
    def travel(direction, distance): #take in direction (NSEW), as well as distance we want to go
        
        
        if direction == North:
            location = newPos
        
        elif direction == South:
            print("hewo")
            
        elif direction == West:
            print("hewo")
            
        elif direction == East:
            print("hewo")
            
        


rook1 = book( (0,0) , True, "rook1" , "black")

board = [[rook1.name,0,0],[0,0,0],[0,0,0]]

print (board)