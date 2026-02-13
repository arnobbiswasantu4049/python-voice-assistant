import os

if __name__== '__main__':

    print("Welcome to Robo Speaker 1.0. Created By Lord Arnob")
    while True:
        x= input("Enter What You Want Me to Speak: ")
        if x == "q":
            bye = '''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Bye bye friend');"'''
            os.system(bye)
            break

        command = f'''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"'''

        os.system(command)
