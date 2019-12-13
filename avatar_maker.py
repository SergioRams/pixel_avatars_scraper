import time
import os
import errno


class AvatarMaker:

    IMAGE_PATH = "/Public/images/layers/"

    def __init__(self, driver):
        # get google chrome browser driver
        self.browser = driver

    # mapping elements to methods
    def random_btn(self):
        """
        generates a random avatar
        """
        self.browser.driver.find_element_by_xpath("//img[@src='/Public/images/ico_random.png']").click()

    def random_color_btn(self):
        """
        given some avatar it will change hair and clothes colors
        """
        self.browser.driver.find_element_by_xpath("//img[@src='/Public/images/ico_random_colors.png']").click()

    def random_clothes_btn(self):
        """
        given some avatar it will change the clothing layers
        """
        self.browser.driver.find_element_by_xpath("//img[@src='/Public/images/ico_random_layers.png']").click()

    def reset(self):
        """
        resets avatar size and appearance
        """
        self.browser.driver.find_element_by_xpath("//img[@src='/Public/images/ico_reset.png']").click()

    def zoom_out(self):
        """
        makes avatar smaller
        """
        self.browser.driver.find_element_by_id("zoomOut").click()

    def zoom_in(self):
        """
        makes avatar larger
        """
        self.browser.driver.find_element_by_id("zoomIn").click()

    def lock_btn(self):
        self.browser.driver.find_element_by_xpath(f"//img[@src='{self.IMAGE_PATH}Locks.png']").click()

    def body_btn(self):
        self.browser.driver.find_element_by_xpath(f"//img[@src='{self.IMAGE_PATH}Body.png']").click()

    def create_folder(self):
        # creates directory to save images if not existent
        filename = f"avatars/test/"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

    def avatar_resize(self, size=100):
        """
        :param size: size in pixels defaults to 100 x 100
        """
        # clicks the reset size button first
        self.reset()
        resize = 0

        if size == 250:
            resize = 0
        elif size == 200:
            resize = 1
        elif size == 150:
            resize = 2
        elif size == 100:
            resize = 3
        elif size == 50:
            resize = 4
        else:
            pass

        for _ in range(resize):
            self.zoom_out()

    def generate_random_avatars(self, n=100):
        """
        Uses randomize feature from the page and saves a screenshot
        :param n: number of random avatar to generate
        """
        for pic_id in range(n):
            time.sleep(.3)
            self.random_btn()
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
