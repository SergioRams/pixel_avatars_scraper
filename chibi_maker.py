import time
import os
import errno


class ChibiMaker:

    image_path = "/Public/images/layers/"

    def __init__(self, driver):
        # get google chrome browser driver
        self.browser = driver

        # creates directory to save images if not existent
        filename = "avatars/chibis/"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        # map elements to attributes
        self.body_btn = self.browser.driver.find_element_by_xpath(f"//img[@src='{self.image_path}Body.png']")
        self.eyebrows_btn = self.browser.driver.find_element_by_xpath(f"//img[@src='{self.image_path}Eyebrows.png']")

    def lock_button(self):
        self.browser.driver.find_element_by_xpath(f"//img[@src='{self.image_path}Locks.png']").click()

    def avatar_resize(self, size=100):
        """
        :param size: size in pixels defaults to 100 x 100
        :return:
        """
        time.sleep(1)
        self.browser.driver.find_element_by_id("zoomOut").click()
        self.browser.driver.find_element_by_id("zoomOut").click()
        self.browser.driver.find_element_by_id("zoomOut").click()

    def randomize_avatar(self, n=100):
        """
        Uses randomize feature from the page and saves a screenshot
        :param n: number of random avatar to generate
        """

        for pic_id in range(n):
            time.sleep(.3)
            self.browser.driver.find_element_by_xpath("//img[@src='/Public/images/ico_random.png']").click()
            self.save_avatar(pic_id)

    def save_avatar(self, pic_id):
        """
        Takes a screenshot and saves it to given path (for some reason getting the dynamic element does not seem to work
        .The screenshot is a workaround)
        :param pic_id: picture ID
        """

        screenshot = self.browser.driver.find_element_by_xpath("//div[@id='largeSize']/img").screenshot_as_png

        # label image and save it
        image_name = 'chibi_avatar' + str(pic_id) + '.png'
        path_to_save = os.path.join('avatars/chibis/', image_name)

        with open(path_to_save, 'wb') as file:
            file.write(screenshot)

