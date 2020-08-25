
Keyboard environment
The keyboard environment is used to simulate different keyboard. The environment is developed with the goal of functioning as reinforcement learning environment.
Therefore, actions and results are accessible from the outside API. The environmen can function as standalone API, standalone interface, or a combination of both. 

## Installation
The keyboard environment is based on Python and Kivy. All required libraries are listed below as well as in the requirements file.
````
kivy
events
````
The requirements can be installed using the following command:
````
pip install -r requirements
````

## Configuration
The environment can be configured from the `./config.py` file. Optionally, keyboards can be configured using JSON files. These allow for more complete configuration of the keyboard.

### `config.py`
The config file contains config about the environment and keyboard. Configuring a keyboard from this file is possible, however, not recommend as actions, position, and style cannot be configured. An invalid or incomplete config will most likely cause errors or crashes to the environment.

``KEYBOARD_PATH`` Keyboard directory path.

``KEYBOARD_NAME`` Name of keyboard config.

``COLUMN_COUNT`` Number of action cell columns.

``ROW_COUNT`` Number of action cell rows.

``KEYBOARD_WIDTH`` Width of keyboard in pixels.

``KEYBOARD_HEIGHT`` Height of keyboard in pixels.

``ENABLE_CLI`` Toggle CLI in `GRAPHIC` mode.

``CLI_HEIGHT`` Height of CLI in `GRAPHIC` mode in pixels.

``APPLICATION_MODE`` Sets the application mode if not specified as run argument.

``SYMBOLS`` Array of symbols available on the keyboard. _(Overwritten by JSON config)_.

``ACTION_TYPES`` Button action types (e.g. click or hold) defined by `ActionTypes`. _(Overwritten by JSON config)_

``BUTTON_WIDTH`` Width of a button in pixels. _(Overwritten by JSON config)_

``BUTTON_HEIGHT`` Height of a button in pixels. _(Overwritten by JSON config)_

### Keyboard configs
The JSON configuration of a keyboard is a bit more complicated but it allows for more customization such as button handlers. It can be used to style the keyboard or to simulate custom button actions like the `SHIFT` button for example. An example keyboard config can be found in `./keyboard/default.json`. 

__keyboard__
 - <b id="#/properties/name">name</b> `required`
	 - _Keyboard name_
	 - Type: `string`
 - <b id="#/properties/width">width</b>
	 - _Keyboard width_
	 - Type: `integer`
 - <b id="#/properties/height">height</b>
	 - _Keyboard height_
	 - Type: `integer`
 - <b id="#/properties/defaults">defaults</b>
	 - _Default button configuration_
	 - Type: `object`
	 - **_Properties_**
		 - <b id="#/properties/defaults/properties/button_width">button_width</b> `required`
			 - _Button width_
			 - Type: `integer`
		 - <b id="#/properties/defaults/properties/button_height">button_height</b> `required`
			 - _Button height_
			 - Type: `integer`
		 - <b id="#/properties/defaults/properties/handlers">handlers</b> `required`
			 - _Button action handlers. Defines what happens on a button action (e.g. click or hold)._
			 - Type: `object`
			 - **_Properties_**
				 - <b id="#/properties/defaults/properties/handlers/properties/on_click">on_click</b>
					 - Type: `object`
					 - **_Properties_**
						 - <b id="#/properties/defaults/properties/handlers/properties/on_click/properties/name">name</b> `required`
							 - _Name of the action handlers (e.g. ValueAppendHandler)_
							 - Type: `string`
 - <b id="#/properties/buttons">buttons</b>
	 - _Buttons in the keyboard._
	 - Type: `array`

## Usage
The keyboard environment can be used in various standalone way, but it can also be used from a jupyter notebook.
The standalone version can be executed from using the following command, make sure all requirements are installed:

``python -m keyboard_environment.main {runmode}``

There are four different run modes available:

``API`` cannot be run standalone, as this functions as coding API. There are two main entry points to use: 
    
- `agent` accessible for reinforcement learning goals. Contains state, actions, and can be used to execute actions.
- `keyboard` accessible for keyboard metadata goals. Contains available buttons, all symbols, and sizes.

``GRAPHIC`` a graphical user interface which can be used with the API or CLI.

``CONSOLE`` interactive console interface to test the environment without gui. Same CLI as in GRAPHIC mode.

``DEMO`` used to demo the tool with a user interface.

### Jupyter Notebook
To run graphical mode from a notebook, make sure that you run this code before importing the library:

````
from threading import Thread

def run():
    %run -i -m keyboard_environment.main GRAPHIC

t = Thread(target=run)
t.start()
````

