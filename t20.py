from datetime import datetime

def log_output(text, file):
    """Helper function to log output on screen and write to file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
    log_line = f"[{timestamp}] {text}"
    print(log_line)
    file.write(log_line + "\n")

def overs_simplification(b):
    """Convert overs from float format (e.g., 12.3) into decimal format (e.g., 12.5)."""
    b_str = str(b)
    integer_part, decimal_part = b_str.split(".") if "." in b_str else (b_str, "0")
    a1 = int(integer_part)  # Convert integer part
    b1 = int(decimal_part) / 6  # Convert decimal part into overs
    return {"Current Over": round(a1 + b1, 3)}
def main(a, d, s):
    """Calculate current run rate, remaining balls, and projected total score."""
    e = round(a / d, 3) if d > 0 else 0  # Avoid division by zero
    ol = round(max(0, 20 - d), 3)  # Prevent negative remaining overs
    g = int(ol * 6)  # Remaining Balls
    if s < 5 and ol < 11 and e < 7:
        h = float((ol*10) + (ol*(10-s))/2)
    elif s > 5 and ol < 10 and e > 9:
        h = float((ol*7) - (ol*(10-s)))
    else:
        h = float((ol*e)+((10-s)*ol))/(s+1)  # fire power remaining
    i = int(a + h)+((2*ol))  # Projected Total Score
    return {
        "Current Runrate": e,
        "Remaining Balls": g,
        "Fire power": h,
        "Total Score if no more wickets don't fall": i,
        "Remaining Overs": ol,
    }
def prediction(a, b, d, e, h, i):
    """Predict score range based on the current game stage."""
    if b > 10:
        j, k = 20 - d, 0  # Last 10 overs, middle phase over
    elif b < 10:
        k, j = 10 - d, 10  # Middle overs left, 10 overs remaining
    else:
        k, j = 0, 10  # Exact transition to last phase
    i = int(i)
    fr = int(a + h)
    l = int((e * d) + (e * k) + (8 * j))  # Mid-range prediction
    m = int((e * d) + (e * k) + (12 * j))  # High-range prediction
    return {
        "no wik loss": i,
        "Current situation":fr,
        "Low estimate": l,
        "High estimate": m
    }
def chase(a, c, ol):
    """Calculate runs needed and required run rate for chase."""
    n = c - a  # Runs needed
    o = round(n / ol, 3) if ol != 0 else float('inf')  # Avoid division by zero
    return {
        "Runs needed": n,
        "Required runrate(RRR)": o,
    }
def range_prediction(a, e, ol):
    """Calculate score predictions at different run rates."""
    results = {}
    run_rate = e
    while run_rate < 15:
        p = int(ol * run_rate)
        q = a + p
        results[f"At run-rate {run_rate:.1f}"] = f"[{p}]  {q}"
        run_rate += 1  # Increment by 1
    return results
def status(b, e, o, fr, c):
    """Determine the match status based on run rate and target."""
    r = int(c - fr)
    if b == 20:
        status_msg = "Game Over"
    elif e >= o:
        status_msg = "At winning position"
    elif o > 36:
        status_msg = "Impossible to WIN"
    else:
        status_msg = f"Losing by {abs(r)} runs"

    return {"\nCURRENT STATUS OF GAME": status_msg}
def Innings():
    """Main function to handle user input and run predictions."""
    with open(r"D:\t20_output.txt", "a") as f:  # log file
        print(" Welcome to ODI Cricket Prediction")
        print(" Select operation:")
        print("         1. 1st Inning {Setting the target}")
        print("         2. 2nd Inning {Chasing the target}")
        choice = input("\nEnter choice (1 or 2): ")
        if choice not in ['1', '2']:
            print("Invalid choice. Please restart and enter 1 or 2.")
            return
        a = int(input("Please enter current score: "))
        b = float(input("Please enter current over: "))
        s = int(input("Please enter number of wicket fallen:"))
        result_0 = overs_simplification(b)
        d = result_0["Current Over"]
        result_1 = main(a, d, s)
        for key, value in result_1.items():
            print(f"   {key:<30}: {value}")
        e = result_1["Current Runrate"]
        ol = result_1["Remaining Overs"]
        i = result_1["Total Score if no more wickets don't fall"]
        h = result_1["Fire power"]
        if choice == '1':  # 1st Innings
            if b < 20:
                result_2 = prediction(a, b, d, e, h, i)
                for key, value in result_2.items():
                    log_output(f"   {key:<30}: {value}",f)

                result_3 = range_prediction(a, e, ol)
                for key, value in result_3.items():
                    print(f"   {key:<30}: {value}")
        elif choice == '2':  # 2nd Innings
            if b < 20:
                c = int(input("Please enter chase target: "))
                result_5 = chase(a, c, ol)
                for key, value in result_5.items():
                    print(f"   {key:<30}: {value}")
            result_6 = prediction(a, b, d, e, h, i)
            for key, value in result_6.items():
                log_output(f"   {key:<30}: {value}",f)
            fr = result_6["Current situation"]
            if b < 20:
                result_7 = range_prediction(a, e, ol)
                for key, value in result_7.items():
                    print(f"   {key:<30}: {value}")
            o = result_5["Required runrate(RRR)"] if b < 20 else None
            i = result_1["Total Score if no more wickets don't fall"]
            result_8 = status(b, e, o, fr, c) if b < 20 else {"CURRENT STATUS OF GAME": "Game Over"}
            for key, value in result_8.items():
                log_output(f"   {key:<30}: {value}\n",f)
if __name__ == "__main__":
    Innings()