import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
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

  #define tileset
  tileset = tcod.tileset.load_tilesheet(
    "arial10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD
  )

  event_handler = EventHandler()

  player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
  npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "!", (255, 255, 0))
  entities = {npc, player}

  game_map = generate_dungeon(
    max_rooms=max_rooms,
    room_min_size=room_min_size,
    room_max_size=room_max_size,
    map_width=map_width,
    map_height=map_height,
    player=player
  )

  engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
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
        events = tcod.event.wait()

        engine.handle_events(events)


if __name__ == "__main__":
  main()