#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self):
            super().__init__('Content must be a Text instance or a list of Text instances')

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.content = content
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = f"<{self.tag}{self.__make_attr()}>"
            result += self.__make_content()
            result += f"</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"<{self.tag}{self.__make_attr()}/>"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += Text(elem)
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    # title = Elem(tag='title', content='Hello ground', tag_type='double')
    # h1 = Elem(tag='h1', content='Oh no, not again!', tag_type='double')
    # img = Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
    
    # head = Elem(tag='head', content=[title],tag_type='double')
    # body = Elem(tag='body', content=[h1, img], tag_type='double')
    # html = Elem(tag='html', content=[head, body], tag_type='double')

    # base = open('resp.html', 'w')
    # base.write(str(html))
    # base.close()
    # Criar os elementos para cabeçalho, parágrafo e lista não ordenada
    header = Elem(tag='h1', content='Meu Título', tag_type='double')
    paragraph = Elem(tag='p', content='Este é um parágrafo de exemplo.', tag_type='double')
    unordered_list = Elem(tag='ul', tag_type='double')

    # Criar os elementos da lista não ordenada (itens de lista)
    list_item_1 = Elem(tag='li', content='Item 1', tag_type='double')
    list_item_2 = Elem(tag='li', content='Item 2', tag_type='double')
    list_item_3 = Elem(tag='li', content='Item 3', tag_type='double')

    # Adicionar os itens de lista à lista não ordenada usando add_content
    # unordered_list.add_content([list_item_1, list_item_2, list_item_3])
    unordered_list.add_content(list_item_1)

    # Criar o elemento <body> e adicionar o cabeçalho, parágrafo e lista não ordenada usando add_content
    body = Elem(tag='body', content=[header, paragraph])
    body.add_content(unordered_list)

    # Criar o elemento HTML e adicionar o cabeçalho e o corpo
    html = Elem(tag='html', content=[body], tag_type='double')

    # Agora você pode criar o arquivo HTML e gravar o HTML resultante nele
    with open('exemplo.html', 'w') as file:
        file.write(str(html))

    
