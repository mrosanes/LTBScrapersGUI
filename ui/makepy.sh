#!/bin/sh

rm ../ui_*py

/usr/bin/pyrcc4 scrapers.qrc -o ../scrapers_rc.py
/usr/bin/pyuic4 SCRH.ui -o ../ui_scrh.py
/usr/bin/pyuic4 SCRV.ui -o ../ui_scrv.py

taurusuic4 -x -o ../ui_scrapersform.py scrapersform.ui
