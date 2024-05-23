from Gauss import main_gauss
from calculadora import main_calcu
import flet as ft



def main(page: ft.Page):
    def cal(event):
        page.clean()
        page.add(btn_r)
        main_calcu(page)
    def gaus(event):
        page.clean()
        page.add(btn_r)
        main_gauss(page)
    
    def regresar(event):
        page.clean()
        page.add(btn_r, fila_boton_click , fila_boton_click2)    
    
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    click = ft.ElevatedButton(text='Conversiones', on_click=cal)
    fila_boton_click = ft.Row([click])
    fila_boton_click.alignment = 'center'
    
    click2 = ft.ElevatedButton(text='Gauss Seidel', on_click=gaus)
    fila_boton_click2 = ft.Row([click2])
    fila_boton_click2.alignment = 'center'
    
    btn_regresar = ft.ElevatedButton(text = 'Regresar', on_click=regresar)
    btn_r = ft.Row([btn_regresar])
    btn_r.alignment = 'start'
    page.add(btn_r, fila_boton_click, ft.Row(alignment=ft.MainAxisAlignment.CENTER, width=70, height=80) , fila_boton_click2)

ft.app(target=main)