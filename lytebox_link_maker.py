import os

def lytebox_link_maker(folder_location):
    plik = open("tekst.log", "w") 
    for i in os.listdir(folder_location):
        (shortname, extension) = os.path.splitext(i)
        cos = [".jpg",".gif", ".png"]       
        if extension in cos:
            plik.write( '<a href="images"'+ i +'" class="lytebox" data-lyte-options="group:vacation" data-title="Some Title">Nazwa</a>\n')
            plik.close() 
        else:
            print "Plik "+i+" nie jest obrazem."
           
    print plik.read()
lytebox_link_maker("c:\\users\\Konrad\\desktop\\foty\\")

