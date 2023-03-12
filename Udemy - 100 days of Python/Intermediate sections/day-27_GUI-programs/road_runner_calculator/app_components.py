from tkinter import *
import datetime

class App_Components(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # dict that holds conversion types and respective base unit options
        self.conversion_options = {
            'Distance': ['Miles', 'Kilometers'],
            'Speed': ['mph', 'kmh'],
            'Pace': ['min/mile', 'min/km']
        }

        # TODO: create a radiobutton selection for the conversion types options (distance = default selection, speed or pace)
        # variable to hold on to the selected state of conversion type
        self.conversion_type_state = StringVar(self)
        # trace when conversion_type_state is written and run a callback to update base unit options 
        self.conversion_type_state.trace('w', self.update_unit_options)
        # create a radiobutton selection for each key in conversion_options
        grid_column = 0
        for type in self.conversion_options.keys():
            type_option = Radiobutton(self, text=type, variable=self.conversion_type_state, value=type.lower())
            type_option.grid(row=0, column=grid_column)
            grid_column += 1

        # TODO: create a selection for the base unit that changes its options based on conversion type selecion
        # variable to hold on to the selected state of base unit
        self.base_unit_state = StringVar(self)
        # create a selection for the base unit
        self.base_unit_options = OptionMenu(self, self.base_unit_state, '')
        self.base_unit_options.grid(row=1, column=1)

        # TODO: create input for base value to be converted
        self.user_input = Entry(self, width=10)
        self.user_input.grid(row=1, column=0)

       
        # set default radio option
        self.conversion_type_state.set('distance')
        # add all components to the screen
        self.pack()

    def update_unit_options(self, *args):
        '''Updates all items in the base unit dropdown selection based on current radio button selection for conversion type'''
        units = self.conversion_options[self.conversion_type_state.get().capitalize()]
        self.base_unit_state.set(units[0])

        menu = self.base_unit_options['menu']
        menu.delete(0, 'end')

        for unit in units:
            menu.add_command(label=unit, command=lambda base_unit=unit: self.base_unit_state.set(base_unit))

    
    # TODO: implement conversion calculation formulas
    
    def distance_speed_converter(self):
        '''Converts inputted distance or speed from unit selected in the dropdown menu to its pair, and return the result'''
        if self.base_unit_state == 'miles' or self.base_unit_state == 'mph':
            result = float(self.user_input.get()) * 1.6093

        elif self.base_unit_state == 'kilometers' or self.base_unit_state == 'kph':
            result = float(self.user_input.get()) * 0.6214
        
        return result

    def pace_converter(self):
        '''Converts inputted pace from unit selected in the dropdown menu to its pair, and returns the result'''
        min, sec = self.user_input.get().split(':')
        total_seconds = (int(min) * 60) + int(sec)

        if self.base_unit_state == 'min/miles':
            total_seconds *= 0.6214
        
        elif self.base_unit_state == 'min/km':
            total_seconds *= 1.6093

        result = str(datetime.timedelta(seconds=int(total_seconds)))[-5:]

        return result