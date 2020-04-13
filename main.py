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
        self.textInput1 = kivy.uix.textinput.TextInput()
        self.textInput2 = kivy.uix.textinput.TextInput()
        bl = kivy.uix.boxlayout.BoxLayout (orientation = "vertical", padding = 50, spacing = 5)
        bl.add_widget(kivy.uix.label.Label(text = " Лабораторна робота №5. Факторизація Ферма"))
        bl.add_widget(kivy.uix.label.Label(text = "Введіть число n"))
        bl.add_widget(self.textInput1)
        bl.add_widget(kivy.uix.label.Label(text="Введіть кількість ітерацій"))
        bl.add_widget(self.textInput2)
        self.button = bl.add_widget(kivy.uix.button.Button(text="Факторизація",on_press=self.factorization))
        self.label = kivy.uix.label.Label(text = "Результат")
        bl.add_widget(self.label)

        return bl

    def factorization(self, n):
        print(n)
        txt = self.textInput1.text
        numb = self.textInput2.text       #Число ітерацій, задане користувачем
        if txt.isdigit() and numb.isdigit():
            numb = int(numb)
            n= int(txt)
            s = math.ceil(math.sqrt(n))
            k = 0
            while True:
                if k < numb:
                    x = s + k
                    y2 = x ** 2 - n
                    y = int(math.sqrt(y2))
                    if y * y == y2:
                        p = x + y
                        q = x - y
                        self.label.text = "Для n : {}\n p = {}\n q = {}".format(n, p, q)
                        break
                    elif x >= n :
                        p, q = None, None
                        self.label.text = "Для n : {}\n p = {}\n q = {}".format(n, p, q)
                        break
                else:
                    self.label.text = "Помилка. Ввведена кількість ітерацій перевищена"
                    break

                k += 1
        else:
            self.label.text = "Введіть число n та кількість ітерацій"



if __name__ == "__main__":
    app = MyApp()
    app.run()