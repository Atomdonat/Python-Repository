import speech2text as s2t
import text2speech as t2s
import comparison_database as cb

begrüßung = "Was kann ich für Sie tun"

t2s.output_speak(begrüßung)

while True:
    cb.comparison_said_text(s2t.input_listen(begrüßung))