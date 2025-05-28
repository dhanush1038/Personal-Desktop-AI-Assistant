import speech_recognition as sr
import pyttsx3
import datetime
import pyautogui

# Initialize text-to-speech engine
engine = pyttsx3.init()


def say(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()


def take_notes():
    """Take voice notes until the user says 'stop taking notes' and save them."""
    say("I'm ready to take notes. Start speaking, and say 'stop taking notes' when finished.")

    recognizer = sr.Recognizer()
    notes = []

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        recognizer.pause_threshold = 2  # Allow natural pauses while speaking
        say("I am listening now...")

        while True:
            try:
                print("Listening for notes...")
                audio = recognizer.listen(source)
                note = recognizer.recognize_google(audio, language="en-in")

                # Debugging - print the recognized text
                print(f"Recognized text: {note}")

                if "stop taking notes" in note.lower():
                    if note.lower() != "stop taking notes":  # Store text before stopping
                        notes.append(note.replace("stop taking notes", "").strip())
                    say("Stopping notes and saving them.")
                    break  # Exit the loop

                if note.strip():  # Ensure it's not empty
                    notes.append(note)  # Append the note properly
                    say(f"Noted: {note}. Anything else?")
                else:
                    say("I couldn't hear anything. Please repeat.")

            except sr.UnknownValueError:
                say("I didn't catch that. Could you repeat?")
            except sr.RequestError:
                say("Speech recognition service is not available right now.")

    # Debugging - Print notes list before saving
    print(f"Final notes list: {notes}")

    # Save notes only if they exist
    if notes:
        file_name = f"notes_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(file_name, "w", encoding="utf-8") as notes_file:
            for line in notes:
                notes_file.write(f"{datetime.datetime.now()}: {line}\n")

        say(f"Your notes have been saved as {file_name}.")
        print(f"✅ Notes saved in {file_name}")
    else:
        say("No notes were recorded.")
        print("❌ No notes recorded.")


def take_screenshot():
    """Take a screenshot and save it."""
    say("Taking a screenshot now.")
    screenshot = pyautogui.screenshot()

    file_name = f"screenshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    screenshot.save(file_name)

    say(f"Screenshot saved as {file_name}.")
