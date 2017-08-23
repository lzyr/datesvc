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
        return 'Today is %s ' % now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")


if __name__ == "__main__":
    app.run()
