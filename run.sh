#! /bin/sh
# Launch datesvc
PORT=8082
(sleep 1; xdg-open http://0.0.0.0:$PORT/now ) &
python2 src/datesvc.py $PORT 
