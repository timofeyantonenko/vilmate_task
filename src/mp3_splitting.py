from pydub import AudioSegment


song = AudioSegment.from_mp3("/home/timofey/projects/vilmate_task/speech_engine/src/output/Joe Rogan Experience 1169 - Elon Musk.mp3")

part_name = 0
for i in range(0, len(song), int(len(song) / 60)):
    part_name += 1
    song[i:i+int(len(song)) / 60].export("splitted/{}_part.mp3".format(part_name), format="mp3")