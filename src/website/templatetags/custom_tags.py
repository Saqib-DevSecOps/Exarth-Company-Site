from django import template

register = template.Library()

@register.filter
def image_or_placeholder(image, placeholder=None):
    if image:
        return image.url

    if placeholder:
        return f"https://placehold.co/{placeholder}"
    return "https://placehold.co/100"