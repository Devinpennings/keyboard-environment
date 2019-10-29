from kivy.clock import Clock, mainthread
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

from ... import application


class Keyboard(StackLayout):
    def on_input(self, value):
        pass

    def on_button_press(self, instance):
        self.dispatch('on_input', instance.text)

    def __init__(self):
        super().__init__()
        self.draw_keyboard()

        with self.canvas.before:
            Color(1, 1, 1)
            self.draw_grid()

        self.register_event_type('on_input')

    def draw_keyboard(self):
        for b in application.keyboard.buttons:
            button = Button(text=b.symbol, width=b.rectangle.width, height=b.rectangle.height, size_hint=(None, None))
            button.bind(on_press=self.on_button_press)

            def press_button(button_to_press, duration):
                button_to_press.widget.trigger_action(duration=duration)

            b.bind(on_click=press_button)

            self.add_widget(button)
            self.set_button_pos(b, button)

    @mainthread
    def set_button_pos(self, button, widget):
        button.widget = widget
        widget.bind(on_click=button.click)

    def draw_grid(self):
        for cell in application.grid.cells:

            # Canvas draw workaround
            max_y = application.grid.height - cell.rectangle.height

            def click_cell(cell_to_draw, duration):
                rectangle = Rectangle(pos=(cell_to_draw.rectangle.pos_x,
                                           max_y - cell_to_draw.rectangle.pos_y + (
                                               application.cli.height if application.cli else 0)),
                                      size=(cell_to_draw.rectangle.width, cell_to_draw.rectangle.height))
                with self.canvas:
                    Color(0, 1, 0, 0.5)

                self.canvas.add(rectangle)

                def remove(obj):
                    self.canvas.remove(rectangle)

                Clock.schedule_once(remove, duration)

            cell.bind(on_click=click_cell)

            self.canvas.add(Line(
                width=1.5,
                rectangle=(cell.rectangle.pos_x,
                           cell.rectangle.pos_y + (application.cli.height if application.cli else 0),
                           cell.rectangle.width,
                           cell.rectangle.height)))
