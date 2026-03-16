Cricket Match Score Prediction and Tracking Portal

Developed a cricket analytics portal that allows cricket enthusiasts to analyze the current match situation and predict future team performance based on real-time match parameters. The system evaluates the current score, wickets fallen, and other match conditions to estimate how the team is likely to perform in the remaining part of the game.

The platform helps users understand match momentum and possible outcomes by analyzing the current state of the innings and generating predictive insights about final scores or performance trends. This provides fans with a deeper analytical perspective of ongoing cricket matches.

api calling (input)

example
curl -X POST http://localhost:8600/predict \
-H "Content-Type: application/json" \
-d '{
  "score": 75,
  "overs": 8.2,
  "wickets": 2,
  "innings": 1
}'
----------------------------------------------
http POST localhost:8600/predict \
score:=75 \
overs:=8.2 \
wickets:=2 \
innings:=1

----------------------------------------------
curl -X POST http://localhost:8600/predict \
-H "Content-Type: application/json" \
-d '{
  "score": 120,
  "overs": 15.3,
  "wickets": 5,
  "innings": 2,
  "target": 165
}'
