import speech_recognition as sr

def live_speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use the microphone as source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        print("Listening... Speak into the microphone.")
        print("\nSay something:")
        # print("Recognizing...")
        try:
            # Capture the audio and recognize speech
            while True:
                audio = recognizer.listen(source)
                try:
                    # Use Google Web Speech API to transcribe the audio
                    #text = recognizer.recognize_google(audio)
                    text = recognizer.recognize_sphinx(audio)
                    
                    print(text)
                except sr.UnknownValueError:
                    print("......")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    live_speech_to_text()
