# task_executor.py

from midiutil.MidiFile import MIDIFile

def generate_beat():
    # Create a new MIDI file
    midi = MIDIFile()

    # Add MIDI events to create a beat pattern
    # For example, add notes for different drum sounds

    # Save the MIDI file
    with open("generated_beat.mid", "wb") as midi_file:
        midi.writeFile(midi_file)

    return "Beat generated successfully."
