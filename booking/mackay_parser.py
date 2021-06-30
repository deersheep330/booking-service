from .virtual_parser import VirtualParser


class MackayParser(VirtualParser):

    def __init__(self):

        super().__init__()

        self.url = 'https://wapps.mmh.org.tw/webhealthnumber/EMWAITdefault.aspx?HOSP=1WAIT'

        self.elements = {
            'submit': "//*[@id='btn_webNum']",
            'full': "//*[contains(text(), '不好意思')]"
        }

    def is_full(self):

        print(f'*** mackay parsing start ***')

        super().is_full()

        self.driver.get(self.url)

        self._wait_for('submit')
        try:
            self._click_and_wait('submit', 'full')
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.driver.quit()
            print(f'*** mackay parsing return ***')
