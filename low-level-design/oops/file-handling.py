import os

file = "example.txt"

if os.path.exists(file):
    print("File Name:", os.path.basename(file))
    print("Absolute Path:", os.path.abspath(file))
    print("Writable:", os.access(file, os.W_OK))
    print("Readable:", os.access(file, os.R_OK))
    print("File Size in bytes:", os.path.getsize(file))
else:
    print("The file does not exist.")

write = None

try:
    write = open(file, "w")
    write.write("Hello, World!")
    write.close()
except IOError as e:
    print("Error:", e)
finally:
    if write:
        write.close()

reader = None

try:
    reader = open(file, "r")
    content = reader.read()
    print("Content:", content)
    reader.close()
except IOError as e:
    print("Error:", e)
finally:
    if reader:
        reader.close()

try:
    with open(file, "r") as reader:
        for line in reader:
            print("strip: ", line.strip())
except IOError as e:
    print("Error:", e)

class Logger:
    def __init__(self, path):
        if not os.path.exists(path):
            with open(path, "w"): 
                pass
        self.path = path

    def log(self, message):
        try:
            with open(self.path, "a") as bw:
                bw.write(message + "\n")
        except Exception as e:
            print("Error:", e)
        finally:
            if bw:
                bw.close()

if __name__ == "__main__":
    try:
        myLogger = Logger("application.log")

        myLogger.log("Application started...")
        myLogger.log("User logged in.")
        myLogger.log("Error: Unable to connect to the database.")
        myLogger.log("Application closed.")

        print("Logs have been written successfully.")
    except Exception as e:
        print(e)