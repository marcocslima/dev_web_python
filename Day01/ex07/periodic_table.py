map = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
[3,4,0,0,0,0,0,0,0,0,0,0,5,6,7,8,9,10],
[11,12,0,0,0,0,0,0,0,0,0,0,13,14,15,16,17,18],
[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36],
[37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54],
[55,56,-1,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86],
[87,88,-1,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118]]

head = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Tabela Periódica</title>
    <style>
        .periodic-table {
            display: grid;
            grid-template-columns: repeat(18, 1fr);
            grid-gap: 5px;
            margin: 20px;
        }
        .element {
            width: 100px;
            height: 100px;
            border: 1px solid #000;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            font-size: 14px;
        }
        .element_empty {
            width: 100px;
            height: 100px;
            border: 0px solid #000;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            font-size: 14px;
        }
        ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        li {
            margin: 0;
        }
        .left-aligned-li {
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Tabela Periódica de Mendeleiev</h1>
"""

def load_info():
    base = {}
    with open('periodic_table.txt', 'r') as file:
        for line in file:
            key = line.split(",")[1].split(":")[1].strip()
            value = line.split("=")[0].strip() \
                    + "," + line.split("=")[1].split(",")[2].split(":")[1].strip() \
                    + "," +  line.split("=")[1].split(",")[3].split(":")[1].strip()  
            base.update({key : value})
    return base

def init_base():
    info = load_info()
    ref = []
    l = 0 
    for line in map:
        l = l + 1
        c = 0
        for col in line:
            c = c + 1
            if str(col) in info:
                ref.append([l,c,str(col),info[str(col)]])
    return ref

def txt_assemble(c,s,e,m,tipo):
    if tipo == 0:
        txt = """\n\t\t<td>\n\t\t\t<ul class="element_empty">\n\t\t\t\t<li class="left-aligned-li" style="text-indent: 20px;">{}</li>\n\t\t\t\t<li>{}</li>\n\t\t\t\t<li>{}</li>\n\t\t\t\t<li>{}</li>\n\t\t\t</ul>\n\t\t</td>""".format(c,s,e,m)
    elif tipo == -1:
        txt = """\n\t\t<td>\n\t\t\t<ul class="element">\n\t\t\t\t<li class="left-aligned-li" style="text-indent: 20px;">{}</li>\n\t\t\t\t<li>{}</li>\n\t\t\t\t<li>{}</li>\n\t\t\t\t<li>{}</li>\n\t\t\t</ul>\n\t\t</td>""".format(c,s,e,m)
    else:
        txt = """\n\t\t<td>\n\t\t\t<ul class="element">\n\t\t\t\t<li class="left-aligned-li" style="text-indent: 20px;">{}</li>\n\t\t\t\t<li><h4 style="margin: 0;">{}</h4></li>\n\t\t\t\t<li>{}</li>\n\t\t\t\t<li>{}</li>\n\t\t\t</ul>\n\t\t</td>""".format(c,s,e,m)
    return txt

def periodic_table():
    base = load_info()
    c,s,e,m = '','','',''
    
    p_table = open("periodic_table.html", "w")
    p_table.write(head)
    p_table.write("<table>\n")
    l = 0
    for line in map:
        p_table.write("\t<tr>")
        for col in line:
            if col == 0:
                p_table.write(txt_assemble('','','','',0))
            elif col == -1:
                p_table.write(txt_assemble('','','','',-1))
            else:
                elem = base[str(col)].split(',')[0]
                simble = base[str(col)].split(',')[1]
                mass = base[str(col)].split(',')[2]
                p_table.write(txt_assemble(col,simble,elem,mass,1))
        p_table.write("\n</tr>\n")
    p_table.write("</table>\n</body>\n</html>")
    
    p_table.close()

if __name__ == '__main__':
    periodic_table()