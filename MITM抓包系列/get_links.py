# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
from mitmproxy import http
import re
from urllib.parse import urljoin
def response(flow:http.HTTPFlow):
    if "Content-Type" in flow.response.headers and flow.response.headers["Content-Type"].find("text/html") != -1:
        pageUrl = flow.request.url
        pageText = flow.response.text
        pattern = (r"<a\s+(?:[^>]*?\s+)?href=(?P<delimiter>[\"'])"
                   r"(?P<link>(?!https?:\/\/|ftps?:\/\/|\/\/|#|javascript:|mailto:).*?)(?P=delimiter)")
        rel_matcher = re.compile(pattern, flags=re.IGNORECASE)
        rel_matches = rel_matcher.finditer(pageText)
        for match_num, match in enumerate(rel_matches):
            (delimiter, rel_link) = match.group("delimiter", "link")
            abs_link = urljoin(pageUrl, rel_link)
            print('LINKS:'+abs_link)
            # LINKS:http://bbs.kjj.com/space.php?username=%BB%F9%BD%F0%CA%D6
            # LINKS:http://bbs.kjj.com/redirect.php?tid=655201&amp;goto=lastpost#lastpost
            # LINKS:http://bbs.kjj.com/space-username-gtthc.html
            # LINKS:http://bbs.kjj.com/forum-154-1.html
            # LINKS:http://bbs.kjj.com/forum-154-1.html
            # LINKS:http://bbs.kjj.com/space.php?username=%B4%BA%C8%D5%D4%D8%D1%F4
            # LINKS:http://bbs.kjj.com/redirect.php?tid=968702&amp;goto=lastpost#lastpost
            # LINKS:http://bbs.kjj.com/space-username-%C0%B6%CC%EC%B7%E3.html
            # LINKS:http://bbs.kjj.com/forum-144-1.html
            # LINKS:http://bbs.kjj.com/forum-144-1.html
            # LINKS:http://bbs.kjj.com/space.php?username=%D4%C2%D7%ED%BB%A8%D2%F5
