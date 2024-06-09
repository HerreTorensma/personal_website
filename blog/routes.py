from flask import Blueprint, render_template, redirect, url_for
import os
import frontmatter
import markdown
from . import utils

ARTICLES_DIRECTORY = "articles"

blog = Blueprint("blog", __name__)

@blog.route("/")
def articles():
    articles = utils.get_all_articles_metadata(ARTICLES_DIRECTORY)

    all_tags = utils.get_all_tags(ARTICLES_DIRECTORY)

    return render_template("articles.html", articles=articles, all_tags=all_tags)

@blog.route("/articles/<slug>")
def article(slug):
    path = os.path.join(ARTICLES_DIRECTORY, f"{slug}.md")
    
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            article = frontmatter.load(file)
            html_content = markdown.markdown(article.content)

            return render_template("article.html", metadata=article.metadata, content=html_content)

    return redirect(url_for("blog.articles"))

@blog.route("/tag/<tag>")
def tag(tag):
    # Display all articles with a certain tag
    articles = utils.get_all_articles_with_tag(ARTICLES_DIRECTORY, tag)

    return render_template("tag.html", tag=tag, articles=articles)