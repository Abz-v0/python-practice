def main():
    name = input("Customer name: ").strip().title()
    amount = int(input("Amount owed: "))
    days = float(input("Days overdue: "))
    message = generate_reminder(name, amount, days)
    print(message)


def generate_reminder(name, amount, days):
    # Gentle reminder
    if 1 <= days <= 7:
        return (f"Hello {name}, just a friendly reminder that you have an outstanding debt of ₦{amount:,.2f}.Please settle at your earliest convenience. Thank you!")
    
    # Firmer reminder
    elif 8 <= days <= 30:
        return (f"Dear {name}, we noticed that your debt of ₦{amount:,.2f} is now overdue. Please prioritize this payment to avoid further action. Contact us if there are any issues.")   
    
    # Urgent reminder
    elif days > 30:
        return (f"URGENT: {name}, your debt of ₦{amount:,.2f} is severely overdue. Immediate payment is required. Please contact us today to resolve this matter.")
    else:
        return (f"Thank you, {name}! We appreciate your consistent and timely payments. Your business means a lot to us. Looking forward to working with you!")
    
main()