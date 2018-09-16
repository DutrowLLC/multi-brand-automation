from __future__ import print_function
from selenium import webdriver as wd
from settings import test_url
from settings import path, log_path
import sys, requests, time, traceback, subprocess as sp
sys.path.append(path)
from credentials import google_business_url, google_uname, google_passwd

class GoogleBusinessScraper(object):
    def __init__(self):
        self.main()

    def main(self):
        with open(log_path + 'google_business_scraper.log', 'w') as self.log_fh:
            self.driver = wd.Chrome(
                service_log_path = log_path + 'chromedriver.log'
            )

            try:
                self.get_insights()
            except:
                traceback.print_exc()
                traceback.print_exc(file=self.log_fh)

            self.driver.quit()

    def get_insights(self):
        self.driver.get(google_business_url)

        self.send_email()
        self.click_submit()
        self.send_passwd()
        self.click_submit()

        los = self.listing_on_search()
        lom = self.listing_on_maps()
        vyw = self.visit_your_website()
        rd = self.request_directions()
        cy = self.call_you()
        cty = self.chat_to_you()

        self.report(los, lom, vyw, rd, cy, cty)
        
        # Pause for 10 seconds
        time.sleep(10)

    def send_email(self):
        el = './/input[contains(@type, "email")]'
        el = self.driver.find_element_by_xpath(el)
        el.send_keys(google_uname)
        time.sleep(2)

    def send_passwd(self):
        el = './/input[contains(@type, "password")]'
        el = self.driver.find_element_by_xpath(el)
        el.send_keys(google_passwd)
        time.sleep(2)

    def click_submit(self):
        el = './/span[contains(text(), "Dalej")]'
        el = self.driver.find_element_by_xpath(el)
        el.click()
        time.sleep(2)

    def listing_on_search(self):
        el = './/span[contains(text(), "Listing on Search")]/following-sibling::span'
        return self.driver.find_element_by_xpath(el).text

    def listing_on_maps(self):
        el = './/span[contains(text(), "Listing on Maps")]/following-sibling::span'
        return self.driver.find_element_by_xpath(el).text
    
    def visit_your_website(self):
        el = './/span[contains(text(), "Visit your website")]/following-sibling::span'
        return self.driver.find_element_by_xpath(el).text

    def request_directions(self):
        el = './/span[contains(text(), "Request directions")]/following-sibling::span'
        return self.driver.find_element_by_xpath(el).text

    def call_you(self):
        el = './/span[contains(text(), "Call you")]/following-sibling::span'
        return self.driver.find_element_by_xpath(el).text

    def chat_to_you(self):
        el = './/span[contains(text(), "Chat to you")]/following-sibling::span'
        return self.driver.find_element_by_xpath(el).text

    def close_wd(self):
        sp.call(['sudo', 'pkill', 'chromedriver'])

    def check_ip(self):
        resp = requests.get(test_url)
        ip = resp.json()['YourFuckingIPAddress']
        resp.close()
        return ip

    def report(self, el1, el2, el3, el4, el5, el6):
        print("Listing on search: {}\nListing on maps: {}\nVisit your website: {}\nRequest directions: {}\nCall you: {}\nChat to you: {}"
            .format(el1, el2, el3, el4, el5, el6))

if __name__ == "__main__":
    GoogleBusinessScraper()

