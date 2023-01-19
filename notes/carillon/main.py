from scamp import *

s = Session()
s.tempo = 120

# requires soundfont from https://www.arrangingforcarillon.com/resources/tools/ 

playback_settings.register_named_soundfont("carillon", "/Users/hse9/Downloads/BrynMawr-carillon.sf2")
playback_settings.default_soundfont = "carillon"
carillon = s.new_part("carillon")
notes = [59, 64, 67, 66, 64, 71, 69, 66, 64, 67, 66, 63, 65, 59]
durs = [1, 1.75, .25, 1, 2, 1, 3, 3, 1.75, .25, 1, 2, 1, 3]

def scroll_move(x, y, dx, dy):
    print(x, dy)
    if dy >= 1:
        carillon.play_note(60*dy, 0.5*dy, 1)
    else:
        print("no")



#for n, d in zip(notes, durs): carillon.play_note(n, d, 1)
s.register_mouse_listener(on_scroll=scroll_move, relative_coordinates=True, suppress=True)
s.wait_forever()
