from flet import *

def switch_page(page: Page):
    pass

def main(page: Page):

    def go_cashIn(e):
        page.route = '/cashIn'

        # Create a new container with the content for the 'Cash In' page
        new_container = Container(
            width='90vw',
            height=750,
            bgcolor=FWG,  # Use FWG instead of FG
            border_radius=35,
            alignment=alignment.center,
            content=Container(
                Stack(
                    width='90vw',
                    height=750,
                    controls=[

                        Text("Cash In", size=40, color='white', weight=FontWeight.BOLD),
                        ElevatedButton("Go Back", width=125, height=50, top=600, on_click=go_back),
                    ],
                ),
                alignment=alignment.center,
                height=750,
            ),
        )

        # Append the new container to the existing views
        page.views.append(new_container)
        page.update()

    def go_cashOut(e):
        page.route = '/cashOut'

        # Create a new container with the content for the 'Cash In' page
        new_container = Container(
            width='90vw',
            height=750,
            bgcolor=FWG,  # Use FWG instead of FG
            border_radius=35,
            alignment=alignment.center,
            content=Container(
                Stack(
                    width='90vw',
                    height=750,
                    controls=[

                        Text("Cash Out", size=40, color='white', weight=FontWeight.BOLD),
                        ElevatedButton("Go Back", width=125, height=50, top=600, on_click=go_back),
                    ],
                ),
                alignment=alignment.center,
                height=750,
            ),
        )

        # Append the new container to the existing views
        page.views.append(new_container)
        page.update()

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
