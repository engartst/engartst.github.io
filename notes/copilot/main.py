#!/usr/bin/env python3

from scamp import *
import scamp_extensions

# Create a new SCAMP session
s = Session()
s.tempo = 99999

cello = s.new_part("cello")
violin = s.new_part("violin")
viola = s.new_part("viola")

s.start_transcribing()

for pitch in range(60, 72):
    cello.play_note(pitch, 0.5, 1)
    violin.play_note(pitch, 0.5, 1)
    viola.play_note(pitch, 0.5, 1)

s.stop_transcribing().to_score().show()
