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
        self.keyboard = factory.create_keyboard()
        self.monitor = factory.create_monitor()

    def prepare_workspace(self):
        print("Setting up workstation...\n")
        self.keyboard.type()
        self.monitor.display()
        print("\nWorkspace ready. 🚀")

if __name__ == "__main__":
    print("----- MAC SETUP -----")
    mac_setup = ComputerSetup(MacFactory())
    mac_setup.prepare_workspace()

    print("\n----- WINDOWS SETUP -----")
    windows_setup = ComputerSetup(WindowsFactory())
    windows_setup.prepare_workspace()