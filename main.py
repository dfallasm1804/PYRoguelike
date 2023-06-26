import copy

import tcod

from engine import Engine
import entity_factories
from procgen import generate_dungeon

def main() -> None:

  # define screen size
  screen_width = 80
  screen_height = 50

  #define map size
  map_width = 80
  map_height = 45

  #max room size and amount
  room_max_size = 10
  room_min_size = 6
  max_rooms = 30

  max_monsters_per_room = 2

  #define tileset
  tileset = tcod.tileset.load_tilesheet(
    "arial10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD
  )

  player = copy.deepcopy(entity_factories.player)

  engine = Engine(player=player)

  engine.game_map = generate_dungeon(
    max_rooms=max_rooms,
    room_min_size=room_min_size,
    room_max_size=room_max_size,
    map_width=map_width,
    map_height=map_height,
    max_monsters_per_room=max_monsters_per_room,
    engine=engine,
  )
  engine.update_fov()

  
  # create screen with prev def'd values and vsync
  with tcod.context.new_terminal(
    screen_width,
    screen_height,
    tileset=tileset,
    title="Roguelike Tutorial",
    vsync=True,
  ) as context:
      # creates 'console', numpy accesses 2d arrays in Y, X order. order="F" changes it to X, Y
      root_console = tcod.console.Console(screen_width, screen_height, order="F") 

      #Game loop
      while True: 

        # put "@" symbol at coords
        engine.render(console=root_console, context=context)

        #updates screen with code has deemed to display, if this isn't here, nothing will print to screen
        engine.event_handler.handle_events()


if __name__ == "__main__":
  main()