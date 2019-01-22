from flask import Flask, session, redirect, url_for, escape, request, render_template, Response, Markup, send_from_directory
import time # remove this for mutex
import json
from gamepad_manager import GMan

# start up the first controller only

manager = GMan()
gamepad = manager.add_gamepad()

app = Flask(__name__)

def test_button(button):
  print("== test {0} ==")
  manager.press_button(gamepad, button)
  time.sleep(1)
  manager.release_button(gamepad, 0)

@app.route('/', methods=['GET', 'POST'])
def root_page():
  if request.method == 'POST':
    if 'button01' in request.form:
      button01 = int(request.form['button01'])
      print('button01 = {0} {1}'.format(button01, type(button01)))
      test_button(manager.key_map['RIGHT'])
    if 'button02' in request.form:
      button02 = request.form['button02']
      print('button02 = {0} {1}'.format(button02, type(button02)))
      test_button(manager.key_map['DOWN'])
    if 'button03' in request.form:
      button03 = int(request.form['button03'])
      print('button03 = {0} {1}'.format(button03, type(button03)))
      test_button(manager.key_map['X'])
    #if button03:
    #  single_press(j, 3)
  return render_template('debug.html')
