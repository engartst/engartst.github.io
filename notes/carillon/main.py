from scamp import *

s = Session()
# requires soundfont from https://www.arrangingforcarillon.com/resources/tools/ 

playback_settings.register_named_soundfont("carillon", "/Users/hse9/Downloads/BrynMawr-carillon.sf2")
#playback_settings.register_named_soundfont("carillon", "C:/Users\engartst\Desktop\BrynMawr-carillon.sf2")
playback_settings.default_soundfont = "carillon"
carillon = s.new_part("carillon")
notes = [60, 69, 65]
durs = [1, 5, 10]
i = 0
j = 0

def scroll_move(x, y, dx, dy):
    print(x, dy)
    global j
    global i
    # some work to be done on getting the durations right on the if statement
    # below...might be + instead? but then have to deal with overflow
    if j == 6 * durs[i-1]:
        if dy > 1:
            if i < len(notes) - 1:
                carillon.play_note(notes[i], 1*dy, durs[i], blocking=False)
                i+=1
            else:
                carillon.play_note(notes[i], 1*dy, durs[i], blocking=False)
                i = 0
        j=0
    else:
        j+=1


s.register_mouse_listener(on_scroll=scroll_move, relative_coordinates=True, suppress=False)
s.wait_forever()
