class king:
    
    locatio
    max_move_length
    team
    is_alive

    def possible_moves():
        board_obj

    def travel():
        pass

    def where_on_board():
        pass
        

class bishop: #moves diagonally infinitely
    location
    max_move_length
    team
    is_alive
    
    def travel():
        print("hewo")

class knight: #moves in an L shape, can jump over other pieces
    location
    max_move_length
    team
    is_alive
    
    def dostuff():
        print("hewo")
        
class rook: #moves vert + horz infinitely
    location
    max_move_length
    team
    is_alive
    
    def travel(direction, distance): #take in direction (NSEW), as well as distance we want to go
        
        if direction == North:
            location = newPos
        
        elif direction == South:
            print("hewo")
            
        elif direction == West:
            print("hewo")
            
        elif direction == East:
            print("hewo")
            
        
class queen:#moves vert, horiz, diag infinitely
    location
    max_move_length
    team
    is_alive
    
    def dostuff():
        print("hewo")
        
class pawn:#moves one forward, kills diagonally 
    
    location
    max_move_length
    team
    is_alive
    is_started
    
    
    
    def dostuff():
        print("hewo")
        
board = [3][3]

board = [[rook,0,0],[0,0,0],[0,0,0]]

print = [board]