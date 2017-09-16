"The OS module in Python provides a way of using operating system dependent functionality."
import os

def get_cwd_images():
    "Gets all images in current working directory"
    #only these extensions count
    extensions = [".jpg", ".png", ".JPG", ".gif"]
    images = [image
              for image in os.listdir(".")
              if os.path.isfile(image)
              if image.endswith(tuple(extensions))]
    return images

def bytes_to_megabytes(size):
    "Converts bytes to megabytes"
    #1 Megabyte = 1,048,576 Bytes
    return size / 1048576

def get_cwd_name():
    "Gets current working directory name"
    return os.path.basename(os.getcwd())

def get_css():
    "Gets css"
    css = """    a {
	text-decoration: none;
    }

    body,
    h1,
    h2,
    h3,
    p {
        margin: 0;
    }

    ul {
        margin: 0;
        padding-left: 0;
    }

    .page {
        background-color: #fafafa;
    }

    .container {
        margin: 0 auto;
        max-width: 992px;
    }

    .ul {
        display: flex;
        justify-content: space-around;
        list-style-type: none;
        padding: 1rem;
    }

    .li {
        display: flex;
        flex-direction: column;
        text-align: center;
    }


    /* Numbers */

    .li span:nth-child(1) {
        color: #131313;
        font: 300 1rem/1 Roboto;
    }


    /* Text */

    .li span:nth-child(2) {
        color: #999;
        font: 300 .8rem/1 Roboto;
    }

    .row {
        display: flex;
        margin-bottom: .4rem;
    }


    /* Removes margin bottom from last row in column */

    .row:last-child {
        margin-bottom: 0;
    }


    /* Aspect ratio problem https://css-tricks.com/aspect-ratio-boxes/ */

    .row-item {
        flex-grow: 1;
        margin-right: .4rem;
        position: relative;
    }

    .row-item::before {
        content: "";
        display: block;
        padding-top: 100%;
    }


    /* Removes margin right from last row item in row */

    .row-item:last-child {
        margin-right: 0;
    }

    .row-item img {
        height: 100%;
        left: 0;
        object-fit: cover;
        position: absolute;
        top: 0;
        width: 100%;
    }"""
    return css


def save_html(title, html):
    "Saves file as html"
    with open(title + ".html", "w") as file:
        file.write(html)

def main():
    "Main function"
    images = get_cwd_images()
    html_img_src = []
    size_b = 0
    for image in images:
        #prints folder path, name, type
        print(os.path.realpath(image))
        #adds image to array
        html_img_src.append(image)
        #increments total image size in bytes
        size_b += os.path.getsize(os.path.realpath(image))
    #converts total image size from bytes to megabytes
    size_mb = bytes_to_megabytes(size_b)
    #four tabs is a must
    html_row = "\t\t\t\t<div class=\"row\">"
    #five tabs is a must
    html_row_item = "\t\t\t\t\t<div class=\"row-item\">"
    img_counter = 0
    row_item_counter = 0
    html_main = ""
    #adds first row
    html_main += html_row + "\n"
    for _ in html_img_src:
        #adds row item
        html_main += html_row_item + "\n"
        #adds image
        html_main += "\t\t\t\t\t\t<img src=\"" + html_img_src[img_counter] + "\" />" + "\n"
        #closes row-item
        html_main += "\t\t\t\t\t</div>" + "\n"
        img_counter += 1
        row_item_counter += 1
        #if three row items are added, add new row
        if row_item_counter == 3 and img_counter != len(html_img_src):
            #closes previous row
            html_main += "\t\t\t\t</div>" + "\n"
            #adds new row
            html_main += html_row + "\n"
            #resets row item counter
            row_item_counter = 0
    #closes last row
    html_main += "\t\t\t\t</div>"
    title = get_cwd_name() + " gallery"
    style = get_css()
    html = """<!DOCTYPE html>
<meta charset="UTF-8">
<title>""" + title + """</title>
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" />
<style>\n""" + style + """\n\t</style>
    <div class="page">
        <div class="container">
            <ul class="ul">
                <li class="li">
                    <span>""" + str(len(images)) + """</span>
                    <span>images</span>
                </li>
                <li class="li">
                    <span>""" + str(round(size_mb, 2)) + """</span>
                    <span>mb</span>
                </li>
            </ul>
            <main>\n""" + html_main + """
            </main>
        </div>
    </div>"""
    save_html(title, html)

if __name__ == "__main__":
    main()
