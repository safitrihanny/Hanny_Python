import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.window(title="profile",
                    layout=[[sg.Text(SELAMAT DATANG DI KELAS",
                                    font=("Arial",25,"italic","bold","underline"))]
                            [sg.Text("NPM           : 2310010685 ")],
                            [sg.Text("Nama          : HANNY SAFITRI ")],
                            [sg.Text("Kelas         : 5A NON REG BANJARMASIN ")]
                            ],
                    size=(510,200),
                    font=("Times", 18))
window()
window.close()