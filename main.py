import curses
import os

menu = ["Image Detection", "Advanced CCTV", "Exit"]

def run_option(option):
    if option == 0:
        os.system("python3 image_detect.py")
    elif option == 1:
        os.system("python3 cctv.py")
    elif option == 2:
        exit()

def draw_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx

        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

    current_row = 0

    while True:
        draw_menu(stdscr, current_row)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_row = (current_row - 1) % len(menu)
        elif key == curses.KEY_DOWN:
            current_row = (current_row + 1) % len(menu)
        elif key == 10:
            run_option(current_row)

curses.wrapper(main)
