"""
A module that defines a PrinterManager class for managing a collection of printers.
"""
# pylint: disable=import-error
from decorators.method_call import method_call
from decorators.pylint_decorator import run_pylint
from models.inkjet_printer import InkjetPrinter
from models.laser_printer import LaserPrinter
from models.led_printer import LedPrinter
from models.matrix_printer import MatrixPrinter


class PrinterManager:
    """
    A class that manages a collection of printers.
    """

    def __init__(self):
        """
        Initialize a new instance of PrinterManager.
        """
        self.printers = []

    def __len__(self):
        """
        Get the number of printers in the manager.
        """
        return len(self.printers)

    # pylint: disable=redefined-outer-name
    def __getitem__(self, index):
        """
        Get the printer at the specified index.
        """
        return self.printers[index]

    def __iter__(self):
        """
        Get an iterator over the printers.
        """
        return iter(self)

    @method_call
    # pylint: disable=redefined-outer-name
    def add_printer(self, printer):
        """
        Add a printer to the manager.

        Args:
            printer: The printer to add.
        """
        self.printers.append(printer)

    @method_call
    def find_by_type(self, printer_type):
        """
        Find printers of a specific type.

        Args:
            printer_type: The type of printers to find.

        Returns:
            A list of printers matching the specified type.
        """
        return list(filter(lambda pr: pr.type == printer_type, self.printers))

    @method_call
    def find_printer_with_volume_bigger_than(self, paper_tray_capacity):
        """
        Find printers with a paper tray capacity greater than a given value.

        Args:
            paper_tray_capacity: The minimum paper tray capacity.

        Returns:
            A filter object containing printers with a paper tray capacity greater than
             the specified value.
        """
        return filter(lambda pr: pr.paper_tray_capacity > paper_tray_capacity, self.printers)

    def execute_method_on_all_printers(self):
        """
        Execute a method on all printers and return the results.

        Returns:
            A list of method results for each printer.
        """
        return [printer.get_remaining_pages_count() for printer in self.printers]

    def get_printers_enumerated(self):
        """
        Get an enumerated list of printers.

        Returns:
            An enumerate object containing index and printer pairs.
        """
        return enumerate(self.printers)

    def zip_printer_with_method_result(self):
        """
        Zip printers with their corresponding method results.

        Returns:
            A list of tuples containing a printer and its method result.
        """
        return list(zip(self.printers, self.execute_method_on_all_printers()))

    def check_condition_on_all_printers(self):
        """
        Check a condition on all printers.

        Returns:
            A dictionary with 'all' and 'any' keys representing the condition results.
        """
        # pylint: disable=redefined-outer-name
        condition_results = [printer.type == "laser" for printer in self.printers]
        return {"all": all(condition_results), "any": any(condition_results)}

    @run_pylint(__file__)
    def start_pylint(self):
        """
        Start the pylint process to analyze the source code.
        """
        print("Pylint is working")


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

    print("All printers:")
    for printer in manager.printers:
        print(printer)

    print("\nPrinters of type 'laser':")
    laser_printers = manager.find_by_type("laser")
    for printer in laser_printers:
        print(printer)

    print("\nPrinters with paper tray capacity greater than 499:")
    high_volume_printers = manager.find_printer_with_volume_bigger_than(499)
    for printer in high_volume_printers:
        print(printer)

    print("\nExecuting a method on all printers:")
    method_results = manager.execute_method_on_all_printers()
    for result in method_results:
        print(result)

    print("\nGetting enumerated printer list:")
    enumerated_printers = manager.get_printers_enumerated()
    for index, printer in enumerated_printers:
        print(f"Index: {index}, Printer: {printer}")

    print("\nZipping printers with method results:")
    zip_result = manager.zip_printer_with_method_result()
    for printer, result in zip_result:
        print(f"Printer: {printer}, Method Result: {result}")

    print("\nChecking a condition on all printers:")
    condition_results = manager.check_condition_on_all_printers()
    print(f"All condition results: {condition_results['all']}")
    print(f"Any condition results: {condition_results['any']}")
    manager.start_pylint()
