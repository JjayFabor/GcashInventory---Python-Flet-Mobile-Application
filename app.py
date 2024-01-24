from flet import *

def main(page: Page):

    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'

    cash_in = Row(
        controls=[
            FilledButton(text='Cash In', width=125, height=50),
            FilledButton(text='Cash Out', width=125, height=50),
        ],
        alignment=MainAxisAlignment.CENTER,
    )
    container = Container(
        width=400,
        height=850, 
        bgcolor=BG,
        border_radius=35,
        alignment=alignment.center,

        content=Stack(
            controls=[
                cash_in,
            ],
        )
    )

    page.add(container)

app(target=main)
