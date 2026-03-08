
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import Driver
import time
import json
from selenium.webdriver.common.keys import Keys


def upload_video(path_to_file,description,cookies_list,proxy):
    driver = Driver(uc=True, incognito=True, proxy=proxy)
    driver.get("https://www.tiktok.com/tiktokstudio/upload")
    for cookie in cookies_list:
        driver.add_cookie(cookie)
    driver.refresh()
    driver.maximize_window()
    driver.get("https://www.tiktok.com/tiktokstudio/upload")
    driver.wait_for_element_present("input[type='file']")
    # abc = input('Нажмите энтер когда все прогрузится')
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(path_to_file)
    driver.wait_for_element_present("div[contenteditable='true']")
    description_element = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true']")
    # description_element.send_keys(Keys.CONTROL + "a")  # Выделяем весь текст
    # description_element.send_keys(Keys.BACKSPACE)      # Удаляем выделенный текст
    description_element.click()
    driver.execute_script("arguments[0].innerHTML = '';", description_element)
    # (Опционально) Вводим новый текст
    description_element.send_keys(description)
    # description_element.send_keys(Keys.ENTER)
    try:
        # Ожидаем, пока кнопка станет кликабельной
        button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-e2e="post_video_button"]'))
        )

        # Нажимаем на кнопку
        button.click()
        print("Кнопка успешно нажата!")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        # Закрываем драйвер
        time.sleep(2200)
        driver.quit()


description = "Описание"
with open("cookies_0.txt", 'r', encoding='utf-8') as file:
    cookies_list = json.load(file)
path_to_file = "Как избавиться от старого телевизора.mp4"
proxy = "USER:PASSWORD@IP:PORT" 

upload_video(path_to_file,description,cookies_list,proxy)