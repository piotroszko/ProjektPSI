# zadanie 8
class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def update_file(self, text_data):
        file_object = open(self.file_name, 'a')
        file_object.write(text_data)
        file_object.close()

    def read_file(self):
        file_object = open(self.file_name, 'r')
        zwrot = file_object.read()
        file_object.close()
        return zwrot
