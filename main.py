import rpg
"""Initialises game and runs main loop """
game_room = rpg.current_room
command_handler = rpg.CommandHandler(game_room, rpg.backpack)
while game_room is not None:
    print("\n")
    game_room.get_details()
    if game_room.get_name() == 'The Street':
        print('end of game')
        break
    command = input("> ")   
    game_room = command_handler.handle(command)
    
    
