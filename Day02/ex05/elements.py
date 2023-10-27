from elem import Elem, Text

class Html(Elem):
    def __init__(self, content, attr={}):
        self.tag = 'html'
        self.tag_type = 'double'
        self.attr = attr
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Head(Elem):
    def __init__(self, content=None, attr={}):
        self.tag = 'head' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Body(Elem):
    def __init__(self, content=None, attr={}):
        self.tag = 'body' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content
    
class Title(Elem):
    def __init__(self, content=None, attr={}):
        self.tag = 'title' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Meta(Elem):
    def __init__(self, attr={}):
        self.tag = 'meta' 
        self.attr = attr
        self.tag_type = 'simple'
        self.content = None
        

class Img(Elem):
    def __init__(self, attr):
        self.tag = 'img' 
        self.attr = attr
        self.tag_type = 'simple'
        self.content = None

class H1(Elem):
    def __init__(self, attr={}, content=None):
        self.tag = 'h1' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class H2(Elem): 
    def __init__(self, attr={}, content=None):
        self.tag = 'h2' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class P(Elem):
    def __init__(self, attr={}, content=None):
        self.tag = 'p' 
        self.attr = attr
        self.tag_type = 'simple'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Div(Elem):
    def __init__(self, attr={}, content=None):
        self.tag = 'div' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Span(Elem):
    def __init__(self, attr={}, content=None):
        self.tag = 'span' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Hr(Elem):
    def __init__(self, attr={}):
        self.tag = 'hr' 
        self.attr = attr
        self.tag_type = 'simple'
        self.content = None

class Br(Elem): 
    def __init__(self):
        self.tag = 'br' 
        self.attr = {}
        self.tag_type = 'simple'
        self.content = None

class Table(Elem):
    def __init__(self, attr={}, content=None):
        self.tag = 'table' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Th(Elem):
    def __init__(self, attr={}, content=None):
        self.tag = 'th' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Tr(Elem):
    def __init__(self, attr={}, content=None):
        self.tag = 'tr' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Td(Elem):
    def __init__(self, attr={}, content=None):
        self.tag = 'td' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Ul(Elem):
    def __init__(self, attr={}, content=None):
        self.tag = 'ul' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Ol(Elem):
    def __init__(self, attr={}, content=None):
        self.tag = 'ol' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

class Li(Elem):
    def __init__(self, attr={}, content=None):
        self.tag = 'li' 
        self.attr = attr
        self.tag_type = 'double'
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

if __name__ == '__main__':
    title = Title(content=Text('"Hello ground!"'))
    head = Head(title)
    img = Img({'src': 'http://www.python.org'})
    h1 = H1(content=Text('"Oh no, not again!"'))
    body = Body([h1, img])

    print( Html([head, body] ))
