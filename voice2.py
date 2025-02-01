from vosk import Model, KaldiRecognizer
import pyaudio
import pyautogui

model = Model(r"C:\Program Files\Geany\Voice\vosk-model-small-ru-0.22")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
fl = False
# ~ color = (254,246,1)
color = (254, 220, 2)

while True:
    data = stream.read(4096, exception_on_overflow = False)
    

    if recognizer.AcceptWaveform(data):
        text = f"{recognizer.Result()[14:-3]}"
        
        if 'стоп' in text:
            continue
        
        elif 'шесть полей' in text:
            fl = True
        elif 'пять полей' in text:
            fl = False
        
        elif 'жёлтый' in text:
            fls = False
            s = pyautogui.screenshot()
            for x in range(410, 2130):
                for y in range(220, 1360):
                    if s.getpixel((x, y)) == color:
                        pyautogui.click(x, y)
                        fls = True
                        break
                if fls:
                    break
        
        elif 'первый' in text:
            pyautogui.click(613, 102)
        elif 'второй' in text:
            pyautogui.click(730	, 102)
        elif 'третий' in text:
            pyautogui.click(895, 102)
        elif 'четвёртый' in text:
            pyautogui.click(1039, 102)
        elif 'пятый' in text:
            pyautogui.click(1183, 102)
        elif 'шестой' in text:
            pyautogui.click(1327, 102)
        elif 'седьмой' in text:
            pyautogui.click(1471, 102)
        elif 'лопата' in text:
            pyautogui.click(1640, 102)
        
        elif text[:4] == 'один':
            y = 324
            if fl:
                y -= 20
            if 'один' in text[5:]:
                pyautogui.click(509, y)
            elif 'два' in text:
                pyautogui.click(699, y)
            elif 'три' in text:
                pyautogui.click(886, y)
            elif 'четыре' in text:
                pyautogui.click(1108, y)
            elif 'пять' in text:
                pyautogui.click(1279, y)
            elif 'шесть' in text:
                pyautogui.click(1469, y)
            elif 'восемь' in text:
                pyautogui.click(1848, y)
            elif 'семь' in text:
                pyautogui.click(1662, y)
            elif 'девять' in text:
                pyautogui.click(2068, y)
        
        elif text[:3] == 'два':
            y = 539
            if fl:
                y -= 23
            if 'один' in text:
                pyautogui.click(509, y)
            elif 'два' in text[4:]:
                pyautogui.click(699, y)
            elif 'три' in text:
                pyautogui.click(886, y)
            elif 'четыре' in text:
                pyautogui.click(1108, y)
            elif 'пять' in text:
                pyautogui.click(1279, y)
            elif 'шесть' in text:
                pyautogui.click(1469, y)
            elif 'восемь' in text:
                pyautogui.click(1848, y)
            elif 'семь' in text:
                pyautogui.click(1662, y)
            elif 'девять' in text:
                pyautogui.click(2068, y)
        
        elif text[:3] == 'три':
            y = 765
            if fl:
                y += 13
            if 'один' in text:
                pyautogui.click(509, y)
            elif 'два' in text:
                pyautogui.click(699, y)
            elif 'три' in text[4:]:
                pyautogui.click(886, y)
            elif 'четыре' in text:
                pyautogui.click(1108, y)
            elif 'пять' in text:
                pyautogui.click(1279, y)
            elif 'шесть' in text:
                pyautogui.click(1469, y)
            elif 'восемь' in text:
                pyautogui.click(1848, y)
            elif 'семь' in text:
                pyautogui.click(1662, y)
            elif 'девять' in text:
                pyautogui.click(2068, y)
            
        elif text[:6] == 'четыре':
            y = 1009
            if fl:
                y -= 61
            if 'один' in text:
                pyautogui.click(509, y)
            elif 'два' in text:
                pyautogui.click(699, y)
            elif 'три' in text:
                pyautogui.click(886, y)
            elif 'четыре' in text[7:]:
                pyautogui.click(1108, y)
            elif 'пять' in text:
                pyautogui.click(1279, y)
            elif 'шесть' in text:
                pyautogui.click(1469, y)
            elif 'восемь' in text:
                pyautogui.click(1848, y)
            elif 'семь' in text:
                pyautogui.click(1662, y)
            elif 'девять' in text:
                pyautogui.click(2068, y)
        
        elif text[:4] == 'пять':
            y = 1254
            if fl:
                y -= 93
            if 'один' in text:
                pyautogui.click(509, y)
            elif 'два' in text:
                pyautogui.click(699, y)
            elif 'три' in text:
                pyautogui.click(886, y)
            elif 'четыре' in text:
                pyautogui.click(1108, y)
            elif 'пять' in text[5:]:
                pyautogui.click(1279, y)
            elif 'шесть' in text:
                pyautogui.click(1469, y)
            elif 'восемь' in text:
                pyautogui.click(1848, y)
            elif 'семь' in text:
                pyautogui.click(1662, y)
            elif 'девять' in text:
                pyautogui.click(2068, y)
        
        elif text[:5] == 'шесть':
            y = 1340
            if 'один' in text:
                pyautogui.click(509, y)
            elif 'два' in text:
                pyautogui.click(699, y)
            elif 'три' in text:
                pyautogui.click(886, y)
            elif 'четыре' in text:
                pyautogui.click(1108, y)
            elif 'пять' in text[5:]:
                pyautogui.click(1279, y)
            elif 'шесть' in text[6:]:
                pyautogui.click(1469, y)
            elif 'восемь' in text:
                pyautogui.click(1848, y)
            elif 'семь' in text:
                pyautogui.click(1662, y)
            elif 'девять' in text:
                pyautogui.click(2068, y)
        
        elif 'клик' in text:
            pyautogui.click()
        elif 'верх' in text:
            pyautogui.move(0, -30)
        elif 'вниз' in text:
            pyautogui.move(0, 30)
        elif 'вправо' in text:
            pyautogui.move(30, 0)
        elif 'влево' in text:
            pyautogui.move(-30, 0)
        
        elif text != '':
            print(text)

