from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Define the list of names
        self.names = ["Jack", "Sally", "Jay"]

    def build(self):
        layout = BoxLayout(orientation='vertical')
        # Loop through the list of names and create a label for each one
        for name in self.names:
            label = Label(text=name)
            layout.add_widget(label)
        return layout


if __name__ == '__main__':
    DynamicLabelsApp().run()
