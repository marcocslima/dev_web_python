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
        # return super().__str__().replace('\n', '\n<br />\n').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self):
            super().__init__('Content must be a Text instance or a list of Text instances')

    def format_html(html_str):
        # html_str = html_str.replace('><', '>\n<')
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
            formatted_line = ' ' * (4 * indent_level) + line
            if not line.startswith("</") and not line.endswith("/>"):
                indent_level += 1
            formatted_lines.append(formatted_line)
            if not line.startswith("<"):
                flag = 1

        formatted_html = '\n'.join(formatted_lines)
        return formatted_html

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.content = content if content is not None else []
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
            result += f"{self.__make_content()}"
            result += f"\n</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"\n<{self.tag}{self.__make_attr()}/>"
        result += '\n'
        result = result.replace('\n\n', '>\n<').replace('<<', '<').replace('>>', '>')
        return Elem.format_html(result)

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
