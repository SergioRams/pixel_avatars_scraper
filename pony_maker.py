from avatar_maker import AvatarMaker, os, errno


class PonyMaker(AvatarMaker):

    MAKER_NAME = 'ponys'

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

    def wings_btn(self):
        self.browser.driver.find_element_by_xpath(f"//img[@src='{self.IMAGE_PATH}Wings.png']").click()

    def tail_btn(self):
        self.browser.driver.find_element_by_xpath(f"//img[@src='{self.IMAGE_PATH}Tail.png']").click()

    def save_avatar(self, pic_id):
        """
        Takes a screenshot and saves it to given path (for some reason getting the dynamic element does not seem to work
        .The screenshot is a workaround)
        :param pic_id: picture ID
        """

        screenshot = self.browser.driver.find_element_by_xpath("//div[@id='largeSize']/img").screenshot_as_png

        # label image and save it
        image_name = 'pony_avatar' + str(pic_id) + '.png'
        path_to_save = os.path.join(f'avatars/{self.MAKER_NAME}/', image_name)

        with open(path_to_save, 'wb') as file:
            file.write(screenshot)

