#!/usr/bin/env python
################################################################################
#                            commbase_tts_pyttsx3.py                           #
#                                                                              #
# Conversational AI Assistant and AI Hub for Computers and Droids              #
#                                                                              #
# Change History                                                               #
# 04/29/2023  Esteban Herrera Original code.                                   #
#                           Add new history entries as needed.                 #
#                                                                              #
#                                                                              #
################################################################################
################################################################################
################################################################################
#                                                                              #
#  Copyright (c) 2022-present Esteban Herrera C.                               #
#  stv.herrera@gmail.com                                                       #
#                                                                              #
#  This program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program; if not, write to the Free Software                 #
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA   #

# commbase_tts_pyttsx3.py
# Utilizes text-to-speech capabilities to read out the content of a file or any
# input text provided.
# Examples:
# shell> cat file.txt | python3.11 commbase_tts_pyttsx3.py
# shell> echo "Hellow World" | python3.11 commbase_tts_pyttsx3.py

# Requirements
import fileinput
import os.path
import pyttsx3


def set_up_text_to_speech():
	"""
	Initializes the text-to-speech engine, retrieves the available voices, and
	sets properties for the engine's rate and voice.
	"""
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('rate', 145)
	engine.setProperty('voice', voices[18].id)  # TODO: Add to the file INSTALL
	return engine, voices


def talk(text):
	"""
	Sets up the text-to-speech engine, utilizes it to speak out the provided text,
	and ensures the speech synthesis is completed before proceeding.
	"""
	# Assign the values returned by set_up_text_to_speech()
	engine, voices = set_up_text_to_speech()

	engine.say(text)
	engine.runAndWait()


def read_file(file_path):
	"""
	Attempts to read the contents of the specified file, handles potential errors
	such as file not found or IO errors, and returns the file's content if it is
	successfully read.
	"""
	try:
		with open(file_path, 'r') as file:
			content = file.read()
			return content
	except FileNotFoundError:
		print("File not found!")
		return None
	except IOError:
		print("An error occurred while reading the file!")
		return None

"""
def main():
	for voice in voices:
		print(voice)
"""


def main():
	"""
	Serves as the entry point of the program.
	This function is responsible for reading input text from either a file or
	standard input, storing it in the file_content variable, and then passing it
	to the talk() function for speech synthesis. If no input text is provided, it
	displays an appropriate message.
	"""
	file_content = ''
	for line in fileinput.input():
		file_content += line

	if file_content:
		talk(file_content)
	else:
		print("No input text provided.")


# Ensure that the main() function is executed only when the script is run
# directly as the main program.
if __name__ == '__main__':
	main()
