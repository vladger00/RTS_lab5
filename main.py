import kivy.app
import kivy.uix.button
import kivy.uix.label
import  kivy.uix.boxlayout
import kivy.uix.textinput
import math
from kivy.core.window import Window


class MyApp(kivy.app.App):


    def build(self):
        Window.clearcolor = (.88,.53,.0, 1)
        self.textInput = kivy.uix.textinput.TextInput()
        bl = kivy.uix.boxlayout.BoxLayout (orientation = "vertical", padding = 50, spacing = 5)
        bl.add_widget(kivy.uix.label.Label(text = " Лабораторна робота №5. Факторизація Ферма"))
        bl.add_widget(kivy.uix.label.Label(text = "Введіть число n"))
        bl.add_widget(self.textInput)
        self.button = bl.add_widget(kivy.uix.button.Button(text="Факторизація",on_press=self.Message))
        #bl.add_widget(self.button)
        self.label = kivy.uix.label.Label(text = "Результат")
        bl.add_widget(self.label)

        return bl

    def Message(self, b):
        txt = self.textInput.text
        if txt.isdigit():
            n = int(txt)
            a,b = self.factorization(n)
            self.label.text = "Для n : {}\n p = {}\n q = {}".format(n, a, b)
        else:
            self.label.text = "Введіть число"

    def factorization(self, n):
        print(n)
        s = math.ceil(math.sqrt(n))
        k = 0
        while True:
            x = s + k
            y2 = x ** 2 - n
            y = int(math.sqrt(y2))
            if y * y == y2:
                p = x + y
                q = x - y
                break
            elif x >= n :
                p, q = None, None
                break

            k += 1


        return p, q

if __name__ == "__main__":
    app = MyApp()
    app.run()