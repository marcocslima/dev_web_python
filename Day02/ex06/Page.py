from elements import *

class Page:
    def __init__(self, elem) -> None:
        self.elem = elem
        

    def is_valid(self):
        print(self.elem.tag)
        for node in self.elem.content:
            if not self.check_tree(node):
                return False
        if self.elem.tag == 'html':
            if self.elem.content != [ Head(), Body() ]:
                print(self.elem.content)
        return True

    def check_tree(self, node):
        types = {'Html', 'Head', 'Body', 'title', 'meta', 'img', 'table', 'th',\
                 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br', 'text'}

        if node.__class__.__name__ not in types:
            return False
        if node.content:
            for content_node in node.content:
                if not self.check_tree(content_node):
                    return False
        return True

if __name__ == '__main__':
    title = Title(content=Text('"Hello ground!"'))
    head = Head(title)
    img = Img({'src': 'http://www.python.org'})
    h1 = H1(content=Text('"Oh no, not again!"'))
    body = Body([h1, img])

    body = Body([h1, img])
    ins = Page( Html( [Head(), Body()] ) )
    print(ins.is_valid())
