from flet import *

def switch_page(page: Page):
    pass

def main(page: Page):

    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'

    buttons = Column(
        controls=[
            FilledButton(text='Cash In', width=125, height=50),
            FilledButton(text='Cash Out', width=125, height=50),
            FilledButton(text='View', width=125, height=50),
        ],
        alignment=MainAxisAlignment.CENTER,
    )
    container = Container(
        width='90vw',
        height=750, 
        bgcolor=BG,
        border_radius=35,
        alignment=alignment.center,
        content = Container(
            Container(buttons),
        )
    )

    page.add(container)

app(target=main)
