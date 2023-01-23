from scamp import *

s = Session()
# requires soundfont from https://www.arrangingforcarillon.com/resources/tools/ 

#playback_settings.register_named_soundfont("carillon", "/Users/hse9/Downloads/BrynMawr-carillon.sf2")
playback_settings.register_named_soundfont("carillon", "C:/Users\engartst\Desktop\BrynMawr-carillon.sf2")
playback_settings.default_soundfont = "carillon"
carillon = s.new_part("carillon")
notes = [60, 67, 65]
durs = [1, 2, 3]
i = 0
j = 0

def scroll_move(x, y, dx, dy):
    print(x, dy)
    global j
    # add if j == 6 * dur[i]:
    if j == 6:
        if dy >= 1:
            print("dong")
            global i
            if i < len(notes):
                print (notes[i])
                carillon.play_note(notes[i], 1*dy, durs[i], blocking=False)
                i+=1
            else:
                i = 0
                print (notes[i])
                carillon.play_note(notes[i], 1*dy, durs[i], blocking=False)
                i+=1
        j=0   
    else:
        j+=1


s.register_mouse_listener(on_scroll=scroll_move, relative_coordinates=True, suppress=False)
s.wait_forever()
