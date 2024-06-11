import os
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional

import dateutil.parser
import frontmatter
import humanize
import jinja2
import mistune
import mistune.toc
import pygments
import pygments.formatters.html
import pygments.lexers
import yaml
from markdown_it import MarkdownIt
from mdit_plain.renderer import RendererPlain

FILE_DIRECTORY = os.path.abspath("public")


class SyntaxHighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if not info:
            return "\n<pre><code>%s</code></pre>\n" % mistune.escape(code)
        info = info.split()
        lang = info[0]

        if lang == "mermaid":
            return """\n<pre class="mermaid">%s</pre>\n""" % mistune.escape(code)

        try:
            lexer = pygments.lexers.get_lexer_by_name(lang, stripall=True)
            formatter = pygments.formatters.html.HtmlFormatter(lineseparator="<br>")
            return pygments.highlight(code, lexer, formatter)
        except pygments.util.ClassNotFound:
            return code

    def inline_html(self, html):
        return "<pre>" + html + "</pre>"


def list_files(*directories):
    out = []

    for directory in directories:
        for root, _, files in os.walk(directory):
            for filename in files:
                ext = os.path.splitext(filename)[1][1:]
                out.append([ext.lower(), os.path.join(root, filename)])
    return out


renderer = SyntaxHighlightRenderer(escape=False)
markdown = mistune.Markdown(renderer=renderer)
plain_parser = MarkdownIt(renderer_cls=RendererPlain)


def parse_markdown(filename) -> Optional[Dict]:
    with open(filename, "r") as fp:
        data = frontmatter.load(fp)
        content_filtered = data.content.replace("<!--more-->", "")
        mistune.toc.add_toc_hook(markdown)
        content, state = markdown.parse(content_filtered)
        toc = [(a, f"#{b}", c) for a, b, c in state.env["toc_items"]]
        teaser = plain_parser.render(data.content.split("<!--more-->")[0][:2000])
        return data, content, teaser, toc


def copy_static(path):
    for root, _, files in os.walk(path):
        for filename in files:
            full_path = os.path.join(root, filename)
            out_filename = os.path.join(
                FILE_DIRECTORY, os.path.relpath(full_path, start=path)
            )
            os.makedirs(os.path.dirname(out_filename), exist_ok=True)
            print("COPY", full_path, out_filename)
            shutil.copyfile(full_path, out_filename)


def parse_tree(**kwargs):
    return _parse_tree("content", "templates", "base", **kwargs)


def _parse_tree(path, template_dir, layout, **kwargs):
    copy_static("static")
    markdown_files = list_files("content")

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

    template = env.get_template(f"test/post.html")

    posts = []
    tags = defaultdict(list)

    formatter = pygments.formatters.html.HtmlFormatter()
    base = "https://rrx.github.io"
    main = {
        "site": {
            "base": base,
            "lang": "en",
            "highlight_styles": formatter.get_style_defs(),
            "title": "More Code, More Problems",
            "description": "A software engineering blog",
        },
        "build": kwargs,
        "links": [
            (3, "/", "Home"),
            (3, "/about", "About"),
            (3, "https://github.com/rrx", "GitHub"),
            (3, "https://www.linkedin.com/in/ryansadler/", "LinkedIn"),
        ],
    }
    main.update(kwargs)

    if kwargs.get("debug", False):
        main["links"].append((3, "/testing", "Testing"))

    for ext, f in markdown_files:
        if ext in ["jpg", "jpeg", "gif", "png", "svg"]:
            out_filename = os.path.join(FILE_DIRECTORY, os.path.relpath(f, start=path))
            print("COPY", f, out_filename)
            os.makedirs(os.path.dirname(out_filename), exist_ok=True)
            shutil.copyfile(f, out_filename)

        if ext == "md":
            data, content, teaser, toc = parse_markdown(f)
            directory = os.path.dirname(f)
            out_dir = os.path.relpath(directory, start=path)
            link_path = Path(os.path.relpath(f, start=path)).with_suffix(".html")
            parts = os.path.split(link_path)

            if parts[0] == "":
                link = str(link_path) + "/"
            else:
                link = os.path.dirname(link_path) + "/"

            if "title" in data:
                post_tags = data.get("tags", [])
                post = {
                    "source": f,
                    "title": data["title"],
                    "filename": link,
                    "date": data["date"].date(),
                    "hdate": humanize.naturaldate(
                        data["date"],
                    ),
                    "teaser": teaser,
                    "link": link,
                    "link_path": link_path,
                    "tags": post_tags,
                    "toc": toc,
                    "content": content,
                    "is_post": parts[0].startswith("posts"),
                }

                if "thumbnail" in data:
                    post["thumbnail"] = os.path.join(base, out_dir, data["thumbnail"])

                if "author" in data:
                    post["author"] = data["author"]

                posts.append(post)

                for tag in post_tags:
                    tags[tag].append(post)

    out_posts = []
    for post in posts:
        kwargs = dict(
            tags=sorted(tags.keys()),
            toc=post["toc"],
            post=post,
            image=post.get("thumbnail"),
            title=post["title"],
            description=post["teaser"],
            **main,
        )

        html = template.render(**kwargs)
        if post["is_post"]:
            out_posts.append(post)

        build_filename = os.path.join(FILE_DIRECTORY, post["link_path"])
        os.makedirs(os.path.dirname(build_filename), exist_ok=True)
        print("COMPILE", post["source"], build_filename)
        with open(build_filename, "w") as fp:
            fp.write(html)

    kwargs = dict(
        posts=list(sorted(out_posts, key=lambda x: x["date"], reverse=True)),
        tags=sorted(tags.keys()),
        title=main["site"]["title"],
        **main,
    )

    # Home Page
    template = env.get_template("test/home.html")
    html = template.render(**kwargs)
    with open(os.path.join(FILE_DIRECTORY, "index.html"), "w") as fp:
        fp.write(html)

    # Simple templates
    for template_name in ["404.html", "test_page.html"]:
        template = env.get_template(os.path.join("pages", template_name))
        html = template.render(**kwargs)
        with open(os.path.join(FILE_DIRECTORY, template_name), "w") as fp:
            fp.write(html)

    for tag, posts in tags.items():
        template = env.get_template("test/tag.html")
        build_filename = os.path.join(FILE_DIRECTORY, "tags", tag) + ".html"
        kwargs = dict(
            title=tag,
            posts=list(sorted(posts, key=lambda x: x["date"], reverse=True)),
            tags=sorted(tags.keys()),
            **main,
        )

        html = template.render(**kwargs)
        os.makedirs(os.path.dirname(build_filename), exist_ok=True)
        with open(build_filename, "w") as fp:
            fp.write(html)
