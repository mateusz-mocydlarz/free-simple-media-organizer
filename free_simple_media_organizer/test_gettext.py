# -*- coding: utf-8 -*-
import gettext

pl = gettext.translation('base', localedir='free_simple_media_organizer/locales', languages=['pl','en'])
pl.install()

_ = pl.gettext

def wiadomosc():
    print(_("Test message!"))

# msgfmt -o free_simple_media_organizer/locales/pl/LC_MESSAGES/base.mo free_simple_media_organizer/locales/pl/LC_MESSAGES/base

if __name__ == "__main__":
    wiadomosc()