---

# 🏏 Cricket Match Score Prediction & Tracking Portal

A cricket analytics platform that enables enthusiasts to **analyze the current match situation and predict future team performance** using real-time match parameters.

The system evaluates factors such as **current score, overs played, wickets lost, and innings context** to estimate how a team is likely to perform for the remainder of the innings. This helps users understand **match momentum, projected scores, and potential outcomes**.

The platform provides fans and analysts with a **data-driven perspective of live cricket matches**, making it easier to interpret match situations and anticipate game progression.

---

# 🚀 Features

* **Match Situation Analysis**
  Evaluates live match inputs including runs, overs, and wickets.

* **Score Prediction Engine**
  Predicts likely team performance based on current match conditions.

* **Momentum Insights**
  Helps users understand whether a team is accelerating, stabilizing, or collapsing.

* **Innings-Aware Prediction**
  Handles both **first innings score projections** and **second innings chase predictions**.

* **API-Based Prediction Service**
  Provides a simple REST API for integration with other applications or dashboards.

---

# 🧠 Prediction Inputs

The prediction model analyzes the following parameters:

| Parameter | Description                                          |
| --------- | ---------------------------------------------------- |
| `score`   | Current team score                                   |
| `overs`   | Overs completed (supports decimal format like `8.2`) |
| `wickets` | Number of wickets fallen                             |
| `innings` | Current innings (1 or 2)                             |
| `target`  | Target score (required for second innings)           |

---

# 🛠 Tech Stack

### Backend

* **Python**
* **Flask / FastAPI** (API service)

### Data Processing

* **NumPy**
* **Pandas**

### Machine Learning (if used)

* **Scikit-Learn**

### Tools

* **Git**
* **GitHub**

---

# 📡 API Usage

The prediction service exposes a REST API endpoint:

```
POST /predict
```

---

# Example API Call (cURL)

### First Innings Prediction

```bash
curl -X POST http://localhost:8600/predict \
-H "Content-Type: application/json" \
-d '{
  "score": 75,
  "overs": 8.2,
  "wickets": 2,
  "innings": 1
}'
```

---

### Second Innings Prediction (With Target)

```bash
curl -X POST http://localhost:8600/predict \
-H "Content-Type: application/json" \
-d '{
  "score": 120,
  "overs": 15.3,
  "wickets": 5,
  "innings": 2,
  "target": 165
}'
```

---

# Example Using HTTPie

```bash
http POST localhost:8600/predict \
score:=75 \
overs:=8.2 \
wickets:=2 \
innings:=1
```

---

# 📊 Use Cases

* Cricket analytics dashboards
* Match commentary tools
* Fan engagement platforms
* Live match prediction engines
* Sports data experimentation

---

# ⚙️ Running the Project

Clone the repository:

```bash
git clone https://github.com/pkg2027/cricket.git
cd cricket
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API server:

```bash
python app.py
```

The prediction API will be available at:

```
http://localhost:8600/predict
```

---

# 📌 Future Improvements

* Live score integration via cricket APIs
* Advanced machine learning prediction models
* Visualization dashboards for match momentum
* Historical match analysis

---

⭐ Contributions, feedback, and improvements are welcome!

---
<img width="1919" height="898" alt="Screenshot 2026-03-16 231312" src="https://github.com/user-attachments/assets/59e69a24-7a9c-45db-bedf-20470708b6b1" />
