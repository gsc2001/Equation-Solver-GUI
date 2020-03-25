python3 server/server.py 7 &
cd gui
npm start
kill $(lsof -t -i:5000)
