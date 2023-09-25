import unittest
import random
import time
from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fake = Faker()

class CSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_chrome(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com')
        driver.maximize_window()
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='https://qasvus.files.wordpress.com/2019/09/kitchen-stove-sink-kitchen-counter-3497491.jpeg?w=740']")))
        time.sleep(1)

        try:
            assert driver.title == "California Real Estate – QA at Silicon Valley Real Estate"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        name = driver.find_element(By.ID, "g2-name")
        name.clear()
        name.send_keys(fake.first_name())


        random_email = str(random.randint(0, 99999)) + "myemail@example.com"

        email = driver.find_element(By.ID, "g2-email")
        email.clear()
        email.send_keys(random_email)
            #email.send_keys(fake.email())
        slovo = driver.find_element(By.ID, "contact-form-comment-g2-message")
        slovo.clear()
        slovo.send_keys(fake.text())
        driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        goBack = driver.find_element(By.XPATH, "//a[contains(.,'Go back')]")
        goBack.click()
        time.sleep(5)
        try:
            assert driver.title == "Qwerty"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        time.sleep(2)


    def test_chrome2(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com')
        driver.set_window_size(1820, 1050)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='https://qasvus.files.wordpress.com/2019/09/kitchen-stove-sink-kitchen-counter-3497491.jpeg?w=740']")))
        time.sleep(1)

        try:
            assert driver.title == "California Real Estate – QA at Silicon Valley Real Estate"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        name = driver.find_element(By.ID, "g2-name")
        name.clear()
        name.send_keys(fake.first_name())


        random_email = str(random.randint(0, 99999)) + "myemail@example.com"

        email = driver.find_element(By.ID, "g2-email")
        email.clear()
        email.send_keys(random_email)
            #email.send_keys(fake.email())
        slovo = driver.find_element(By.ID, "contact-form-comment-g2-message")
        slovo.clear()
        slovo.send_keys(fake.text())
        driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        goBack = driver.find_element(By.XPATH, "//a[contains(.,'Go back')]")
        goBack.click()
        time.sleep(5)
        try:
            assert driver.title == "Qwerty"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        time.sleep(2)

class FSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def test_edge(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com')
        driver.maximize_window()
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='https://qasvus.files.wordpress.com/2019/09/kitchen-stove-sink-kitchen-counter-3497491.jpeg?w=740']")))
        time.sleep(1)

        try:
            assert driver.title == "California Real Estate – QA at Silicon Valley Real Estate"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        name = driver.find_element(By.ID, "g2-name")
        name.clear()
        name.send_keys(fake.first_name())


        random_email = str(random.randint(0, 99999)) + "myemail@example.com"

        email = driver.find_element(By.ID, "g2-email")
        email.clear()
        email.send_keys(random_email)
            #email.send_keys(fake.email())
        slovo = driver.find_element(By.ID, "contact-form-comment-g2-message")
        slovo.clear()
        slovo.send_keys(fake.text())
        driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        goBack = driver.find_element(By.XPATH, "//a[contains(.,'Go back')]")
        goBack.click()
        time.sleep(5)
        try:
            assert driver.title == "Qwerty"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        time.sleep(2)

    def test_edge2(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com')
        driver.set_window_size(1820, 1050)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='https://qasvus.files.wordpress.com/2019/09/kitchen-stove-sink-kitchen-counter-3497491.jpeg?w=740']")))
        time.sleep(1)

        try:
            assert driver.title == "California Real Estate – QA at Silicon Valley Real Estate"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        name = driver.find_element(By.ID, "g2-name")
        name.clear()
        name.send_keys(fake.first_name())


        random_email = str(random.randint(0, 99999)) + "myemail@example.com"

        email = driver.find_element(By.ID, "g2-email")
        email.clear()
        email.send_keys(random_email)
            #email.send_keys(fake.email())
        slovo = driver.find_element(By.ID, "contact-form-comment-g2-message")
        slovo.clear()
        slovo.send_keys(fake.text())
        driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        goBack = driver.find_element(By.XPATH, "//a[contains(.,'Go back')]")
        goBack.click()
        time.sleep(5)
        try:
            assert driver.title == "Qwerty"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        time.sleep(2)