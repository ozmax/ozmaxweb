import itertools
import operator


def get_archive(posts):
	dates = [(post.created_at.strftime("%Y"), post.created_at.strftime("%B")) for post in posts]
	def accumulate(l):
	    it = itertools.groupby(dates, operator.itemgetter(0))
	    for key, subiter in it:
	        yield key, [(key, len(list(group))) for key, group in itertools.groupby([item[1] for item in subiter])]
	return list(accumulate(dates))
