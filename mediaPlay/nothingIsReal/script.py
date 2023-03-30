from scamp import *

s = Session()
p = s.new_part("goblin")
s.start_transcribing()
s.fast_forward_to_beat(1000)

c_1_n = [67, 74, 71, 71, 69, 67]
c_1_d = [1, .5, .5, 1, .5, 2]
c_2_n = [67, 72, 72, 71, 69, 69, 67]
c_2_d = [.5, .5, .5, .5, .5, .5, 2]
c_3_n = [67, 74, 71, 71, 69, 69, 67, 67, 64]
c_3_d = [.5, .5, .5, .5, .5, .5, .5, .5, 3]
c_4_n = [74, 71, 69, 67, 71, 71, 72, 71, 69, 67, 65, 64, 62]
c_4_d = [1, 1, .5, 1, .5, .5, .5, 1, .5, .5, .5, .5, 2]
c_5_n = [71, 67, 67, 64, 67, 67]
c_5_d = [.5, 1, .25, .25, .5, 1]
c_6_n = [67, 64, 67, 67, 67, 71]
c_6_d = [.25, .25, .5, 1, 1.5, 1.5]
c_7_n = [67, 72, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67]
c_7_d = [.75, .25, .5, .5, .25, .25, .25, .25, .5, .5, .75, .25]
c_8_n = [71, 74, 71, 76, 71, 74, 74, 71, 76]
c_8_d = [.25, .5, .25, .5, .25, .5, .25, 2]

for notes, durs in zip(c_1_n, c_1_d):
    p.play_note(notes + 12, 1, durs)
for notes, durs in zip(c_2_n, c_2_d):
    p.play_note(notes, 1, durs)
for notes, durs in zip(c_3_n, c_3_d):
    p.play_note(notes, 1, durs)
for notes, durs in zip(c_4_n, c_4_d):
    p.play_note(notes - 12, 1, durs)
for notes, durs in zip(c_5_n, c_5_d):
    p.play_note(notes - 36, 1, durs)
for notes, durs in zip(c_6_n, c_6_d):
    p.play_note(notes - 24, 1, durs)
for notes, durs in zip(c_7_n, c_7_d):
    p.play_note(notes + 12, 1, durs)
for notes, durs in zip(c_8_n, c_8_d):
    p.play_note(notes + 24, 1, durs)

s.wait_for_children_to_finish()
performance = s.stop_transcribing()
performance.to_score().export_lilypond("test.ly")
