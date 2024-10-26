import PySimpleGUI as Sg
Window = Sg.Window(title="Profile Hanny Safitri",
                   layout=[[Sg.Text("Selamat Belajar PySimpleGUI Hanny")],
                           [Sg.Text("NPM    : 2310010685")],
                           [Sg.Text("Nama   : Hanny Safitri")],
                           [Sg.Text("Kelas  : 5A Non Regular Banjarmasin")],
                           [Sg.Text("Matkul : Pemrograman Visual 3")]
                           ],
                    size=(400,200))
Window()
Window.close()