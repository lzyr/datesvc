"""
datesvc provides web services around Date
python2 datesvc.py <port>
"""
import web
from datetime import date

urls = (
    '/now', 'Now',
)

web.config.debug=False
app = web.application(urls, globals())

class Now:
    def GET(self):
        now = date.today()
        """return 'Hello'"""
        strf = 'Today is %s ' % now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
        daySinceEpoch = (now - date(1970, 1, 1)).days
        stEpoch = '%s since Unix Epoch' % daySinceEpoch
        return strf + '\n' + stEpoch
        #        return """\
        #        %s
        #%s """ % (strf, stEpoch)


if __name__ == "__main__":
    app.run()
