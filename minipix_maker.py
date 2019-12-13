from avatar_maker import AvatarMaker, os, errno, time


class MinipixMaker(AvatarMaker):

    MAKER_NAME = 'minipixs'

    def __init__(self, driver):
        super().__init__(driver)
        self.create_folder()

    def create_folder(self):
        # creates directory to save images if not existent
        filename = f"avatars/{self.MAKER_NAME}/"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

    # unique buttons to this class
    def background_btn(self):
        self.browser.driver.find_element_by_xpath(f"//img[@src='{self.IMAGE_PATH}Background.png']").click()

    def background_blank(self):
        """ sets the background to be white """

        self.background_btn()
        self.browser.driver.find_element_by_xpath("//img[@src='/minipix/Background/0/thumbnail.png']").click()
        self.lock_btn()
        self.browser.driver.find_element_by_xpath('//button[@data-lock="Background"]').click()

    def cape_back_btn(self):
        self.browser.driver.find_element_by_xpath(f"//img[@src='{self.IMAGE_PATH}CapeBack.png']").click()

    def glasses_btn(self):
        self.browser.driver.find_element_by_xpath(f"//img[@src='{self.IMAGE_PATH}Glasses.png']").click()

    def hat_btn(self):
        self.browser.driver.find_element_by_xpath(f"//img[@src='{self.IMAGE_PATH}Hat.png']").click()

    def jacket_btn(self):
        self.browser.driver.find_element_by_xpath(f"//img[@src='{self.IMAGE_PATH}Jacket.png']").click()

    def generate_random_avatars(self, n=100):
        """
        Uses randomize feature from the page and saves a screenshot
        :param n: number of random avatar to generate
        """

        # sets to white background firsts
        self.background_blank()

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
        image_name = 'minipix_avatar' + str(pic_id) + '.png'
        path_to_save = os.path.join(f'avatars/{self.MAKER_NAME}/', image_name)

        with open(path_to_save, 'wb') as file:
            file.write(screenshot)
