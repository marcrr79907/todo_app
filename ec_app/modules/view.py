import flet as ft
import requests

base_url = 'http://127.0.0.1:8000/tasks/'


class Task(ft.UserControl):
    def __init__(self, task_name, task_status_change, delete_task, id_task):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.delete_task = delete_task
        self.id_task = id_task

    def build(self):

        self.chb_display_task = ft.Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed)
        self.txt_edit_name = ft.TextField(expand=1, autofocus=True)

        self.row_display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.chb_display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip='Edit To-Do',
                            on_click=self.edit_task
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINE,
                            tooltip='Delete To-Do',
                            on_click=self.delete_clicked
                        )
                    ]
                )
            ]
        )

        self.row_edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.txt_edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip='Update To-Do',
                    on_click=self.save_task
                )
            ]
        )

        return ft.Column(controls=[self.row_display_view, self.row_edit_view])

    def edit_task(self, e):
        self.txt_edit_name.value = self.chb_display_task.label
        self.row_display_view.visible = False
        requests.put(
            base_url+str(self.id_task)+'/',
            data={
                'completed': self.completed,
                'body': self.txt_edit_name.value
            }
        )
        self.row_edit_view.visible = True
        self.update()

    def save_task(self, e):
        self.chb_display_task.label = self.txt_edit_name.value
        requests.put(
            base_url+str(self.id_task)+'/',
            data={
                'completed': self.completed,
                'body': self.txt_edit_name.value
            }
        )
        self.row_display_view.visible = True
        self.row_edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.delete_task(self)

    def status_changed(self, e):
        self.completed = self.chb_display_task.value
        requests.put(
            base_url+str(self.id_task)+'/',
            data={
                'completed': self.completed,
                'body': self.task_name
            }
        ).json()
        self.task_status_change(self)


class TodoApp(ft.UserControl):

    def build(self):
        self.col_tasks = []
        self.txt_new_task = ft.TextField(
            hint_text='Que tarea deseas agregar?', expand=True, autofocus=True)
        self.btn_add_task = ft.FloatingActionButton(
            icon=ft.icons.ADD, on_click=self.add_task_clicked)

        self.col_tasks = ft.Column()
        self.r = requests.get(base_url).json()
        print(len(self.r))
        for i in range(len(self.r)):
            self.col_tasks.controls.append(
                Task(self.r[i]['body'],
                     self.tabs_changed, self.delete_task, id_task=self.r[i]['id'])
            )

        self.tbs_filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text='todas'), ft.Tab(text='activa(s)'),
                  ft.Tab(text='completada(s)')]
        )

        self.txt_items_left = ft.Text('0 tareas pendientes')

        return ft.Column(
            width=600,
            controls=[
                ft.Row([
                    ft.Text(value='Tareas', style='headlineMedium')
                ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        self.txt_new_task,
                        self.btn_add_task
                    ]
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.tbs_filter,
                        self.col_tasks,
                        ft.Divider(),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                self.txt_items_left,
                                ft.OutlinedButton(
                                    icon=ft.icons.CLEANING_SERVICES,
                                    text='Limpiar',
                                    on_click=self.clear_clicked
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def add_task_clicked(self, e):
        task = Task(self.txt_new_task.value,
                    self.tabs_changed, self.delete_task, len(self.r))
        requests.post(
            base_url,
            data={
                'completed': task.completed,
                'body': task.task_name
            }
        ).json()

        self.col_tasks.controls.append(task)
        self.txt_new_task.focus()
        self.txt_new_task.value = ''
        self.update()

    def delete_task(self, task: Task):
        requests.delete(base_url+str(task.id_task))
        self.col_tasks.controls.remove(task)
        self.update()

    def clear_clicked(self, e):
        for task in self.col_tasks.controls[:]:
            if task.completed:
                self.delete_task(task)

    def update(self):
        status = self.tbs_filter.tabs[self.tbs_filter.selected_index].text
        count = 0
        for task in self.col_tasks.controls:
            task.visible = (
                status == 'todas'
                or (status == 'activa(s)' and task.completed == False)
                or (status == 'completada(s)' and task.completed)
            )
            if not task.completed:
                count += 1

        self.txt_items_left.value = f'{count} tarea(s) pendiente(s) '
        super().update()

    def tabs_changed(self, e):
        self.update()
