import browser
import chibi_maker

if __name__ == "__main__":

    # get google chrome browser driver
    driver = browser.ChromeBrowser("http://www.avatarsinpixels.com/chibi/clothing/Body")
    chibi = chibi_maker.ChibiMaker(driver)

    """ SCRAPE """
    # resize to 100x100 pixels
    chibi.avatar_resize(100)
    chibi.randomize_avatar()

    driver.close()
