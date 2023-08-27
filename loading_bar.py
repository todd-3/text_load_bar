"""
loading_bar.py
Author: Roman T

Provides a simple text based loading bar of adjustable size

Based on code from https://gist.github.com/greenstick/b23e475d2bfdc3a82e34eaa1f6781ee4
and https://stackoverflow.com/a/34325723
"""

__version__ = 0.3

class LoadingBar:

    def __init__(self, total: int, prefix: str = "", decimals:int = 2, length:int = 25,
                 auto_size:bool = False, fill:str = "█"):
        from os import system
        system("")  # sets console to allow ansi control characters

        self.total = total
        self.prefix = prefix
        self.counter = 0
        self.fill_char = fill
        self.bar_length = length
        self.decimal_places = decimals

        # creates format string like {0:.2f} to define a floating point number out to given number of decimal places
        self.rounding = "\033[94m{0:." + str(decimals) + "f}\033[0m"

        if auto_size:
            self.auto_size()

    def increment(self, counter_increment: int = 0):
        self.counter += counter_increment  # increments counter

        # fills in format string with current percentage complete
        percent = self.rounding.format(100 * (self.counter / float(self.total)))

        filledLength = int(self.bar_length * self.counter // self.total)  # calculates total of bar filled

        # creates string for bar filled with correct number of fill characters
        bar = "\033[94m" + self.fill_char * filledLength + "\033[92m" + '-' * (self.bar_length - filledLength) + "\033[0m"

        # prints combination of prefix, generated bar, and calculated percentage
        # bar is fenced by | on either side like |███-----|
        print(f'\r{self.prefix} |{bar}| {percent}%', end="\r")
              
        # Print New Line on Complete
        if self.counter >= self.total:
            self.counter = 0
            print()
            
    def auto_size(self):
        from shutil import get_terminal_size as gts
        
        try:
            # gets width of terminal using shutil
            # sets fallback value equal to self.bar_length
            terminal_width = gts((self.bar_length, 1)).columns

            extra_width = len(self.prefix) + (self.decimal_places + 4) + 5  # accounts for length of other printed elements
            self.bar_length = terminal_width - extra_width
                
        except Exception as e:
            print("Error encountered: Could not find terminal width. Switching to default sizing")
