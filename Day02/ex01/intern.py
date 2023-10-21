class Intern:

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
    
    def make_coffee(self):
        return self.Coffee()

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

def intern():
    intern_no_name = Intern()
    intern = Intern("Mark")

    print(intern_no_name.name)
    print(intern.name)

    coffee = intern.make_coffee()
    print(coffee)

    try:
        intern_no_name.work()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    intern()
