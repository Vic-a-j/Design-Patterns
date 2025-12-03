from abc import ABC, abstractmethod

# ============================================================
# Abstract Products
# ============================================================

class Keyboard(ABC):
    @abstractmethod
    def type(self) -> None:
        pass


class Monitor(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


# ============================================================
# Concrete Products — Mac Family
# ============================================================

class MacKeyboard(Keyboard):
    def type(self):
        print("Typing with the sleek, low-profile Mac keyboard.")


class MacMonitor(Monitor):
    def display(self):
        print("Displaying on a Retina Mac monitor with TrueTone.")


# ============================================================
# Concrete Products — Windows Family
# ============================================================

class WindowsKeyboard(Keyboard):
    def type(self):
        print("Typing with the mechanical Windows keyboard.")


class WindowsMonitor(Monitor):
    def display(self):
        print("Displaying on a Windows monitor with HDR10.")