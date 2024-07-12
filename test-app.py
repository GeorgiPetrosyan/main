import flet as ft


def main(page: ft.Page):

    page.title = "Test app"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    user_ip = page.client_ip
    result_text = ft.Text()

    def button_click(event):
        result_text.value = f"Here is your IP address: {user_ip}"
        page.update()

    button = ft.ElevatedButton(text="Get your IP", on_click=button_click)

    page.add(
        button,
        result_text
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
