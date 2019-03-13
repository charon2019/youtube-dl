# coding: utf-8
from __future__ import unicode_literals

from .nuevo import NuevoBaseIE
from pprint import pprint


class PornVideosIE(NuevoBaseIE):
    _VALID_URL = r'https?://(?:www\.)?pornvideos\.rs/video/(?P<id>[0-9a-zA-Z\-]*)'
    _TEST = {
        'url': 'http://www.pornvideos.rs/video/amateur-skinny-girl-almost-paralized-by-horse-sized-cock-tearing-her-pussy-apart',
        'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        'info_dict': {
            'id': 'amateur-skinny-girl-almost-paralized-by-horse-sized-cock-tearing-her-pussy-apart',
            'ext': 'mp4',
            'title': 'Amateur Skinny Girl Almost Paralized by Horse Sized Cock Tearing Her Pussy Apart',
            'thumbnail': 'http://www.pornvideos.rs/thumbs/0c8832edc6b87d609210572b562d8b2d.jpg',
        }
    }

    def _real_extract(self, url):
        display_id = self._match_id(url)
        webpage = self._download_webpage(url, display_id)
        video_id = self._search_regex(
            r'<iframe.*src=".*/embed/(\d+)"', webpage, 'video id')

        info = self._extract_nuevo(
            'https://www.nonktube.com/media/nuevo/econfig.php?key=%s'
            % video_id, video_id)
        info['age_limit'] = 18
        pprint(info)
        return info
