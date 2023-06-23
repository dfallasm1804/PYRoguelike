import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:

  # define screen size
  screen_width = 80
  screen_height = 50

  # keep track of player coords
  # py3 doesn't truncate, int casts float to int to stop error from tcod
  player_x = int (screen_width / 2)
  player_y = int (screen_height / 2)

  #define tileset
  tileset = tcod.tileset.load_tilesheet(
    "arial10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD
  )

  event_handler = EventHandler()

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

        # put "@" symbol at 1, 1 coords
        root_console.print(x=player_x, y=player_y, string="@")

        #updates screen with code has deemed to display, if this isn't here, nothing will print to screen
        context.present(root_console)

        #clears console every iteration
        root_console.clear()

        # handles key presses
        for event in tcod.event.wait():
          action = event_handler.dispatch(event)

          if action is None:
            continue

          #is action is an instance of class MovementAction, and the action can move, update coords to renderer
          if isinstance(action, MovementAction):
            player_x += action.dx
            player_y += action.dy

          # is in instance and action is Escape press, close
          elif isinstance(action, EscapeAction):
            raise SystemExit()


if __name__ == "__main__":
  main()