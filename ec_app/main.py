import flet as ft
from modules.view import TodoApp

txf = ft.TextField(hint_text='Say something')


def main(page: ft.Page):

    page.title = 'To Do App'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()

    page.add(
        todo
    )


ft.app(main)
