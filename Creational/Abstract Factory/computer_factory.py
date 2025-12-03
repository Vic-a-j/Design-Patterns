from abc import ABC, abstractmethod

from computer_products import Keyboard, Monitor, MacKeyboard, MacMonitor, WindowsKeyboard, WindowsMonitor

# ============================================================
# Abstract Factory
# ============================================================

class ComputerFactory(ABC):
    @abstractmethod
    def create_keyboard(self) -> Keyboard:
        pass

    @abstractmethod
    def create_monitor(self) -> Monitor:
        pass


# ============================================================
# Concrete Creators
#
# Note: In this example, we are creating multiple products - Keyboards, and Monitors
# ============================================================

class MacFactory(ComputerFactory):
    def create_keyboard(self) -> Keyboard:
        return MacKeyboard()

    def create_monitor(self) -> Monitor:
        return MacMonitor()


class WindowsFactory(ComputerFactory):
    def create_keyboard(self) -> Keyboard:
        return WindowsKeyboard()

    def create_monitor(self) -> Monitor:
        return WindowsMonitor()