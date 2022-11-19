import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

    first_name = ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disabled = True
    page.add(c)

ft.app(target=main)