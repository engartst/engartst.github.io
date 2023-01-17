#!/bin/sh
 EMAILID="engartst@gmail.com"
 MAIL=/tmp/mail.$$
 echo "Line 1">$MAIL
 echo "Line 2" >>$MAIL
 echo "Line 3" >>$MAIL
 ...
 mail  -s "Subject" "$EMAILID" <$MAIL
 rm -f $MAIL
