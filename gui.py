import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlFile
from pyforms.controls import ControlCombo
from pyforms.controls import ControlButton

from PIL import Image


class Gui(BaseWidget):
    converter = {
        'jpg': ['png', 'gif', 'tiff', 'pdf'],
        'tiff': ['png', 'gif', 'bmp'],
        'bmp': ['png', 'gif', 'tiff']
    }

    def __init__(self):
        super(Gui, self).__init__('Converter')

        self._firstname = ControlText('First name')
        #self.__from = ControlCombo('From')
        #self.__from.add_item('jpeg')
        #self.__from.add_item('tiff')
        #self.__from.add_item('bmp')
        self._fileControl = ControlFile('Select File')
        self._fileControl.changed_event = self.__fileselectionevent
        self._toControl = ControlCombo('To', enabled=0)
        self._buttonControl = ControlButton('Convert', enabled=0)
        self._buttonControl.pressed = self.__clicker

    def __fileselectionevent(self):
        self._firstname.value = "file"
        self._fileFormat = self._fileControl.value.split('.')[-1]
        if self._fileFormat in self.converter:
            self._toControl.enabled = 1
            for item in self.converter[self._fileFormat]:
                self._toControl.add_item(item)
            self._buttonControl.enabled = 1
        else:
            self._toControl.enabled = 0
            self._buttonControl.enabled = 0

    def __clicker(self):
        self._firstname.value = "click"
        im = Image.open(self._fileControl.value)
        rgb_im = im.convert('RGB')
        self._firstname.value = self._fileControl.value.replace(self._fileFormat, self._buttonControl.value)
        rgb_im.save(self._fileControl.value.replace(self._fileFormat, self._buttonControl.value), quality=95)


if __name__ == "__main__":
    pyforms.start_app(Gui, geometry=(200, 200, 300, 200))
