# coding: utf-8
#
# dummy device is used for test

from __future__ import absolute_import

import os

from atx.device.device_mixin import DeviceMixin
from atx.device import Display
from PIL import Image


__dir__ = os.path.dirname(os.path.abspath(__file__))

class DummyDevice(DeviceMixin):
    def __init__(self, *args, **kwargs):
        DeviceMixin.__init__(self)
        self._display = Display(1280, 720)
        self._rotation = 1

    def screenshot(self, filename=None):
        """ Take a screenshot """
        # screen size: 1280x720
        screen_path = os.path.join(__dir__, '../../tests/media/dummy_screen.png')
        screen = Image.open(screen_path)
        if filename:
            screen.save(filename)
        return screen

    @property
    def display(self):
        return self._display

    @property
    def rotation(self):
        return self._rotation