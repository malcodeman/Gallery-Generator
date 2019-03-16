"The OS module in Python provides a way of using operating system dependent functionality."
import os


def get_cwd_images():
    "Gets all images in current working directory"
    # Extension whitelist
    extensions = [".jpg", ".png", ".JPG", ".gif"]
    images = [image
              for image in os.listdir(".")
              if os.path.isfile(image)
              if image.endswith(tuple(extensions))]
    return images


def bytes_to_megabytes(size):
    "Converts bytes to megabytes"
    # 1 Megabyte = 1,048,576 Bytes
    return size / 1048576


def get_cwd_name():
    "Gets current working directory name"
    return os.path.basename(os.getcwd())


def get_css():
    "Gets css"
    with open('style.css', 'r') as style:
        css = style.read()
        return css


def save_html(title, html):
    "Saves file as html"
    with open(title + ".html", "w") as file:
        file.write(html)


def main():
    "Main function"
    images = get_cwd_images()
    post_urls = []
    size_b = 0
    for image in images:
        print(os.path.realpath(image))
        post_urls.append(image)
        size_b += os.path.getsize(os.path.realpath(image))
    size_mb = bytes_to_megabytes(size_b)
    title = get_cwd_name() + " gallery"
    style = get_css()
    posts = ""
    for post_url in post_urls:
        posts += f"""<div class="post"><img src={post_url} /></div>"""
    html = f"""
    <!DOCTYPE html>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>{style}</style>
    <div class="page">
      <div class="container">
        <ul class="ul">
          <li class="li">
            <span>{str(len(images))}</span>
            <span>images</span>
          </li>
          <li class="li">
            <span>{str(round(size_mb, 2))}</span>
            <span>mb</span>
          </li>
        </ul>
        <main><div class="grid">{posts}</div></main>
      </div>
    </div>
    """
    save_html(title, html)


if __name__ == "__main__":
    main()
