from tkinter import *
import datetime

class Runner_Conversion_Calculator(Frame):
    '''Models conversion calculator that converts distance, speed and pace units, commonly used by road runners'''
    def __init__(self, master):
        Frame.__init__(self, master)

        # dict that holds conversion types and respective base unit options
        self.conversion_options = {
            'Distance': ['mi', 'km'],
            'Speed': ['mph', 'kph'],
            'Pace': ['min/mile', 'min/km']
        }

        # create all screen elements for the application
        self.create_screen_elements()
        # make all widgets take focus when you click on them
        master.bind_all("<Button-1>", lambda event: event.widget.focus_set())


# screen elements creation
    def create_screen_elements(self):
        '''Creates all elements present in the screen for the application'''
        # conversion tyoe radiobutton selection
        # variable to hold on to the selected state of conversion type
        self.conversion_type_state = StringVar(self)
        # create a radiobutton selection for each key in conversion_options
        grid_column = 0
        for type in self.conversion_options.keys():
            type_option = Radiobutton(self, text=type, variable=self.conversion_type_state, value=type.lower())
            type_option.grid(row=0, column=grid_column)
            grid_column += 1


        # base unit dropdown selection
        # variable to hold on to the selected state of base unit
        self.base_unit_state = StringVar(self)
        # create a selection for the base unit
        self.base_unit_options = OptionMenu(self, self.base_unit_state, '')
        self.base_unit_options.grid(row=1, column=1)


        # base value input
        self.user_input = Entry(self, width=10)
        self.user_input.bind("<FocusIn>", self.focus_in_input)
        self.user_input.bind("<FocusOut>", self.focus_out_input)
        self.user_input.grid(row=1, column=0)


        # calculate button
        self.calculate_button = Button(self, text="Calculate")
        self.calculate_button.grid(row=1, column=2)


        # result label
        self.result = StringVar(self, '')
        self.result_target_unit = StringVar(self)
        self.result_label = Label(self, text='', font=("Arial", 10, "bold"))
        self.result_label.grid(row=1,column=3)


        # trace when conversion_type_state is written and run callbacks to:
        # update base unit options
        self.conversion_type_state.trace('w', self.update_unit_options)
        # update entry placeholder
        self.conversion_type_state.trace('w', self.update_input_placeholder)
        # define button command
        self.conversion_type_state.trace('w', self.define_button_command)

        # trace when base_unit_state is written and run a callback to update the target unit 
        self.base_unit_state.trace('w', self.set_target_unit)
    
        # set default radio button selection option
        self.conversion_type_state.set('distance')
        # add all components to the screen
        self.pack()


# screen elements management
    def update_unit_options(self, *args):
        '''Updates all items in the base unit dropdown selection based on current radio button selection for conversion type.'''
        # get all units from conversion_options dictionary where the key matches the conversion type selected
        units = self.conversion_options[self.conversion_type_state.get().capitalize()]
        # select the first item in the list of units by default -> base_unit_state
        self.base_unit_state.set(units[0])
        # sets the second item as target unit by default
        self.result_target_unit.set(units[1])

        # get access to base_data_unit_options 
        menu = self.base_unit_options['menu']
        # delete all data from previous conversion type selection
        menu.delete(0, 'end')
        # add new units with the respective labels and attached commands to set base_unit_state as current selected unit 
        for unit in units:
            menu.add_command(label=unit, command=lambda base_unit=unit: self.base_unit_state.set(base_unit))



    def set_target_unit(self, *args):
        '''Sets the pair of the current base unit selected as the target unit'''
        units = self.conversion_options[self.conversion_type_state.get().capitalize()]
        target = [unit for unit in units if unit != self.base_unit_state.get()]
        self.result_target_unit.set(target[0])



    def update_input_placeholder(self, *args):
        '''Based on conversion type selected, sets a text in the input with the expected format.'''
        if self.conversion_type_state.get() == 'pace':
            # delete current placeholder from previous conversion type selection
            self.user_input.delete(0, 'end')
            # insert new placeholder in the correct format
            self.user_input.insert(0,'00:00')
        else:
            self.user_input.delete(0, 'end')
            self.user_input.insert(0,'0.00')


    
    def focus_in_input(self, *args):
        '''Remove placeholder from entry when user focus in'''
        if self.user_input.get() == '0.00' or self.user_input.get() == '00:00':
            self.user_input.delete(0, 'end')

        
            
    def focus_out_input(self, *args):
        '''Adds placeholder from entry when user focus out without entering data in the input'''
        if not self.user_input.get():
            self.update_input_placeholder()

    
    
    def define_button_command(self, *args):
        '''Based on conversion type selected, defines calculation to be performed when button is clicked.'''
        if self.conversion_type_state.get() == 'pace':
            self.calculate_button.config(command = self.pace_converter)
        else:
            self.calculate_button.config(command = self.distance_speed_converter)



    def display_result(self):
        '''Puts together a string with the result and sets it as text attribute for the result_label'''
        input_value = self.user_input.get()
        base_unit = self.base_unit_state.get()
        result_value = self.result.get()
        target_unit = self.result_target_unit.get()
        self.result_label.config(text=f'{input_value}{base_unit.lower()} equals to {result_value}{target_unit.lower()}')
        
        
#conversion calculation formulas
    def distance_speed_converter(self):
        '''Converts inputted distance or speed from base unit selected in the dropdown menu to its target pair'''
        try:
            if self.base_unit_state.get() == 'mi' or self.base_unit_state.get() == 'mph':
                self.result.set(str(round((float(self.user_input.get()) * 1.6093), 2)))
            elif self.base_unit_state.get() == 'km' or self.base_unit_state.get() == 'kph':
                self.result.set(str(round((float(self.user_input.get()) * 0.6214), 2)))

            self.display_result()

        except:
            self.result_label.config(text='Invalid input format. Please enter a valid number.')
        


    def pace_converter(self):
        '''Converts inputted pace from unit selected in the dropdown menu to its target pair'''
        try:
            min, sec = self.user_input.get().split(':')
            total_seconds = (int(min) * 60) + int(sec)

            if self.base_unit_state.get() == 'min/mile':
                total_seconds *= 0.6214  
            elif self.base_unit_state.get() == 'min/km':
                total_seconds *= 1.6093

            self.result.set(str(datetime.timedelta(seconds=int(total_seconds)))[-5:])
            self.display_result()
       
        except:
            self.result_label.config(text='Invalid input format. Please enter input in format MM:SS')
