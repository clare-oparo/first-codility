#goal is to calculate the final balance of the account by the end of 2020, taking into account transactions amounts and card fees
# initialize variables to track total balance, monthly card payments, and fee waiver
# iterate over transactions
# apply monthly fees
# return final balance
def solution(A, D):
    #step 1: initialize variables
    total_balance = 0
    monthly_card_payments ={month:{"count":0, "total":0}    
    for month in range(1, 13)}

#step 2: iterate over transactions
    for amount, date in zip(A,D):
        total_balance += amount
        month = int(date.split('-')[1]) # extract the month from the date
    #update monthly card payments if it is a card payment (negative amount)
        if amount < 0:
            monthly_card_payments[month]['count'] += 1
            monthly_card_payments[month]['total'] += amount

#step three: apply monthly fees
    monthly_fee = 5
    for month, payment_info in monthly_card_payments.items():
    #check if fee waivers conditions are met
        if payment_info['count'] < 3 or payment_info['total'] > -100:
            total_balance -= monthly_fee

#step four: return final balance
    return total_balance



