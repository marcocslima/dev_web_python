class Intern:
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def make_coffee(self):
        return self.Coffee()

    def print_name(self):
        print(self.name)

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

def intern():
    intern_no_name = Intern()
    intern = Intern("Mark")

    intern_no_name.print_name()
    intern.print_name()

    cf = intern_no_name.make_coffee()
    print(cf)

    try:
        intern_no_name.work()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    intern()
