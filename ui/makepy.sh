#!/bin/sh
/usr/bin/pyrcc4 scrapers.qrc -o scrapers_rc.py
/usr/bin/pyuic4 SCRH.ui -o ui_scrh.py
/usr/bin/pyuic4 SCRV.ui -o ui_scrv.py

pushd ..
rm ui*py
rm scrapers_rc.py

mv ui/ui*py .
mv ui/scrapers_rc.py .
popd
