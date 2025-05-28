import pywhatkit as kit
import speech_recognition as sr
import pyttsx3
from twilio.rest import Client

# Initialize text-to-speech engine
engine = pyttsx3.init()

def say(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        say("Listening for your message.")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            message = recognizer.recognize_google(audio)
            return message
        except sr.UnknownValueError:
            say("Sorry, I couldn't understand. Please try again.")
            return listen()
        except sr.RequestError:
            say("Speech recognition service is not available.")
            return None

def send_whatsapp_message():
    """Ask for recipient's phone number, take voice input for the message, and send it via WhatsApp."""
    say("Please enter the recipient's phone number along with the country code.")
    phone_number = input("Enter phone number (with country code, e.g., +11234567890): ")

    say("What message would you like to send?")
    message = listen()

    if message:
        say(f"Sending your message: {message}")
        try:
            kit.sendwhatmsg_instantly(phone_number, message, wait_time=15)
            say("Message sent successfully.")
        except Exception as e:
            say("An error occurred while sending the message.")
            print(f"Error: {e}")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Twilio credentials (replace with your actual credentials)
TWILIO_SID = "AC1009fe3d21a84ee169a9f64287221f37"
TWILIO_AUTH_TOKEN = "130be2d25c9c0451990a1dbc81a65128"
TWILIO_PHONE_NUMBER = "+18454421463"

def say(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def make_phone_call():
    """Ask for recipient's phone number, make a call, and play a message."""
    say("Please enter the recipient's phone number along with the country code.")
    phone_number = input("Enter phone number (with country code, e.g., +11234567890): ")

    say("What message should I say in the call?")
    message = input("Enter the message to be spoken during the call: ")

    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        call = client.calls.create(
            twiml=f'<Response><Say>{message}</Say></Response>',
            to=phone_number,
            from_=TWILIO_PHONE_NUMBER
        )
        say("The call is being placed.")
        print(f"Call initiated successfully. Call SID: {call.sid}")
    except Exception as e:
        say("An error occurred while making the call.")
        print(f"Error: {e}")

