# coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Marley Adriano de Souza Silva <marleyas@gmail.com>
# Created Date: 2022-02-27
# version ='1.0'
# ---------------------------------------------------------------------------
from pystray import Menu, MenuItem as item
import pystray
from PIL import Image
import base64
from io import BytesIO
import time
import sys
import serial.tools.list_ports

bytes_img_off = 'iVBORw0KGgoAAAANSUhEUgAAAD8AAAA/CAMAAABggeDtAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAsSAAALEgHS3X78AAAAFnRFWHRDcmVhdGlvbiBUaW1lADAyLzE2LzIyTXGDiwAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTNui8sowAAAHmUExURf///2NocXp+hX6CiX+DioCDiISEhIWFhYaGhoiIiImJiYmJiomKioqKiouMjIyMjI2NjY6Ojo+QkJCQkJKTk5KVmpOTk5OTlJOUlZSUlZSVlpWWl5aWlpaXmJaZnZeYmZiYmJiZmpianJicoZucnZ2foZ2go56enp6fn5+fn5+goKGhoaGioqGjpaKjo6KjpaSlpaSmqKWnqaipqqiqrKiqrqmpqamrrautrautr6ysrK6vr66wsa6xta+xs7Cys7CytLGzs7GztbOZe7O1t7SUZbSVZrSdgrS1trS2uLW1tbW2trW3uba4u7e3t7e4uLe5ure5u7ihfbi4uLi6vLi6vbmfcLmif7m5ubm6u7m6vLm7vbm7vrqgcrqohbq6urq8v7u8vru9vbu9v7y+v76/wL7Awb+ugb+/v7/BwcDBwsGugMG/usHCw8HCxMHDxMHDxcHDxsLCwsLDxMPFxsTFxsXHyMfJysjIyMjKzMnKy8nLzMnMzcvNzszMzMzOz83P0M7Ozs/R0tDS09DS1NHT1NLS0tLU1dPV1tPW19TW19jY2NyXQuWxauaybOazbea0bui6guu6auy7auy8be2+bO3HjO6uP++vP/HHhfK0P/LJiPO1P//EPf/Za//nsv/vtf/72wOF3OIAAAABdFJOUwBA5thmAAACbElEQVRIx+3U+VsSQRjA8Un0leiwtcM7s+yisms73YoyNQstSrqzuzSkMlMiMww1bKLDLu20/tPeYQGR3Rlm4eHpl74/Lcz7Gdh99hlCWD9ZM+xqMipsks3MxMZJSrn7H1NTX3X/9gu397r/Pj39zeCj0bh/84fbu7iPRgX+w29un2T8x1/cPv/3Bt+H9fp8V1paTrPLptauu9y6WpvYzLnm5rM+Xy+77CPzcupAwhcWFhYULF+T1i5sXVori4psNlvSE3IGGigdVNUyaKQSNUKZqg5S2gBX9SeQ8OWyvlzgb2VI4CuY37Fa2HbmK8x9payvzODXcpLx2hZhmsBXyfqqPPo2l7A2ga9h3rVH2CHma7L3B/Poa5m/5Ha7L/LCJeZrBf6mR9j1PPo65h967gjy3Ge+zuD9/guaVg8nKJ0YuCdoYILSk1Cvaad6elJ8shCl4/183j9O6cjstNEvwoGwn8f9YUojiw0+0YtigBW4wViQ0xjyaoDi58S817jnBrzD0WemjVL6ajOOvCS8nuDqTjwiw2Yc/zzdiwOPCL/zuH6YbTBsiPFjuHyciNqPEzd4J/dtXNxNxG3CmQfm/DEurSeZWoVTG7eZ5MSFapK5pQB2h97CJdiC+Ac7gEJkckDpMpNKwSHFSQc4zW7fCR1yvpvnu+V9SN03JzVk1adl0QePpBW05oeupTVk3V9OZt3n+PyfmmTBc5L1iqKU4FmYEkAJfinpYwFEZm89AkAsxnwkXrbepb96rn/l24/Gas/We/VX15udDwQ6vbE6A4Fs/NysekXRT835mMOhKMRydhjGVwef/1bRr/8FWjRZqLcQQBkAAAAASUVORK5CYII='
bytes_img_on = 'iVBORw0KGgoAAAANSUhEUgAAAD8AAAA/CAYAAABXXxDfAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAK6wAACusBgosNWgAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTNui8sowAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDIvMTYvMjJNcYOLAAAEEklEQVRoge2aTWsTURSG30maqLW1VWjFiiIUUhEKNn4URKXTgm4CQv+C0iCSVXAhFBduJRuDlAj+gS6yKqWrjuKmaGihiqTBIFRorSVqk9A0qe24mGYyyUwyk9wzU+PkWWVuZs49773nzpz7wYmCABWup6KqrP8xEO/klEUbu+/EbPKN+nkL6OgfwWnXrTJ/cDEjIvlcffPuM05dCDhM8axJaKv1Z3bLgd289Nvp/IgTuKF5X/vZSzjSc4HaN03yqVVsf/uk+V9m9TP2NqX+dLqAzu79mrZqigeAnxtOAEDPmer3iOI+Tl29p2eKhPW5FzX/T32X/O09t6drS1e8EdzHAGQTFKYM1bVNZItEPMcB+DFLYUq/Lofmu6shbP3Ca4m3K7YW3wZAlc3ldp7gQ/o98uk0CvtZAMCXxA7uni+/t130IuYG3CknXJk/lji8W2hDwd0L8WsePk+5P470IOJ7SQBAcvM4jha6AQC3T6o1AgA3oSH+f+fa2BgeTE7W/tR5NMrcL18h8GiCrXZPheUEW44wFXmNh/77qnK/znOcYmIjhngeQQCIREpOzsxIv0MhhAAEBYHZWXI8Hsi+B4NSmc9X8tPvL/kOyImC7V94jVMZvlbDGIHs6W1xWFiNz8dswtZhb2vx7GEfChG40QCtsGfD1uLZw15r9bdJYBfP8wRuNABBozdv2BM0evOKJ4At7P3+w09xGbB1z9taPFvYRyJS6A8MELljkJUVqW7GWZ12z3s86rF88GmZzeVKZYmE9cIBqU6F8Ln8wYZi5edPS4cC1UqOEVSrOVZPaxV5/eL1YQhDlw09RrKSo2okgkmGYSrq8v7+1bApTvNwggZLXV3ivNcrX2uu5Zn92dOoT9kRI7EYrmQyhjfzDPf80NYW54vH5esQz5OvwtZER/id5eW6hAN1hv3A+jp3c2FBvrasAXSEBwUBg6lU3du3dY/54VyOCyqGiukNYEA4FC+xejA85jUQVU6YvZ5PKBxgy/D0I4ASYuEAW88XKY8AVmtVUK4UUggHaMQDigYYDQR0bx4aHy+7XopGdZ+ZD4cB0AkHiM7kQHJGBNTCjGD0mYMGIDuUQyUeQUEojclslsqsREeHXAclZOLLWFujs9XXR2erAnPEF2H99JmcLtt6McPW4s0Ne9aprskZY6vnTeNfO7tTgTniCd/SBY6DWzTntBy5+KVoVE5FqRgNBDAfDjeUPdaCKrcHALFy/4z12IJqkkSY1wO0Pc+plo55XgTqT0vlNFkQ6A7Xa9B621tGIlF9jd/ns3zTs9XzlmLlBocO1ov3VzkLXTzsbCHWiz8EkdWwRLzRDVCroUxytBABYDEahVBH1qfIC0z9zpvd8xwACOGwoWTn7dQUYtPT8nNm8xeG7FACGeluQAAAAABJRU5ErkJggg=='

img_on = Image.open(BytesIO(base64.b64decode(bytes_img_on)))
img_off = Image.open(BytesIO(base64.b64decode(bytes_img_off)))

def exit_action(icon):
    icon.visible = False
    icon.stop()
    sys.exit(0)
        
def main_action(icon):
    ports_aval = set()
    while True:
        icon.visible = True
        ports = serial.tools.list_ports.comports()        
        menu_itens = []
        if len(ports):
            for port, desc, hwid in sorted(ports):
                menu_itens.append(item('{}: {}'.format(port, desc), None))
                if not port in ports_aval:
                    icon.notify('{}: {}'.format(port, desc))
                ports_aval.add(port)
            icon.icon = img_on
        else:
            ports_aval = set()
            menu_itens.append(item('Nenhum dispositivo detectado!', None))
            icon.icon = img_off
        menu_itens.append(Menu.SEPARATOR)
        menu_itens.append(item('Sair', lambda : exit_action(icon)))
        icon.menu = tuple(menu_itens)        
        time.sleep(5)

menu = (item('Nenhum dispositivo detectado!', None), Menu.SEPARATOR, item('Sair', lambda : exit_action(icon)))
icon = pystray.Icon(name='name', icon=img_off, title='Portas Seriais', menu=menu)
icon.run()

if __name__ == '__main__':
    main_action(icon)
