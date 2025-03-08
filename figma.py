from images_path import images
import pyautogui
from variables import get_variables

light_variables, dark_variables = get_variables()


class Figma:
    def __init__(self) -> None:
        pass

    def click_local_variables_button(self):
        self.locate_and_click("local_variables_btn")

    def click_create_first_variable_button(self):
        self.locate_and_click("init_create_new_variable_btn")

    def click_color_variable_option(self):
        self.locate_and_click("color_variable_option")

    def change_theme_collection(self):
        self.locate_and_click("change_theme_select")
        pyautogui.sleep(0.5)
        pyautogui.click()

    def define_light_theme_variables(self):
        for key, value in light_variables.items():
            pyautogui.write(key)
            pyautogui.press("TAB", 2)
            pyautogui.write(value)
            self.locate_and_click("second_create_new_variable_btn")
            pyautogui.sleep(0.1)
            self.locate_and_click("color_variable_option")
            pyautogui.sleep(0.05)

    def define_dark_theme_variables(self):
        for key, value in dark_variables.items():
            pyautogui.write(key)
            pyautogui.press("TAB", 2)
            pyautogui.write(value)
            self.locate_and_click("second_create_new_variable_btn")
            pyautogui.sleep(0.1)
            self.locate_and_click("color_variable_option")
            pyautogui.sleep(0.05)

    def locate_and_click(self, key: str, right_click=False):
        x, y = pyautogui.locateCenterOnScreen(images[key])  # type: ignore
        if right_click:
            pyautogui.rightClick(x, y)
            return
        pyautogui.click(x, y)

    def start(self):
        pyautogui.alert("The script will start in 2 seconds after you confirm.")  # type: ignore
        pyautogui.sleep(2)
        self.click_local_variables_button()
        pyautogui.sleep(0.1)
        self.click_create_first_variable_button()
        pyautogui.sleep(0.1)
        self.click_color_variable_option()
        pyautogui.sleep(0.1)
        self.define_light_theme_variables()
        pyautogui.sleep(0.1)
        self.change_theme_collection()
        pyautogui.sleep(0.1)
        self.click_create_first_variable_button()
        pyautogui.sleep(0.1)
        self.click_color_variable_option()
        pyautogui.sleep(0.1)
        self.define_dark_theme_variables()
        pyautogui.sleep(0.1)
        self.delete_last_option()
