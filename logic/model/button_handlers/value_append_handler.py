from .... import application
from .base_button_handler import BaseButtonHandler


class ValueAppendHandler(BaseButtonHandler):

    def handle(self, obj, action):
        application.text.append(obj.value)
