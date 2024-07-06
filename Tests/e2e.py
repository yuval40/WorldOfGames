from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_scores_service(url):
    driver = webdriver.Chrome()

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "score"))
        )

        score_text = driver.find_element(By.ID, "score").text

        score = int(score_text)

        if 1 <= score <= 1000:
            return True
        else:
            return False

    except TimeoutException:
        print("Timed out waiting for score element to appear")
        return False

    finally:

        driver.quit()


def main_function():
    url = "http://127.0.0.1:8777"

    if test_scores_service(url):
        print("Tests passed")
        return 0
    else:
        print("Tests failed")
        return -1


if __name__ == "__main__":

    exit_code = main_function()
    exit(exit_code)
