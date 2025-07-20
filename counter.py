import math

class Counter:
    def __init__(self):
        self.count = 0
        self.total_time = 0
        self.is_break = False
        self.open_file()

    def open_file(self):
        try:
            with open("data.txt","r") as file:
                content = float(file.read())
                self.total_time = content

        except FileNotFoundError:
            with open("data.txt", "w") as file:
                file.write(str(0))

    def save_file(self):
        with open("data.txt", "w") as file:
            file.write(str(float(self.total_time)))

    def time_format(self,n):
        mins = math.floor(n / 60)
        secs = math.floor(n % 60)
        millis = int((n - int(n)) * 100)  # get the hundredths part

        return f"{mins:02d}:{secs:02d}:{millis:02d}"
