from nicegui import ui
import cli


@ui.refreshable
def load_ui():
    # global container, name1, name2, result, image
    container = ui.column()

    with container:
        ui.label('Are you really bros, bro?').style('font-style: italic')
        ui.separator()

        name1 = ui.input(label='Your name').props('clearable')
        name2 = ui.input(label='Name of the other person').props('clearable')

        def display_results():
            with container:
                if name1.value and name2.value:
                    if cli.arewebro(name1.value, name2.value):
                        result.set_text(f"YES, YOU AND {name2.value.upper()} ARE BRO!")
                        result.style('color: Violet; font-weight: bold')
                        image.set_source("i-got-you-bro-fist-bump.gif")
                        image.set_visibility(True)
                    else:
                        result.set_text(f"No, you and {name2.value} are not BRO!")
                        result.style('color: Red; font-weight: normal')
                        image.set_visibility(False)

        with ui.row():
            ui.button('Check', on_click=display_results)
            ui.button('Reset', on_click=load_ui.refresh, color='lightgray')
        result = ui.label()
        image = ui.image()


load_ui()

# reload=false avoid the server kept up when you close the window in Native mode
ui.run(title="Are We Bro?", native=True,
       window_size=(300, 500), reload=False,
       fullscreen=False)
