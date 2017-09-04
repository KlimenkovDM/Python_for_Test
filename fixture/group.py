

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    #Create New Group
    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        # insert value Name
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        # insert value header
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        # insert value footer
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.returns_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        #find and click element
        wd.find_element_by_name("selected[]").click()
        #submit delete
        wd.find_element_by_name("delete").click()
        self.returns_to_group_page()

    def returns_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
