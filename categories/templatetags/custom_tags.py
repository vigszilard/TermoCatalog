from django import template

register = template.Library()


@register.filter(name='construct_youtube_link')
def construct_youtube_link(link):
    start = "https://www.youtube.com/embed/"
    parameter = "?enablejsapi=1"
    return start + link.split("https://www.youtube.com/watch?v=")[1].split("&")[0] + parameter
