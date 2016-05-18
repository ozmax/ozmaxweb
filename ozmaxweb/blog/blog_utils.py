import itertools
import operator
import calendar


def get_archive(posts):
    dates = [(post.created_at.strftime("%Y"), post.created_at.strftime("%B"))
             for post in posts]

    def accumulate(l):
        it = itertools.groupby(dates, operator.itemgetter(0))
        for key, subiter in it:
            yield key, [(key, len(list(group))) for key, group in
                        itertools.groupby([item[1] for item in subiter])]
    return list(accumulate(dates))


def month_num_from_name(month_name):
    correspondence = {calendar.month_name[i]: i for i in range(1, 13)}
    try:
        month = correspondence[month_name]
    except KeyError:
        month = None
    return month


def sanitize_year(year):
    try:
        year = int(year)
    except ValueError:
        year = None
    return year


def filter_posts(posts, tag=None, year=None, month=None):
    filter_term = None
    if year and month:
        filter_term = '%s - %s' % (month, year)
        month = month_num_from_name(month)
        year = sanitize_year(year)
        if month and year:
            posts = posts.filter(created_at__year=year,
                                 created_at__month=month)
        else:
            posts = posts.none()
    if tag:
        filter_term = tag
        posts = posts.filter(categories__name=tag)
    return posts, filter_term


def cut_more(posts):
    for post in posts:
        if "&lt;!-- more --&gt;" in post.content:
            post.content = post.content.split("&lt;!-- more --&gt;")[0]
            post.has_more = True
    return posts


def clean_more(post):
    if "&lt;!-- more --&gt;" in post.content:
        post.content = ''.join(part for part in
                               post.content.split("&lt;!-- more --&gt;"))
    return post
