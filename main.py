from nicegui import ui
import cli

container = ui.column()

with container:
    ui.label('Are you really bros, bro?').style('font-style: italic')
    ui.separator()

    name1 = ui.input(label='Your name').props('clearable')
    input_name1 = name1.value

    name2 = ui.input(label='Name of the other person').props('clearable')
    input_name2 = name2.value


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

    ui.button('Check', on_click=display_results)
    result = ui.label()
    image = ui.image()

ui.run(title="Are We Bro?", native=True, window_size=(300, 500), fullscreen=False)
