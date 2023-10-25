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

    def format_final(html_str):
        html_str = html_str.replace('><', '>\n<')
        lines = html_str.split('\n')
        formatted_lines = []
        indent_level = 0
        flag = 0

        for line in lines:
            line = line.strip()
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

        formatted_html = '\n'.join(formatted_lines)
        return formatted_html
    
    def ident(html_str):
        lines = html_str.replace('\n', '@@@ @@@')
        lines = lines.split(' @@@')
        formatted_lines = []
        indent_level = 0
        flag = 0

        if len(lines) == 1:
            print(lines[0].find('>'))
            print(lines[0].find('</'))
            print(lines[0][[lines[0].find('>')]:[lines[0].find('</')]])
            front = lines[0].split(' ')
            back = front[1].split('</')
            if len(front) == 2 and len(back) == 2:
                return front[0] + '\n  ' + back[0] + '\n</' + back[1]  

        for line in lines:
            line = line.strip()
            if line.startswith("</"):
                indent_level -= 1
            if flag == 1:
                indent_level -= 1
                flag = 0
            formatted_line = ' ' * (2 * indent_level) + line
            if not line.startswith("</") and not line.endswith("/>"):
                indent_level += 1
            formatted_lines.append(formatted_line)
            if not line.startswith("<") or '<div></div>' in line:
                flag = 1
           
        formatted_html = ''.join(formatted_lines)
        formatted_html = formatted_html.replace('@@@','\n')
        return formatted_html        

    
    def format_html(html_str):
        lines = html_str.replace('><','>,<')
        lines = lines.split(',')
        formatted_lines = lines

        for i in range(0, len(formatted_lines)):
            if formatted_lines[i] == '<body>' and '<div>' in formatted_lines[i+1]:
                formatted_lines[i] += '\n'
            if formatted_lines[i] == '<div>' and '<div>' in formatted_lines[i+1]:
                formatted_lines[i] += '\n'
            if formatted_lines[i] == '<div>' and not '<' in formatted_lines[i+1]:
                formatted_lines[i] += '\n'
                formatted_lines[i+1] += '\n'
            if not '<' in formatted_lines[i] and not '<' in formatted_lines[i+1]:
                formatted_lines[i+1] += '\n'
            if len(formatted_lines) > 1:
                if '<div>' in formatted_lines[i] and '  </div>' in formatted_lines[i+1]:
                    formatted_lines[i+1] = formatted_lines[i+1].replace('  </div>','</div>')
                    formatted_lines[i+1] += '\n'
            
        formatted_html = ''.join(formatted_lines)
        if formatted_html == '<div></div>':
            return formatted_html
        else:
            if '</' in formatted_lines[len(formatted_lines)-1] \
            and '</' in formatted_lines[len(formatted_lines)-2]\
            and len(formatted_lines) > 1:
                formatted_lines[len(formatted_lines)-2] = formatted_lines[len(formatted_lines)-2] + '\n'
            formatted_html = ''.join(formatted_lines)
            formatted_html = formatted_html.replace('\n \n','\n ')
            formatted_html = formatted_html.replace('\n\n','\n')
            formatted_html = formatted_html.replace(' \n ','')
            formatted_html = Elem.ident(formatted_html)
            return formatted_html

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
        result = Elem.format_html(result)
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
    try:
        title = Elem(tag='title', content=Text('Hello ground'), tag_type='double')
        h1 = Elem(tag='h1', content=Text('Oh no, not again!'), tag_type='double')
        img = Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
        

        header = Elem(tag='head', content=title, tag_type='double')
        body = Elem(tag='body', content=[h1,img], tag_type='double')
        html = Text(Elem(tag='html', content=[header,body], tag_type='double'))

        base = open('base.html', 'w')
        base.write(Elem.format_final(html))
        base.close()
    except Elem.ValidationError as e:
        print(e)
