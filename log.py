from pynput import keyboard, mouse

# future -> find way to override on_click method, remove global variable
phrases = set()
phrase = ""

def on_click(x, y, button, pressed):
        global phrase
        global phrases
        if pressed:
            if (phrase != ""):
                phrase.strip('_') # strip shifts
                phrases.add(phrase)
                phrase = ""
            print()
            

def monitor(): 

    global phrase
    global phrases

    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

    with keyboard.Events() as events:
        for event in events:
            # want mouse click monitoring -> user selects new textbox
            if event.key == keyboard.Key.enter:
                if(phrase != ""):
                    phrase.strip('_') # strip shifts
                    phrases.add(phrase)
                    phrase = ""
            elif event.key == keyboard.Key.cmd:
                print(phrases)
            elif event.key == keyboard.Key.esc:
                break
            else:
                stringEvent = format(event)
                if(stringEvent[0:5] == 'Press'):
                    if(event.key == keyboard.Key.space):
                        phrase += " "

                    else: 
                        phrase += (format(event)[-3])

def main():
    phrases = monitor()
    print(phrases)

if __name__ == '__main__':
    main()


