from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_IN_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]")
    ORDER_INGREDIENTS_LIST = (By.XPATH, "//p[text()='Cостав']")
    FIRST_ORDER_NUMBER = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[last()]")
    TOTAL_ORDERS_COUNT = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__')])[1]")
    TODAY_ORDERS_COUNT = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__')])[2]")
    CURRENT_ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'orderListReady')]/li[contains(@class, 'default mb-2')]")

    
    