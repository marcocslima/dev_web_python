#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.
    """
    def __str__(self):
        if super().__str__() == '<':
            return super().__str__().replace('<', '&lt;')
        if super().__str__() == '>':
            return super().__str__().replace('>', '&gt;')
        if super().__str__() == '"':
            return super().__str__().replace('"', '&quot;')
        return super().__str__().replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    class ValidationError(Exception):
        def __init__(self, value='incorrect behaviour.'):
            super().__init__(value)
    
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag 
        self.attr = attr
        self.tag_type = tag_type
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content

    def simple(self):
        if self.attr:
            result = f'<{self.tag}{self.__make_attr()}>' 
        else:
            result = f'<{self.tag}>\n'
        return result

    def double(self, jump, level):
        if  self.attr and self.content:
            result = f'<{self.tag} {self.__make_attr()}>{self.__make_content(level, jump)}</{self.tag}>' 
        elif self.attr:
            result = f'<{self.tag} {self.__make_attr()}></{self.tag}>'
        elif self.content:
            if isinstance(self.content, Elem):
                result = f'{self.__make_content(level, jump)}'
            else:
                result = f'{jump}<{self.tag}>{self.__make_content(level, jump)}</{self.tag}>'
        else:
            if level > 0:
                result = f'{jump}<{self.tag}></{self.tag}>'
            else:
                result = f'<{self.tag}></{self.tag}>'
        return result


    def __str__(self, level=0):
        jump = ' ' * 2 * level
        
        if self.tag_type == 'simple':
            result = Elem.simple(self)
        elif self.tag_type == 'double':
            result = Elem.double(self, jump, level)
        return result

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self, nivel, espacos=''):
        try:
            result ='\n'
            if isinstance(self.content, Elem):
                content_str = self.content.__str__(nivel + 1)
                result = f'{espacos}<{self.tag}>\n{content_str}\n{espacos}</{self.tag}>'
            elif len(self.content) == 0:
                return ''
            elif isinstance(self.content, Text):
                result = f'\n{espacos}  {self.content.__str__()}\n{espacos}'
            elif isinstance(self.content, list) and isinstance(self.content[1], Elem):
                for elem in self.content: 
                    separar = elem.__str__().split('\n') 
                    for line in separar:
                        result += f'{espacos}  {line}\n'
            else:
                for elem in self.content:
                    if elem == '':
                        continue
                    result += f'  {elem}\n'
                
                if result == '\n':
                    return ''
            return result
        except:
            raise(Elem.ValidationError)

    def add_content(self, content):
        if not Elem.check_type(content):
            raise(Elem.ValidationError)
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

if __name__ == '__main__':
    img = Elem('img', {'src': 'http://www.python.org'}, tag_type='simple')
    head = Elem(tag=Text('head'),content=Elem(tag=Text('title'),content=Text('"Hello ground!"')))
    body = Elem(tag=Text('body'),content=[Elem(tag=Text('h1'),content=Text('"Oh no, not again!"')), img])
    
    print(str(Elem(tag=Text('html'),content=[head, body])))