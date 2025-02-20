import os
import requests
import zipfile
import io
import curses
from tqdm import tqdm
from datetime import datetime
from rpi_bootloader_tool.modules import bootloader_builder
from rpi_bootloader_tool.modules import eeprom_builder


def get_bootloader(stdscr):
    stdscr.clear()
    stdscr.addstr(2, 2, "Downloading Bootloader...")
    stdscr.refresh()
    bootloader_builder.build_bootloader()  # Aufruf der Bootloader-Funktion
    stdscr.addstr(4, 2, "Bootloader successfully built!")
    stdscr.refresh()
    stdscr.getch()

def get_eeprom(stdscr):
    stdscr.clear()
    stdscr.addstr(2, 2, "Downloading EEPROM...")
    stdscr.refresh()
    eeprom_builder.build_eeprom()  # Aufruf der EEPROM-Funktion
    stdscr.addstr(4, 2, "EEPROM successfully built!")
    stdscr.refresh()
    stdscr.getch()

def update(stdscr):
    stdscr.clear()
    stdscr.addstr(2, 2, "Checking for updates...")
    stdscr.refresh()
    stdscr.getch()

def about(stdscr):
    stdscr.clear()
    stdscr.addstr(2, 2, "Raspberry Pi Bootloader - Download Utility\nVersion 1.0\nDeveloped by You")
    stdscr.refresh()
    stdscr.getch()

def help_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(2, 2, "Help Section\nUse arrow keys to navigate and Enter to select.")
    stdscr.refresh()
    stdscr.getch()

def draw_menu(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    
    menu = ["Get Bootloader", "Get EEPROM", "Update", "About", "Help", "Exit"]
    title = "Raspberry Pi Bootloader - Download Utility"
    current_row = 0
    
    # Anzahl der Spalten (3 pro Zeile)
    columns = 3
    h, w = stdscr.getmaxyx()  # Höhe und Breite des Fensters
    menu_width = w // columns  # Berechnet die Breite jedes Menüabschnitts

    while True:
        stdscr.clear()
        
        # Titel zentrieren
        stdscr.addstr(1, (w // 2) - (len(title) // 2), title, curses.A_BOLD | curses.A_UNDERLINE)
        
        # Menüeinträge in 3 Spalten anordnen
        for idx, row in enumerate(menu):
            # Berechne die Zeile (y) und Spalte (x) basierend auf dem Index
            x = (w // columns) * (idx % columns) + (menu_width // 2) - (len(row) // 2)
            y = 3 + (idx // columns)
            
            # Markiere die aktuelle Auswahl
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == 10:  # Enter key
            if menu[current_row] == "Exit":
                break
            elif menu[current_row] == "Get Bootloader":
                get_bootloader(stdscr)
            elif menu[current_row] == "Get EEPROM":
                get_eeprom(stdscr)
            elif menu[current_row] == "Update":
                update(stdscr)
            elif menu[current_row] == "About":
                about(stdscr)
            elif menu[current_row] == "Help":
                help_menu(stdscr)
    
    stdscr.clear()
    stdscr.refresh()
    

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()