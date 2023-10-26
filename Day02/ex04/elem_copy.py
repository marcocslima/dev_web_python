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
        def __init__(self):
            super().__init__("incorrect behaviour.")

    def r_arr(str):
        replacements = {'<': '', '>': '', '</': '',}
        for old, new in replacements.items():
            str = str.replace(old, new)
        return str

    def format(str):
        lines = str.replace('><','>@@@<').replace(',','@@@').split('@@@')

        formatted_lines = []

        if len(lines) == 2:
            return ''.join(lines).replace('\n', '')
        
        for i in range(0, len(lines)-1):
            if not lines[i] in lines[i+1]:
                if Elem.r_arr(lines[i]) in lines[i+1]:
                    if not '\n' in lines[i]:
                        lines[i+1] = lines[i+1].replace('>', '>\n')
                else:
                    if not '\n' in lines[i]:
                        lines[i] = lines[i].replace('>', '>\n')
            else:
                if Elem.r_arr(lines[i]) in lines[i+1]:
                    if not '\n' in lines[i]:
                        lines[i] = lines[i].replace('>', '>\n')
                
        indent_level = 0
        flag = 0

        for line in lines:
            if line.startswith("</"):
                indent_level -= 1
            if flag == 1:
                indent_level -= 1
                flag = 0
            formatted_line = ' ' * (2 * indent_level) + line
            if not line.startswith("</") and not line.endswith("/>"):
                indent_level += 1
            formatted_lines.append(formatted_line)
            if not line.startswith("<"):
                flag = 1

        formated = ''.join(formatted_lines)        

        if '>  <' in formated:
            formated = formated.replace('>  <', '><').replace('\n\n','\n')
        if formated[-1] == '\n':
            formated = formated[:-1]
        return formated
    
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.content = content
        self.tag_type = tag_type

        if not Elem.check_type(content):
            raise Elem.ValidationError()

        if content is not None:
            if isinstance(content, Elem):
                self.content = content
            elif isinstance(content, list):
                self.content = []
                for item in content:
                    if isinstance(item, (Elem, Text)):
                        self.add_content(item)
          
    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = f"<{self.tag}{self.__make_attr()}>"
            result += f"{self.__make_content()}"
            result += f"</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"<{self.tag}{self.__make_attr()}/>"
        result = Elem.format(result)
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
        if not isinstance(self.content, Elem):
            if self.content is None:
                return ''
        if type(self.content) == list:
            result = ''
            for elem in self.content:
                if isinstance(elem, Text):
                    result += str(elem).replace('\n', '\n<br />\n')  # Adiciona <br /> para quebras de linha
                elif isinstance(elem, Elem):
                    if not '<' in result:
                        result = ',' + result.replace('\n','\n ,')
                    result += str(elem)
                if not result == '': 
                    result += '\n'  # Adiciona uma quebra de linha após cada elemento
            return result
        result = str(self.content)
        if len(result) == 1:
            result = ' ' + result
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (content == None or isinstance(content, Elem)
                or type(content) == Text or (type(content) == list
                and all([type(elem) == Text or isinstance(elem, Elem)
                for elem in content])))

if __name__ == '__main__':
    assert str(Elem('div', {}, None, 'double')) == '<div></div>'
    # try:
    #     title = Elem(tag='title', content=Text('Hello ground'), tag_type='double')
    #     h1 = Elem(tag='h1', content=Text('Oh no, not again!'), tag_type='double')
    #     img = Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
        

    #     header = Elem(tag='head', content=title, tag_type='double')
    #     body = Elem(tag='body', content=[h1,img], tag_type='double')
    #     html = Text(Elem(tag='html', content=[header,body], tag_type='double'))

    #     base = open('base.html', 'w')
    #     base.write(Elem.format_final(html))
    #     base.close()
    # except Elem.ValidationError as e:
    #     print(e)
