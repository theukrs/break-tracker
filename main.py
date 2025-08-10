import math

class Counter:
    def __init__(self):
        self.count = 0
        self.total_time = 0
        self.is_break = False
        self.open_file()
        self.milliformat = True

    def open_file(self):
        try:
            with open("data.txt","r") as file:
                content = float(file.read())
                self.total_time = content

        except FileNotFoundError:
            with open("data.txt", "w") as file:
                file.write(str(0))

    def save_file(self):
        try:
            with open("data.txt", "w") as file:
                file.write(str(float(self.total_time)))
        except FileNotFoundError:
            with open("data.txt", "w") as file:
                file.write(str(0))

    def time_format(self,n):
        mins = math.floor(n / 60)
        secs = math.floor(n % 60)
        millis = int((n - int(n)) * 100)  # get the hundredths part
        
        return f"{mins:02d}:{secs:02d}:{millis:02d}" if self.milliformat else f"{mins:02d}:{secs:02d}"

    def change_format(self):
        if self.milliformat == True:
            self.milliformat = False
        else:
            self.milliformat = True
