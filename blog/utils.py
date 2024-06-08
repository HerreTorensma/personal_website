import os
import frontmatter

def get_all_articles_metadata(directory):
    all_metadata = []

    for file_name in os.listdir(directory):
        if file_name.endswith(".md"):
            path = os.path.join(directory, file_name)
            
            with open(path, "r", encoding="utf-8") as file:
                article = frontmatter.load(file)
                all_metadata.append(article.metadata)

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