from models.inkjet_printer import InkjetPrinter
from models.laser_printer import LaserPrinter
from models.led_printer import LedPrinter
from models.matrix_printer import MatrixPrinter


class PrinterManager:
    def __init__(self):
        self.printers = []

    def add_printer(self, printer):
        self.printers.append(printer)

    def find_by_type(self, printer_type):
        return list(filter(lambda pr: pr.type == printer_type, self.printers))

    def find_printer_with_volume_bigger_than(self, paper_tray_capacity):
        return list(filter(lambda pr: pr.paper_tray_capacity > paper_tray_capacity, self.printers))


if __name__ == "__main__":
    manager = PrinterManager()
    manager.add_printer(LaserPrinter("RealRif", "laser", True, True, 250, 0, 250, 10))
    manager.add_printer(LaserPrinter("Soliq", "laser", True, False, 500, 0, 500, 10))
    manager.add_printer(MatrixPrinter("Epson", "matrix", False, False, 150, 50, 100, 5, 2))
    manager.add_printer(MatrixPrinter("HP", "matrix", False, True, 300, 200, 100, 1, 1))
    manager.add_printer(LedPrinter("Miwa 04", "LED", True, True, 250, 150, 100, 4, 1.25))
    manager.add_printer(LedPrinter("Lazur", "LED", True, False, 18, 18, 0, 5, 1.00))
    manager.add_printer(InkjetPrinter("R", "inkjet", True, True, 100, 50, 50, "RGB", 2, 5, 5, 4,5))
    manager.add_printer(InkjetPrinter("M", "inkjet", True, False, 50, 30, 30, "RGB", 2, 5, 5, 4, 5))

    for printer in manager.printers:
        print(printer)

    print(manager.find_by_type("laser"))
    print(manager.find_printer_with_volume_bigger_than(499))
