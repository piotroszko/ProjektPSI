#zadanie 9
import file_manager
plik = file_manager.FileManager("text.txt")
plik.update_file("tekst przykladowy")
print(plik.read_file())