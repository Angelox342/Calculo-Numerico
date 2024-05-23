import numpy as np
import flet as ft

def rellenar_matriz(n):
    # Genera una matriz n x n con números aleatorios enteros entre 1 y 100
    matriz = np.random.randint(1, 100, size=(n, n))
    # Asegura que la matriz sea diagonalmente dominante
    for i in range(n):
        matriz[i][i] = sum(np.abs(matriz[i])) + 1
    return matriz

def es_diagonalmente_dominante(A):
    # Verifica si la matriz es diagonalmente dominante
    D = np.diag(np.abs(A))  # Diagonal principal
    S = np.sum(np.abs(A), axis=1) - D  # Suma de los valores absolutos de los otros elementos de la fila
    return np.all(D > S)

def main(page: ft.Page):
    page.title = "Resolución de sistemas de ecuaciones"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    txt_name = ft.TextField(label="Your name")
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    page.padding = 50
    
    page.update()

    # Agrega la etiqueta
    page.add(ft.Text("Soluciones Lineales Gauss-Seidel", text_align=ft.TextAlign.CENTER))
   

    
   # Pide al usuario que ingrese el tamaño de la matriz
    
    
    n = int(input("Ingrese el tamaño de la matriz:"))

    page.update()
    matrix_grid = ft.GridView(
        expand=1,
        runs_count=n,  # Ajusta este valor a n para una matriz nxn
        max_extent=100,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    page.add(matrix_grid)

    matrix_rows = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=50))
        matrix_rows.append(row)

    for row in matrix_rows:
        for control in row:
            matrix_grid.controls.append(control)

    def on_click_random(event):
        # Llama a la función rellenar_matriz cuando se hace clic en el botón "Random"
        matriz = rellenar_matriz(n)
        for i, row in enumerate(matrix_rows):
            for j, control in enumerate(row):
                control.value = str(matriz[i][j])
        # Llama a page.update() después de cambiar los valores
        page.update()

    def gauss_seidel_modificado(A, b, max_iter=1000, tol=1e-8):
        n = len(b)
        x = np.zeros_like(b)
        for it in range(max_iter):
            x_prev = x.copy()
            for i in range(n):
                x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x_prev[i + 1:])) / A[i, i]
            if np.linalg.norm(x - x_prev, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tol:
                return x
        return x

    def on_click_solution(event):
        # Crea una matriz A y un vector b a partir de los valores del GridView
        matriz = np.array([float(control.value) for control in matrix_grid.controls]).reshape(n, n).astype(np.float64)
        b = matriz[:, -1]

        # Verifica si la matriz es diagonalmente dominante
        if not es_diagonalmente_dominante(matriz):
            page.add(ft.Text("La matriz no es diagonalmente dominante. El método de Gauss-Seidel puede no converger.", text_align=ft.TextAlign.CENTER))
            return

        # Llama a la función gauss_seidel_modificado
        x = gauss_seidel_modificado(matriz, b)

        # Muestra la solución
        for i, xi in enumerate(x):
            page.add(ft.Text(f"x{i + 1} = {xi}", text_align=ft.TextAlign.CENTER))

        # Llama a page.update() después de agregar los nuevos controles
        page.update()


        

    # Agrega los botones en una fila
    page.add(
        ft.Row(
            [
                ft.ElevatedButton("Random", on_click=on_click_random),
                ft.ElevatedButton("Solución", on_click=on_click_solution),
                ft.ElevatedButton("Ingresar el tamaño de la matriz "),txt_number
                
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.update()

ft.app(main)








