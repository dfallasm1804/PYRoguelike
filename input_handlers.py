from typing import Optional #denotes something that could be set to None

#importing event to use tcod's event system
import tcod.event

from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):

  #method to quit program 
  def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
    raise SystemExit()

    # takes an action, returns Action subclass or None if no valid key pressed
  def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:

      action: Optional[Action] = None

      key = event.sym

      if key == tcod.event.KeySym.UP:
        action = MovementAction(dx=0, dy=-1)
      elif key == tcod.event.K_DOWN:
        action = MovementAction(dx=0, dy=1)
      elif key == tcod.event.K_LEFT:
        action = MovementAction(dx=-1, dy=0)
      elif key == tcod.event.K_RIGHT:
        action = MovementAction(dx=1, dy=0)

      elif key == tcod.event.K_ESCAPE:
        action = EscapeAction()

      return action

