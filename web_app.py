from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path

import t20

# -------------------------------------------------
# Paths
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
DASHBOARD_HTML = TEMPLATES_DIR / "dashboard.html"

# -------------------------------------------------
# App
# -------------------------------------------------
app = FastAPI(title="T20 Match Intelligence")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# -------------------------------------------------
# Routes
# -------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def dashboard():
    if not DASHBOARD_HTML.exists():
        raise HTTPException(status_code=500, detail="dashboard.html not found")

    return DASHBOARD_HTML.read_text(encoding="utf-8", errors="ignore")


@app.post("/predict")
def predict(payload: dict):
    """
    Payload from dashboard.js:
    {
      score: int,
      overs: float,
      wickets: int,
      innings: 1 | 2,
      target?: int
    }
    """

    try:
        score = payload["score"]
        overs = payload["overs"]
        wickets = payload["wickets"]
        innings = payload["innings"]
        target = payload.get("target")

        # -------- Overs conversion --------
        over_data = t20.overs_simplification(overs)
        current_over = over_data["Current Over"]

        # -------- Main metrics --------
        main_data = t20.main(score, current_over, wickets)
        runrate = main_data["Current Runrate"]
        remaining_overs = main_data["Remaining Overs"]
        firepower = main_data["Fire power"]
        projected_total = main_data["Total Score if no more wickets don't fall"]

        # -------- Prediction --------
        prediction_data = t20.prediction(
            score,
            overs,
            current_over,
            runrate,
            firepower,
            projected_total
        )

        response = {
            "main": main_data,
            "prediction": prediction_data
        }

        # -------- 2nd Innings logic --------
        if innings == 2 and target is not None:
            chase_data = t20.chase(score, target, remaining_overs)
            rrr = chase_data["Required runrate(RRR)"]

            status_data = t20.status(
                overs,
                runrate,
                rrr,
                prediction_data["Current situation"],
                target
            )

            response["chase"] = chase_data
            response["status"] = status_data

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
