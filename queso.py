from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import chess

driver = webdriver.Firefox(executable_path="/home/famdjg/Descargas/geckodriver")
board = chess.Board()
url = input("Url: ")
driver.get(url)
i = 0
action = ActionChains(driver)
desplazamiento = 60

def mover():
    pieza_mover = input("Pieza a mover")
    piezas = driver.find_elements_by_xpath("//piece[@class = 'white pawn']")
    print(piezas)
    driver.implicitly_wait(10)
    movimientos = []
    if pieza_mover == "peon":
        action.drag_and_drop_by_offset(piezas[3],0,-desplazamiento).perform()

mover()

while i == 1:
    elem = driver.find_elements_by_xpath("//l4x")
    driver.implicitly_wait(10)
    movimientos = []

    for value in elem:
        movimientos.append(value.text)
        print(value.text)