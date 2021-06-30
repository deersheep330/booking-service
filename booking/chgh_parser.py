from .virtual_parser import VirtualParser


class ChghParser(VirtualParser):

    def __init__(self):

        super().__init__()

        self.url = 'https://www.chgh.org.tw/Covid19/CovidRemaining.aspx'

        self.elements = {
            'cells': "//table//tr//td//span",
        }

    def is_full(self):

        print(f'*** chgh parsing start ***')

        super().is_full()

        self.driver.get(self.url)

        try:
            cells = self.driver.find_elements_by_xpath('cells')
            for cell in cells:
                if "已額滿" not in cell.text:
                    return False
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.driver.quit()
            print(f'*** chgh parsing return ***')
