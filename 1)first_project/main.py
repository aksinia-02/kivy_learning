from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

# BoxLayout
# AnchorLayout
# GridLayout
# StackLayout
# Scroll View
# PageLayout

# FloatLayout
# RelativeLayout
# ScatterLayout


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 10):
            self.orientation = "rl-tb"
            size = dp(100) + i * 10
            b = Button(text=str(i), size_hint=(None, None), size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     self.add_widget(b1)
    #     self.add_widget(b2)


class MainWidget(Widget):
    pass


class FirstProjectApp(App):
    pass


FirstProjectApp().run()
