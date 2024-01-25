from flet import *

def main(page: Page):
    page.theme_mode = ThemeMode.LIGHT
    page.title = "Gcash Inventory"
    BG = '#041955'

    def go_cashIn(e):
        page.route = '/cashIn'

        # Create a new container with the content for the 'Cash In' page
        new_container = Container(
            width='90vw',
            bgcolor=BG,
            border_radius=35,
            alignment=alignment.center,
            content=Container(
                Stack(
                    height=750,
                    controls=[
                        Text("Cash In", size=40, color='white', weight=FontWeight.BOLD),
                        Container(
                            top=100,
                            alignment=alignment.center,
                            content=TextField(label="Amount", border="underline", filled=True, hint_text="Enter amount"),
                        ),
                        Container(
                            top=200,
                            alignment=alignment.center,
                            content=TextField(label="Fee", border="underline", filled=True, hint_text="Enter amount"),
                        ),
                        ElevatedButton("Save", width=125, height=50, top=300),
                        ElevatedButton("Go Back", width=125, height=50, top=600, on_click=go_back),
                    ],
                ),
            width=700,
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
            bgcolor=BG,
            border_radius=35,
            alignment=alignment.center,
            content=Container(
                Stack(
                    height=750,
                    controls=[
                        Text("Cash Out", size=40, color='white', weight=FontWeight.BOLD),
                        Container(
                            top=100,
                            alignment=alignment.center,
                            content=TextField(label="Amount", border="underline", filled=True, hint_text="Enter amount"),
                        ),
                        Container(
                            top=200,
                            alignment=alignment.center,
                            content=TextField(label="Fee", border="underline", filled=True, hint_text="Enter amount"),
                        ),
                        ElevatedButton("Save", width=125, height=50, top=300),
                        ElevatedButton("Go Back", width=125, height=50, top=600, on_click=go_back),
                    ],
                ),
            width=700,
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
        height=700,
        bgcolor=BG,
        border_radius=35,
        alignment=alignment.center,
        content=Container(
            buttons,
        )
    )

    page.add(container)

app(target=main)
