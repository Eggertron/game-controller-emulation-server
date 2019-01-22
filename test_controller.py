from flask import Flask, session, redirect, url_for, escape, request, render_template, Response, Markup, send_from_directory
import time # remove this for mutex
import json
import pyvjoy

# start up the first controller only

j = pyvjoy.VJoyDevice(1)
app = Flask(__name__)

def single_press(j, button):
  print('pressed button {0}'.format(button))
  j.set_button(button, 1)
  j.update()
  time.sleep(1)
  j.set_button(button, 0)
  j.update()

def test_axis(j):
  print('testing axis')
  j.

@app.route('/', methods=['GET', 'POST'])
def root_page():
  if request.method == 'POST':
    print('got post')
    button01 = int(request.form['button01'])
    print('button01 = {0} {1}'.format(button01, type(button01)))
    #button02 = request.form['button02']
    #print('button02 = {0}'.format(type(button02)))
    #button03 = request.form['button03']
    #print('button03 = {0}'.format(button03))
    if button01:
      single_press(j, 1)
    #if button02:
    #  single_press(j, 2)
    #if button03:
    #  single_press(j, 3)
  return render_template('debug.html')
