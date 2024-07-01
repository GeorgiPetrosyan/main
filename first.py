import flet as ft
def main(page: ft.Page):
    page.title = "Простое приложение на Flet"

    header = ft.Text("Добро пожаловать в мое простое приложение!", style="headlineLarge")
    input_field = ft.TextField(label="Введите сообщение")
    result_text = ft.Text()


    def on_button_click():
        result_text.value = f"Вы ввели: {input_field.value}"
        page.update()


    submit_button = ft.ElevatedButton(text="Отправить", on_click=on_button_click)


    page.add(
        header,
        input_field,
        submit_button,
        result_text
    )

ft.app(target=main)

# if __name__ == "__main__":
# ft.app(target=main, view=None, port=8888)
