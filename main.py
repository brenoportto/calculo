from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.image import AsyncImage
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex


class MyApp(App):
    def build(self):
        #imagem
        self.tela = Window.size = (420, 600)
        self.background_image = AsyncImage(source='C:/Users/breno/pythonProject/images/OIG (10).png')
        #label
        self.label1 = Label(text="Quantos peixes dá?", font_size= 40 , size_hint=(None, None), size=(300, 50),
                      pos_hint={'center_x': 0.5, 'center_y': 0.95},  color=get_color_from_hex('##880996'))
        self.label2 = Label(text="Digite a largura do viveiro e m.", font_size= 20, size=(300, 50),
                      pos_hint={'center_x': 0.5, 'center_y': 0.90},  color=get_color_from_hex('##880996'))
        self.label3 = Label(text="Digite o comprimento do viveiro e m.", font_size= 20, size=(300, 50),
                      pos_hint={'center_x': 0.5, 'center_y': 0.80},  color=get_color_from_hex('##880996'))
        self.label4 = Label(text="Digite a profundidades média do viveiro e m.", font_size= 20, size=(300, 50),
                      pos_hint={'center_x': 0.5, 'center_y': 0.7},  color=get_color_from_hex('##880996'))
        self.label5 = Label(text="Selecione o a espécie abaixo:", font_size= 20, size=(300, 50),
                      pos_hint={'center_x': 0.5, 'center_y': 0.50},  color=get_color_from_hex('##880996'))
        self.label6 = Label(text="Resultado", font_size= 20 , size=(300, 50),
                      pos_hint={'center_x': 0.5, 'center_y': 0.2},  color=get_color_from_hex('##880996'))

        #textos
        self.text1 = TextInput(size_hint=(None, None),
            size=(300, 30), pos_hint={'center_x': 0.5, 'center_y': 0.85}, font_size= 18)
        self.text2 = TextInput(size_hint=(None, None),
            size=(300, 30), pos_hint={'center_x': 0.5, 'center_y': 0.75}, font_size= 18)
        self.text3 = TextInput(size_hint=(None, None),
            size=(300, 30), pos_hint={'center_x': 0.5, 'center_y': 0.65})

        #butoes
        self.button = Button(size_hint=(None, None),text="Calcular", background_color=(1, 0, 0, 1), size=(300, 50),
                      pos_hint={'center_x': 0.5, 'center_y': 0.33})
        self.button.bind(on_press=self.atualizar_texto)
        #spinners
        self.tree = Spinner(text="Tambaqui", values=("Tambaqui", "Matrinxã", "Pirapitinga"), size_hint=(None, None),
            size=(100, 44), pos_hint={'center_x': 0.5, 'center_y': 0.42})
        #layouts
        self.layout = RelativeLayout()

        #inserir widgets
        self.layout.add_widget(self.background_image)
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.text1)
        self.layout.add_widget(self.label3)
        self.layout.add_widget(self.text2)
        self.layout.add_widget(self.label4)
        self.layout.add_widget(self.text3)
        self.layout.add_widget(self.label5)
        self.layout.add_widget(self.tree)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.label6)
        return self.layout
    def dismiss_popup(self, instance):
        self.popup.dismiss()

    def atualizar_texto(self, instance):
        if self.text1.text !='':
                    raca = self.tree.text
                    if raca == 'Matrinxã':
                        a2= self.text1.text.replace(',', '.')
                        a = float(a2)
                        b2 = self.text2.text.replace(',', '.')
                        b = float(b2)
                        c2 = self.text2.text.replace(',', '.')
                        c = float(c2)
                        d = a*b*c
                        self.label6.text = f"Resultado: \n*Quantidade máxima -  {d*0.7:.2f} peixes \n*Quantidade mínima   {d*0.8:.2f} peixes"
                    elif raca == 'Tambaqui':
                        a2= self.text1.text.replace(',', '.')
                        a = float(a2)
                        b2 = self.text2.text.replace(',', '.')
                        b = float(b2)
                        c2 = self.text2.text.replace(',', '.')
                        c = float(c2)
                        d = a*b*c
                        self.label6.text = f"Resultado: \n*Quantidade máxima -  {d*0.03:.2f} peixes \n*Quantidade mínima -  {d*0.07:.2f} peixes"
                    elif raca == 'Pirapitinga':
                        a2= self.text1.text.replace(',', '.')
                        a = float(a2)
                        b2 = self.text2.text.replace(',', '.')
                        b = float(b2)
                        c2 = self.text2.text.replace(',', '.')
                        c = float(c2)
                        d = a*b*c
                        self.label6.text = f"Resultado: \n*Quantidade máxima -  {d*0.7:.2f} peixes \n*Quantidade mínima -  {d*0.8:.2f} peixes"
        else:

            layout = BoxLayout(orientation='vertical')
            content = Label(text="Digite um numero maior que zero para calcular")
            ok_button = Button(text="OK", on_press=self.dismiss_popup)

            layout.add_widget(content)
            layout.add_widget(ok_button)

            popup = Popup(title="#Erro!", content=layout, size_hint=(None, None), size=(400, 200))
            self.popup = popup  # Armazene o popup para poder fechá-lo posteriormente
            popup.open()

MyApp().run()