# requires soundfont from https://www.arrangingforcarillon.com/resources/tools/ 
from scamp import *

s = Session()

playback_settings.register_named_soundfont("carillon", "/Users/hse9/Downloads/BrynMawr-carillon.sf2")
playback_settings.default_soundfont = "carillon"
carillon = s.new_part("carillon")
notes = [59, 64, 67, 66, 64, 71, 69, 66, 64, 67, 66, 63, 65, 59]
durs = [1, 1.75, .25, 1, 2, 1, 3, 3, 1.75, .25, 1, 2, 1, 3]
i = 0

def scroll_move(x, y, dx, dy):
    if dy >= 1:
        print(len(notes))
        global i
        if i < len(notes):
            i+=1
        else:
            i=0
        carillon.play_note(notes[i], 0.5*dy, durs[i], blocking = False)
    else:
        print("wrong way")



s.register_mouse_listener(on_scroll=scroll_move, relative_coordinates=True, suppress=True)
s.wait_forever()
