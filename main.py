from flet import *

def switch_page(page: Page):
    pass

def main(page: Page):

    def go_cashIn(e):
        page.route = '/cashIn'

    def go_cashOut(e):
        page.route = '/cashOut'

    def go_view(e):
        page.route = '/view'

    def go_back(e):
        page.route = '/'
        page.views.pop()
        page.update()

    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'

    buttons = Column(
        controls=[
            ElevatedButton(text='Cash In', width=125, height=50, on_click=go_cashIn),
            ElevatedButton(text='Cash Out', width=125, height=50, on_click=go_cashOut),
            ElevatedButton(text='View', width=125, height=50, on_click=go_view),
        ],
        alignment=MainAxisAlignment.CENTER,
    )

    # Initially, create a container with a placeholder content
    container = Container(
        width='90vw',
        height=750,
        bgcolor=BG,
        border_radius=35,
        alignment=alignment.center,
        content=Container(
            buttons,
        )
    )

    page.add(container)

app(target=main)
