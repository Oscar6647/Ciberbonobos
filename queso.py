from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import chess

driver = webdriver.Firefox(executable_path= r"C:\Users\maxpr\Downloads\geckodriver-v0.29.1-win64(1)\geckodriver.exe")
#driver = webdriver.Firefox(executable_path="/home/famdjg/Descargas/geckodriver")
board = chess.Board()
url = "https://lichess.org/2Se9AqUy"
#url = input("Url: ")
driver.get(url)
i = 0
action = ActionChains(driver)
desplazamiento = 60


def mover():
    pieza_mover = input("Pieza a mover")
    piezas_pawn = driver.find_elements_by_xpath("//piece[@class = 'white pawn']")
    piezas_bishop = driver.find_elements_by_xpath("//piece[@class = 'white bishop']")
    piezas_rook_w = driver.find_elements_by_xpath("//piece[@class = 'white rook']")
    piezas_rook_b = driver.find_elements_by_xpath("//piece[@class = 'black rook']")
    piezas_knight = driver.find_elements_by_xpath("//piece[@class = 'white knight']")
    print(piezas_pawn[0].location)
    print(piezas_pawn[1].location)
    print(piezas_pawn[2].location)
    print(piezas_rook_w[0].location)
    print(piezas_rook_b[1].location)
    print(piezas_pawn)
    driver.implicitly_wait(10)
    movimientos = []
    if pieza_mover == "peon":
        action.drag_and_drop_by_offset(piezas_pawn[0],0,-desplazamiento).perform()

mover()

while i == 1:
    elem = driver.find_elements_by_xpath("//l4x")
    driver.implicitly_wait(10)
    movimientos = []

    for value in elem:
        movimientos.append(value.text)
        print(value.text)