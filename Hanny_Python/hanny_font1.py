import PySimpleGUI as Sg
Sg.theme("DarkGreen4")
Sg.theme_text_color("#FFFF00")
Window = Sg.Window(title="Profile Hanny",
                   layout=[[Sg.Text("NPM    : 2310010685")],
                           [Sg.Text("Nama   : Hanny Safitri")],
                           [Sg.Text("Kelas  : 5A Non Regular Banjarmasin")],
                           [Sg.Text("Matkul : Pemrograman Visual 3")]
                           ],
                    size=(400,200),
                    font=("Times", 18))
Window()
Window.close()