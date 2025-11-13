from selenium.webdriver.common.by import By

class MainPageLocators:
    ENTER_BUTTON_ACCOUNT = (By.XPATH, "//button[text() = 'Войти в аккаунт']")
    USER_PROFILE_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")
    CONSTRUCTOR_BURGER_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[text() = 'Лента Заказов']")
    INGREDIENT_CARD = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_INFO_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__')]")
    CLOSE_INGREDIENT_MODAL_BUTTON = (By.XPATH, ".//section[contains(@class, 'Modal_modal_open')]//button[contains(@class, 'close')]")    
    CONSTRUCTOR_BUN_SLOT = (By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_')
    AMOUNT_INDICATOR = (By.XPATH, "//p[contains(@class, 'text text_type_digits-medium mr-3')]")   
    ORDER_COOKING = (By.XPATH, "//p[contains(@class, 'undefined text text_type_main-small mb-2')]")   
    CLOSE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
    MODAL_BACKDROP = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")
    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow_')]")    
    HIDDEN_INGREDIENT_MODAL = (By.CLASS_NAME, 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5')
    DRAGGABLE_INGREDIENT_CARD = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]")
