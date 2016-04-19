# Create virtualenv
VENV_NAME="fonodoc"
mkvirtualenv -p /usr/bin/python3 $VENV_NAME

# Link global pyqt5 with the virtualenv
LIBDIR="$HOME/.virtualenvs/$VENV_NAME/lib/python3.4/site-packages"
ln -s /usr/lib/python3/dist-packages/PyQt5 "$LIBDIR/PyQt5"
ln -s /usr/lib/python3/dist-packages/sip.cpython-34m-*.so "$LIBDIR/"
