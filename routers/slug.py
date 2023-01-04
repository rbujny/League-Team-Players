from slugify import slugify
def name_to_slug(name: str):
    slug = slugify(name)
    print(slug)
    return slug
