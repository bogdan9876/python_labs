"""
A module that defines a SetManager class for managing sets of printers.
"""
# pylint: disable=import-error
from managers.printer_manager import PrinterManager
from models.inkjet_printer import InkjetPrinter
from models.laser_printer import LaserPrinter
from models.led_printer import LedPrinter
from models.matrix_printer import MatrixPrinter


class SetManager:
    """
    A class that manages sets of printers.
    """

    def __init__(self, printer_manager):
        """
        Initialize a new instance of SetManager.

        Args:
            printer_manager: The printer manager to use.
        """
        self.printers = printer_manager
        self.index = 0

    def __len__(self):
        """
        Get the number of elements in the set manager.
        """
        return len(list(iter(self)))

    def __iter__(self):
        """
        Get an iterator over the set manager.
        """
        # pylint: disable=attribute-defined-outside-init
        self.printer_set_list = []
        for printer in self.printers:
            for name in printer.favorite_tasks:
                self.printer_set_list.append(name)
        return iter(self.printer_set_list)

    def __getitem__(self, index):
        """
        Get the element at the specified index.

        Args:
            index: The index of the element.

        Returns:
            The element at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index not in range")
        return self.printer_set_list[index]

    def __next__(self):
        """
        Get the next element in the iteration.

        Returns:
            The next element in the iteration.

        Raises:
            StopIteration: If there are no more elements.
        """
        if self.index >= len(self.printer_set_list):
            raise StopIteration
        swap = self.printer_set_list[self.index]
        self.index += 1
        return swap


if __name__ == "__main__":
    manager = PrinterManager()
    manager.add_printer(LaserPrinter("RealRif", "laser", True, True, 250, 0, 250, 10))
    manager.add_printer(LaserPrinter("Soliq", "laser", True, False, 500, 0, 500, 10))
    manager.add_printer(MatrixPrinter("Epson", "matrix", False, False, 150, 50, 100, 5, 2))
    manager.add_printer(MatrixPrinter("HP", "matrix", False, True, 300, 200, 100, 1, 1))
    manager.add_printer(LedPrinter("Miwa 04", "LED", True, True, 250, 150, 100, 4, 1.25))
    manager.add_printer(LedPrinter("Lazur", "LED", True, False, 18, 18, 0, 5, 1.00))
    manager.add_printer(InkjetPrinter("R", "inkjet", True, True, 100, 50, 50, "RGB", 2, 5, 5, 4, 5))
    manager.add_printer(InkjetPrinter("M", "inkjet", True, False, 50, 30, 30, "RGB", 2, 5, 5, 4, 5))

    print(f"SetManager length: {len(manager)}")

    print("Iterating over SetManager:")
    for smanager in manager:
        print(smanager)

    print("\nOutput 2nd element in SetManager:", manager[1])
