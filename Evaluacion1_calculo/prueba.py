import numpy as np
import flet as ft

def rellenar_matriz(n):
    # Genera una matriz n x n con números aleatorios enteros entre 1 y 100
    return np.random.randint(1, 100, size=(n, n))

def main(page: ft.Page):
    page.title = "Resolución de sistemas de ecuaciones"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.padding = 50
    page.update()

    # Agrega la etiqueta
    page.add(ft.Text("Soluciones Lineales Gauss-Seidel", text_align=ft.TextAlign.CENTER))

    matrix_grid = ft.GridView(
        expand=1,
        runs_count=3,  # Ajusta este valor a 3 para una matriz 3x3
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    page.add(matrix_grid)

    for i in range(9):  # Ajusta este valor a 9 para una matriz 3x3
        matrix_grid.controls.append(
            ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=50)  # Centra el texto y reduce el ancho
        )

    def on_click_random(event):
        # Llama a la función rellenar_matriz cuando se hace clic en el botón "Random"
        matriz = rellenar_matriz(3)
        for i in range(9):
            matrix_grid.controls[i].value = str(matriz.flatten()[i])
        # Llama a page.update() después de cambiar los valores
        page.update()

    # Agrega los botones en una fila
    page.add(
        ft.Row(
            [
                ft.ElevatedButton("Random", on_click=on_click_random),  # Implementa la función para rellenar la matriz aleatoriamente
                ft.ElevatedButton("Solución", on_click=None),  # Implementa la función para mostrar la solución
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.update()

ft.app(main)















def gauss_seidel_modificado(A, b, max_iter=1000, tol=1e-8):
    n = len(b)
    x = np.zeros_like(b)
    for it in range(max_iter):
        x_prev = x.copy()
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x_prev[i+1:])) / A[i, i]
        if np.linalg.norm(x - x_prev, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tol:
            return x
    return x



def rellenar_matriz(n):
    # Genera una matriz n x n con números aleatorios
    matriz = np.random.rand(n, n)
    return matriz