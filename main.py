

import speech_recognition as SR
import pyttsx3

voice_recognizer = SR.Recognizer()


def speak_text(voice_command):
    text_engine = pyttsx3.init()
    text_engine.say(voice_command)
    text_engine.runAndWait()


if __name__ == '__main__':
    try:
        with SR.Microphone() as voice:
            print("Silence Please Calibrating Background Noise")
            voice_recognizer.adjust_for_ambient_noise(
                voice, duration=3)
            print("Calibrated, Please Speak now.....")
            audio_data = voice_recognizer.listen(voice)
            try:
                voice_to_text = voice_recognizer.recognize_google(
                    audio_data)
                print(f"You said {voice_to_text}")
                speak_text(voice_to_text)
            except Exception as e:
                print("sorry, could not recognise")
        # speak_text(voice_to_text)
    except SR.RequestError as e:
        print("Could not request results; {0}".format(e))

    except SR.UnknownValueError:
        print("unknown error occured")
