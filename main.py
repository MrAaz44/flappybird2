from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.image import Image
from kivy.properties import *
from kivy.metrics import *
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from random import randint
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class pop(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (.7,.7)
        self.all = BoxLayout(orientation='vertical')
        self.add_widget(self.all)
        self.süre = Label(text="Skorunuz = "+str(app.skor),size_hint_y=.3)
        self.all.add_widget(self.süre)

        butonlar = BoxLayout(size_hint_y=.7)
        self.all.add_widget(butonlar)

        self.çık = Button(text="Exit")
        butonlar.add_widget(self.çık)
        self.çık.bind(on_release=self.exit)

        self.geri = Button(text="tekrar başla")
        butonlar.add_widget(self.geri)
        self.geri.bind(on_release=self.returnn)

    def returnn(self,b):
        app.oyunda = 0
        self.dismiss()

    def exit(self,b):
        exit()

class game(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bird = Image(source='bird.png',size_hint=(None,None),size=(dp(50),dp(50)),pos_hint={'x':app.birdx,'y':app.birdy})
        self.add_widget(self.bird)
        Clock.schedule_interval(self.grav, 0.001)
        Clock.schedule_interval(self.öl, 0.01)
        Clock.schedule_interval(self.ekle, 2)
        self.skor = Label(text=str(app.skor),pos_hint={'center_x':.5,'y':.9},size_hint=(.1,.1))
        self.add_widget(self.skor)
        Clock.schedule_interval(self.değiş, 1)

    def değiş(self,b):
        self.skor.text = str(app.skor)

    def on_touch_down(self, touch):
        if app.oyunda == 0:
            app.birdy += 0.07
            self.bird.pos_hint = {'x':app.birdx,'y':app.birdy}

    def grav(self,b):
        if app.oyunda == 0:
            app.birdy -= 0.0013
            self.bird.pos_hint = {'x': app.birdx, 'y': app.birdy}

    def öl(self,b):
        if app.oyunda == 0:
            if app.birdy <= 0 or app.birdy >= 1:
                pop().open()
                app.oyunda = 1
                app.birdy = .5
                f = open("last_skor.txt","a")
                fw = open("last_skor.txt","w")
                fr = open("last_skor.txt","r")
                if fr.read() == "":
                    print("dosya boş")
                    fw.write(str(app.skor))
                else:
                    fw.write(str(app.skor))
                app.skor = 0

    def ekle(self,b):
        if app.oyunda == 0:
            yy = randint(50, 99)
            self.add_widget(üst_bar(yy = yy/100))
            self.add_widget(alt_bar(yyy = (yy-98)/100))

class üst_bar(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (0,1,0,1)
        self.size_hint = (.1,.5)
        self.pos_hint = {'x':self.xx,'y':self.yy}
        Clock.schedule_interval(self.kay, 0.001)
        Clock.schedule_interval(self.çarp, 0.001)

    def kay(self,b):
        if app.oyunda == 0:
            self.xx -= 0.003
            self.pos_hint = {'x': self.xx, 'y': self.yy}

    def çarp(self,b):
        if app.oyunda == 0:
            if self.xx-0.05<app.birdx<self.xx+0.05 and self.yy<app.birdy<self.yy+.5:
                pop().open()
                app.oyunda = 1
                app.birdy = .5
                f = open("last_skor.txt", "a")
                fw = open("last_skor.txt", "w")
                fr = open("last_skor.txt", "r")
                if fr.read() == "":
                    print("dosya boş")
                    fw.write(str(app.skor))
                else:
                    fw.write(str(app.skor))
                app.skor = 0

    xx = NumericProperty(.8)
    yy = NumericProperty()

class alt_bar(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (0, 1, 0, 1)
        self.size_hint = (.1, .5)
        self.pos_hint = {'x': self.xxx, 'y': self.yyy}
        Clock.schedule_interval(self.kay, .001)
        Clock.schedule_interval(self.çarp, 0.01)

    def kay(self,b):
        if app.oyunda == 0:
            self.xxx -= 0.003
            self.pos_hint = {'x': self.xxx, 'y': self.yyy}

    def çarp(self,b):
        if app.oyunda == 0:
            if self.xxx-0.05<app.birdx<self.xxx+0.05 and self.yyy<app.birdy<self.yyy+.5:
                pop().open()
                app.oyunda = 1
                app.birdy = .5
                f = open("last_skor.txt", "a")
                fw = open("last_skor.txt", "w")
                fr = open("last_skor.txt", "r")
                if fr.read() == "":
                    print("dosya boş")
                    fw.write(str(app.skor))
                else:
                    fw.write(str(app.skor))
                app.skor = 0

    xxx = NumericProperty(.8)
    yyy = NumericProperty()

class app(App):
    def build(self):
        Clock.schedule_interval(self.arttır, 1)
        return game()
    birdx = NumericProperty(.2)
    birdy = NumericProperty(.7)
    skor = NumericProperty(0)
    oyunda = NumericProperty(0)
    def arttır(self,b):
        if self.oyunda == 0:
            self.skor += 1
        else:
            print("Menüde")

if __name__ == "__main__":
    app = app()
    app.run()