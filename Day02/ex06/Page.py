from elem import Elem, Text
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br

class Page(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content, tag_type='double')

    def is_valid(self):
        # Verifica se a árvore é válida de acordo com as regras estabelecidas
        # Regra 1: Verifica se todos os elementos são do tipo permitido
        valid_types = {'html', 'head', 'body', 'title', 'meta', 'img', 'table',
                       'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div',
                       'span', 'hr', 'br', 'Text'}
        if not self.validate_tree_types(self, valid_types):
            return False

        # Regra 2: Verifica a estrutura Html -> Head -> Body
        if not self.validate_html_structure(self):
            return False

        # Regra 3: Verifica a estrutura de Head e Title
        if not self.validate_head_structure(self):
            return False

        # Regra 4: Verifica a estrutura de Body e Div
        if not self.validate_body_structure(self):
            return False

        # Regra 5: Verifica a estrutura de Text dentro de Title, H1, H2, Li, Th e Td
        if not self.validate_text_structure(self):
            return False

        # Regra 6: Verifica a estrutura de Text dentro de P
        if not self.validate_p_text_structure(self):
            return False

        # Regra 7: Verifica a estrutura de Text e P dentro de Span
        if not self.validate_span_structure(self):
            return False

        # Regra 8: Verifica a estrutura de Li dentro de Ul e Ol
        if not self.validate_li_structure(self):
            return False

        # Regra 9: Verifica a estrutura de Tr, Th e Td dentro de Table
        if not self.validate_table_structure(self):
            return False

        return True

    def validate_tree_types(self, element, valid_types):
        # Verifica se todos os elementos na árvore são de tipos permitidos
        if element.tag not in valid_types:
            return False
        for child in element.content:
            if isinstance(child, Elem) and not self.validate_tree_types(child, valid_types):
                return False
        return True

    def validate_html_structure(self, element):
        # Verifica a estrutura Html -> Head -> Body
        if element.tag == 'html':
            head_found = False
            body_found = False
            for child in element.content:
                if child.tag == 'head':
                    head_found = True
                elif child.tag == 'body':
                    body_found = True
            return head_found and body_found
        return True

    def validate_head_structure(self, element):
        # Verifica a estrutura de Head e Title
        if element.tag == 'head':
            title_count = 0
            for child in element.content:
                if child.tag == 'title':
                    title_count += 1
            return title_count == 1
        return True

    def validate_body_structure(self, element):
        # Verifica a estrutura de Body e Div
        if element.tag in {'body', 'div'}:
            valid_types = {'h1', 'h2', 'div', 'table', 'ul', 'ol', 'span', 'Text'}
            return all(child.tag in valid_types for child in element.content)
        return True

    def validate_text_structure(self, element):
        # Verifica a estrutura de Text dentro de Title, H1, H2, Li, Th e Td
        valid_text_elements = {'title', 'h1', 'h2', 'li', 'th', 'td'}
        if element.tag in valid_text_elements:
            return all(isinstance(child, Text) and len(child.content) == 1 for child in element.content)
        return True

    def validate_p_text_structure(self, element):
        # Verifica a estrutura de Text dentro de P
        if element.tag == 'p':
            return all(isinstance(child, Text) for child in element.content)
        return True

    def validate_span_structure(self, element):
        # Verifica a estrutura de Text e P dentro de Span
        if element.tag == 'span':
            valid_span_content = {'Text', 'p'}
            return all(child.tag in valid_span_content for child in element.content)
        return True

    def validate_li_structure(self, element):
        # Verifica a estrutura de Li dentro de Ul e Ol
        valid_list_elements = {'ul', 'ol'}
        if element.tag in valid_list_elements:
            return any(child.tag == 'li' for child in element.content)
        return True

    def validate_table_structure(self, element):
        # Verifica a estrutura de Tr, Th e Td dentro de Table
        if element.tag == 'table':
            valid_table_content = {'tr'}
            return all(child.tag in valid_table_content for child in element.content)
        return True
    
if __name__ == '__main__':
    html = Html(content=[
        Head(content=[
            Title(content=[Text('"Hello ground!"')])
            ]),
        Body(content=[
            H1(content=Text('"Oh no, not again!"')),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])
    print(Page(content=[html]).is_valid())
    # resp = open('html_base.html', 'w')
    # resp.write(Elem.format_html(html.__str__()))
    # resp.close()
