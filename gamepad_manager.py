import pyvjoy

class GMan(object):
  def __init__(self):
    # create empty array of gamepads
    self.gamepads = []
    self.key_map = {
      "A": 1,
      "B": 2,
      "X": 4,
      "Y": 8,
      "L": 16,
      "R": 32,
      "UP": 64,
      "DOWN": 128,
      "LEFT": 256,
      "RIGHT": 512
    }

  # Creates a new gamepad and returns the gamepad number
  def add_gamepad(self):
    gamepad_count = len(self.gamepads) + 1
    self.gamepads.append(pyvjoy.VJoyDevice(gamepad_count))
    return gamepad_count

  def press_button(self, gamepad, button):
    self._button_state(gamepad, button)
  
  def release_button(self, gamepad, button):
    self._button_state(gamepad, button)

  def _button_state(self, gamepad, button):
    j = self.gamepads[gamepad - 1]
    j.data.lButtons = button
    j.update()
