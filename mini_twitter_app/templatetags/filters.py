import urllib.parse as urlparse

from django import template


register = template.Library()


@register.filter
def get_page_url(url, page_to_link):

    if not page_to_link:
        page_to_link = 1

    tpl = urlparse.urlparse(url)
    params = urlparse.parse_qs(tpl.query)
    params['page'] = str(page_to_link)

    if 'q' in params:
        # resolves encoding error on search with non latin characters
        params['q'][0] = params['q'][0].encode("utf-8")

    return tpl._replace(query=urlparse.urlencode(params, True)).geturl()
