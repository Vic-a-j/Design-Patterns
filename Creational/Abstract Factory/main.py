from computer_factory import ComputerFactory, MacFactory, WindowsFactory

# ============================================================
# Client
# ============================================================

class ComputerSetup:
    """
    The client works with *abstract* products and factories.
    It never knows about concrete classes.
    """

    def __init__(self, factory: ComputerFactory):
        print("Setting up workstation...\n")
        self.keyboard = factory.create_keyboard()
        self.monitor = factory.create_monitor()
        print("\nWorkspace ready. 🚀")

    def type(self) -> None:
        self.keyboard.type()

    def display(self) -> None:
        self.monitor.display()

if __name__ == "__main__":
    print("----- MAC SETUP -----")
    mac_setup = ComputerSetup(MacFactory())
    mac_setup.type()
    mac_setup.display()

    print("\n----- WINDOWS SETUP -----")
    windows_setup = ComputerSetup(WindowsFactory())
    windows_setup.type()
    windows_setup.display()