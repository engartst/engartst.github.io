from mido import MidiFile
from scamp import *
from collections import namedtuple

INPUT_FILE_PATH = 'bwv665.mid'

# -------------------------------- Processing the MIDI Data ---------------------------------------

# following https://www.twilio.com/blog/working-with-midi-data-in-python-using-mido
# MIDO Documentation (a little confusing): https://mido.readthedocs.io/en/latest/index.html

mid = MidiFile(INPUT_FILE_PATH, clip=True)

# print(mid)
#
# for track in mid.tracks:
#     print(track)
#
# for message in mid.tracks[1]:
#     print(message)

Note = namedtuple("Note", "channel pitch volume start_time length")

notes_started = {}
notes = []

for track in mid.tracks:
    t = 0
    for message in track:
        t += message.time/mid.ticks_per_beat
        if message.type == "note_off" or (message.type == "note_on" and message.velocity == 0):
            volume, start_time = notes_started[(message.note, message.channel)]
            notes.append(Note(message.channel, message.note, volume, start_time, t - start_time))
        elif message.type == "note_on":
            notes_started[(message.note, message.channel)] = message.velocity / 127, t

notes.sort(key=lambda note: note.start_time)

channels, pitches, volumes, start_times, lengths = zip(*notes)
channels = list(channels)
pitches = list(pitches)
volumes = list(volumes)
start_times = list(start_times)
lengths = list(lengths)

inter_onset_times = [t2 - t1 for t1, t2 in zip(start_times[:-1], start_times[1:])]

# -------------------------------- Doing something interesting with it! ---------------------------------------

# The code below just plays back the music as-is, but what can you do with it?

s = Session()
s.fast_forward_in_beats(float("inf"))

notes = []
durs = []
vol = []

piano = s.new_part("piano")

for wait_time, pitch, length, volume in zip(inter_onset_times, pitches, lengths, volumes):
    piano.play_note(pitch, volume, length, blocking=False)
    wait(wait_time)
    notes.append(pitch)
    vol.append(volume)
    durs.append(length)


print(f'Notes: {notes}')
print(f'Vol: {vol}')
print(f'Durs: {durs}')
