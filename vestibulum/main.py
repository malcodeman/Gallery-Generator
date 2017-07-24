"""The OS module in Python provides a way of using operating system dependent functionality."""
import os

def main():

    STYLE = """body {
        margin: 0;
    }

    a {
        text-decoration: none;
    }

    h1,
    h2,
    h3,
    p {
        margin-top: 0;
        margin-bottom: 0;
    }

    .main {
        background-color: #fafafa;
    }

    .container {
        max-width: 992px;
        margin: 0 auto;
        width: 100%;
    }

    .header{
        padding-bottom: 1rem;
    }

    .ul{
        list-style-type: none;
        padding-left: 0;
        margin-top: 0;
        margin-bottom: 0;
        display: flex;
        justify-content: space-around;
        padding-bottom: 1rem;
    }

    .li{
        display: flex;
        flex-direction: column;
        text-align: center;
        font-family: Open Sans;
    }

    .li span:nth-child(1){
        color: #131313;
        font-size: 1rem;
    }

    .li span:nth-child(2){
        color: #353535;
        font-size: .8rem;
    }

    .col {
        display: flex;
        flex-direction: column;
    }

    .row {
        display: flex;
        margin-bottom: .4rem;
    }

    .row:last-child {
        margin-bottom: 0;
    }

    .row-content {
        flex-grow: 1;
        position: relative;
        margin-right: .4rem;
    }

    .row-content::before {
        content: "";
        display: block;
        padding-top: 100%;
    }

    .row-content:last-child {
        margin-right: 0;
    }

    .row-content img {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        object-fit: cover;
    }
    """


    HTML_IMG_SRC = []
    EXTENSIONS = [".jpg", ".png", ".JPG", ".gif"]
    SIZE = 0

    FILES = [f for f in os.listdir(".") if os.path.isfile(f) if f.endswith(tuple(EXTENSIONS))]
    for f in FILES:
        print(f)
        print(os.path.realpath(f))
        HTML_IMG_SRC.append(os.path.realpath(f))
        print(os.path.getsize(os.path.realpath(f)))
        SIZE += os.path.getsize(os.path.realpath(f))

    print("Enter title: ")
    TITLE = "This is title"
    FORMULA = SIZE / 1048576

    HTML_EXTRA = ""
    HTML_ROW = "<div class=\"row\">"
    HTML_ROW_CONTENT = "\t\t\t\t<div class=\"row-content\">"

    IMG_COUNTER = 0
    ROW_COUNTER = 0
    HTML_EXTRA += HTML_ROW + "\n"

    for img in HTML_IMG_SRC:
        HTML_EXTRA += HTML_ROW_CONTENT
        HTML_EXTRA += "\n\t\t\t\t\t<img src=\""
        HTML_EXTRA += HTML_IMG_SRC[IMG_COUNTER]
        HTML_EXTRA += "\" />\n"
        HTML_EXTRA += "\t\t\t\t</div>"
        if IMG_COUNTER + 1 < len(HTML_IMG_SRC):
            HTML_EXTRA += "\n"
        IMG_COUNTER += 1
        ROW_COUNTER += 1

        print("ROW COUNTER " + str(ROW_COUNTER) + "  IMG COUNTER + 1  " + str(IMG_COUNTER + 1))

        if ROW_COUNTER < 3 and IMG_COUNTER == len(HTML_IMG_SRC):
            print("PREKUCO")
            HTML_EXTRA += "\n\t\t\t</div>"

        if ROW_COUNTER == 3:
            """print("ROW COUNTER " + str(ROW_COUNTER) + "IMG COUNTER " + str(IMG_COUNTER))"""
            HTML_EXTRA += "\t\t\t</div>\n"
            HTML_EXTRA += "\t\t\t" + HTML_ROW + "\n"
            ROW_COUNTER = 0

    HTML = """<!DOCTYPE html>
    <meta charset="UTF-8">
    <title>""" + TITLE + """</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans|Raleway:300,400" rel="stylesheet" />
    <style>
    """ + STYLE + """</style>
    <main class="main">
        <div class="container">
            <header class="header"></header>
            <ul class="ul">
                <li class="li">
                    <span>""" + str(len(FILES)) + """</span>
                    <span>images</span>
                </li>
                <li class="li">
                    <span>""" + str(round(FORMULA, 2)) + """</span>
                    <span>mb</span>
                </li>
            </ul>
            <div class="col">\n\t\t\t""" + HTML_EXTRA + """\n\t\t</div>\n\t</div>\n</main>
    """

    with open(TITLE + ".html", "w") as file:
        file.write(HTML)
