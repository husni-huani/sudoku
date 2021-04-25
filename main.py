from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from class_sudoku import board_to_num
from sudoku_web import solve_web
from time import sleep


browser = webdriver.Chrome('chromedriver')
browser.get('https://sudoku.com/')
sleep(5)
while True:
    solve_web(browser)

    input()

