from pageobject2.page.index import Index


class TestAddMember:
    def setup(self):
        self.index = Index()

    def test_add_member(self):
        add_member = self.index.goto_add_member()
        add_member.add_member()
        assert add_member.get_first() == "abcde"
