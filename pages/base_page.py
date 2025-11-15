from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import *
import allure
from selenium.common import TimeoutException



class BasePage:

    def __init__(self, driver):
        self.driver = driver       
    
    @allure.step('Кликнуть на элемент')
    def click_element(self, locator):
        element = self.find_element(locator)   
        element.click()
    
    @allure.step('Найти элемент на странице')
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))        
   
    @allure.step('Найти элементы на странице')
    def find_all_elements(self, locator):
        return self.driver.find_elements(*locator)   

    @allure.step('Ожидание пока элемент станет кликабелен')
    def wait_element_to_be_clickable(self, locator, time=30):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
    
    @allure.step('Ввести текст в input')
    def text_input(self, locator, data):
        element = self.find_element(locator)
        element.send_keys(data)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Ожидание загрузки элемента')
    def wait_element_load(self, locator):
         WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание пока элемент исчезнет')
    def wait_for_element_hidden(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(lambda driver: len(driver.find_elements(*locator)) == 0)
            return True
        except TimeoutException:
            return False
        
    @allure.step('Получение элемента')
    def get_element(self, locator):
        return self.find_element(locator).text  
    
    @allure.title('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
    
    @allure.step("Ожидание исчезновения перекрывающего окна")
    def wait_window_is_hidden(self):
        modals = self.find_all_elements(MainPageLocators.MODAL_BACKDROP)
        for modal in modals:
            WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(modal))       

    @allure.step('Переместить элемент') 
    def drag_ingredient_to_constructor(self, element, place):

        js_code_to_drag = """
        function triggerDragAndDrop(sourceNode, destinationNode) {
            const dataTransfer = new DataTransfer();
            
            const fireEvent = (type, node) => {
                const event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                node.dispatchEvent(event);
            };
            
            fireEvent('dragstart', sourceNode);
            fireEvent('dragenter', destinationNode);
            fireEvent('dragover', destinationNode);
            fireEvent('drop', destinationNode);
            fireEvent('dragend', sourceNode);
        }
        triggerDragAndDrop(arguments[0], arguments[1]);
        """
        element_to_draggable = self.find_element(element)
        place_to_draggable = self.find_element(place)
        self.driver.execute_script(js_code_to_drag, element_to_draggable, place_to_draggable)

