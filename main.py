import browser
import chibi_maker
import minipix_maker
import pony_maker


if __name__ == "__main__":

    # get google chrome browser driver
    driver = browser.ChromeBrowser("http://www.avatarsinpixels.com/chibi/clothing/Body")
    chibi = chibi_maker.ChibiMaker(driver)
    """ SCRAPE CHIBIS"""
    # resize to 100x100 pixels
    chibi.avatar_resize(100)
    # save 60 random avatars
    chibi.generate_random_avatars(60)

    driver.driver.get("http://www.avatarsinpixels.com/minipix/clothing/Body")
    minipix = minipix_maker.MinipixMaker(driver)
    """ SCRAPE MINIPIX """
    minipix.avatar_resize(100)
    minipix.generate_random_avatars(60)

    driver.driver.get("http://www.avatarsinpixels.com/pony/clothing/Body")
    ponys = pony_maker.PonyMaker(driver)
    """ SCRAPE PONIES """
    ponys.avatar_resize(100)
    ponys.generate_random_avatars(60)

    driver.close()
