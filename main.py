import PySimpleGUI as sg
import requests,json;
import mymodule;
from PIL import Image;
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  
            [sg.Text("Click button to get random anime images",font = "Any 25",justification="center")],
            [sg.Text("Give image url if you want to show it",font = "Any 18")],
            [sg.InputText()],
            [sg.Button('Show anime image'),sg.Button('Show url image'), sg.Button('Exit')],
            [sg.Image(r"g.png",key = "img")],
            [sg.Text('',key = "connection",font = "Any 22",justification="center")]]

# Create the Window
window = sg.Window('Get image', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break;
    if event == 'Show anime image':
        try:
            window['connection'].update('Internet is working');
            mymodule.get_image();
            layout+=[sg.Image(r"g.png")];
            window['img'].update(r"img1.png");
        except Exception:
            window['connection'].update('Internet is not working');
            pass;
    if event == "Show url image":
        try:
            r = requests.get(values[0]);
            r = r.content;
            out = open(".\img2","wb");
            out.write(r);
            mymodule.convert_png();
            out.close();
            window['img'].update(r"C:\django\img2.png");
            pass;
        except Exception:
            window['connection'].update('No connection to site')
            pass;
        
        # sg.Image('');
    print('You entered ', values[0])

window.close()