def main():
    bet = float(input("Bet: "))
    odds = float(input("Odds: "))
    payout = calculate_payout(bet, odds)
    profit = calculate_profit(payout, bet)
    risk = classify_risk(odds)

    print(f"Bet: ₦{bet:,.2f}\nOdds: {odds}\nPayout: ₦{payout:,.2f}\nProfit: ₦{profit:,.2f}\nRisk: {risk}\n",end="") 

def calculate_payout(bet, odds):
    payout = bet * odds
    return payout

def calculate_profit(payout, bet):
    return payout - bet

def classify_risk(odds):
    if odds < 1.5:
        return "Low risk"
    elif 1.5 <= odds <= 3.0:
        return "Medium risk"
    elif odds > 3.0:
        return "High risk"


if __name__ == "__main__":
    main()