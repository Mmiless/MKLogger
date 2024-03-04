from pynput import keyboard

def monitor(): 

    phrases = set()
    phrase = ""

    with keyboard.Events() as events:
        for event in events:
            # want mouse click monitoring -> user selects new textbox
            if event.key == keyboard.Key.enter:
                if(phrase != ""):
                    phrase.strip('_') # strip shifts
                    phrases.add(phrase)
                    phrase = ""
            elif event.key == keyboard.Key.esc:
                print(phrases)
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


