import os
import frontmatter
import re

def get_all_articles_metadata(directory):
    all_metadata = []

    for file_name in os.listdir(directory):
        file_name_no_extension = os.path.splitext(file_name)[0]

        if file_name.endswith(".md") and re.fullmatch("^[a-z0-9_]+$", file_name_no_extension):
            path = os.path.join(directory, file_name)
            
            with open(path, "r", encoding="utf-8") as file:
                article = frontmatter.load(file)
                article.metadata["slug"] = file_name_no_extension
                # print(article.metadata)
                all_metadata.append(article.metadata)

    # Sort articles by date
    all_metadata.sort(key=lambda x: x["date"], reverse=True)

    return all_metadata

def get_all_tags(directory):
    all_tags = set()

    all_metadata = get_all_articles_metadata(directory)
    for metadata in all_metadata:
        for tag in metadata["tags"]:
            all_tags.add(tag)

    return all_tags

def get_all_articles_with_tag(directory, tag):
    metadatas_with_tag = []
    
    articles = get_all_articles_metadata(directory)
    for metadata in articles:
        if tag in metadata["tags"]:
            metadatas_with_tag.append(metadata)

    return metadatas_with_tag