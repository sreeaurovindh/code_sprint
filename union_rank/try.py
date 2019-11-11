
from collections import defaultdict
from datetime import datetime

def amounts_to_return_users(transaction_activities):
    # Write your code here
    trans_date = transaction_activities[0]
    remaining_activities = transaction_activities[1:]
    answer_set = []
    card_transactions = defaultdict()
    for item in remaining_activities:
        details = item.split(",")
        if details[0] not in card_transactions:
            card_transactions[details[0]] = [0, 0, [item[len(details[0])+1:]]]
        else:
            card_transactions[details[0]][2].append(item[len(details[0])+1:])

    for item in card_transactions.keys():
        single_user_trans = card_transactions[item][2]
        single_user_trans.sort(key = lambda x: datetime.strptime(str(x.split(",")[2]),"%Y-%m-%d %H:%M:%S"))
        affirm_bal = 0
        user_bal = 0
        purch_amount = 0
        first_balance = 0
        is_purchased = False
        break_index = 0
        remain_bal = 0

        for index,single_transation in enumerate(single_user_trans):
            single_trans = single_transation.split(",")
            if is_purchased == False:
                marker = single_trans[0]
                if marker == "Purchase":
                    purch_amount = int(single_trans[1])
                    is_purchased = True
                if not is_purchased and marker =="Creation":
                    affirm_bal = int(single_trans[1])
                if not is_purchased and marker == "Load":
                    user_bal += int(single_trans[1])
            if is_purchased == True:
                affirm_rest_balance = purch_amount - affirm_bal
                if affirm_rest_balance < 0:
                    first_balance = user_bal
                else:
                    first_balance = user_bal - affirm_rest_balance
                break_index = index
                break

        for i in range(break_index+1,len(single_user_trans)):
            load_item =single_user_trans[i]
            single_trans = load_item.split(",")
            if single_trans[0] == 'Load':
                remain_bal += int(single_trans[1])

        if is_purchased:
            total_remainig_balance = remain_bal - affirm_bal
            if total_remainig_balance  > 0 :
                total_remainig_balance = total_remainig_balance + first_balance
            else:
                total_remainig_balance = first_balance
            if total_remainig_balance > 0 :
                answer_set.append(str(item)+"**"+str(total_remainig_balance))

    return answer_set









        #print(all_transactions)


input = ['2019-05-19','1289,Creation,120000,2019-05-18 05:30:00', '1289,Load,40000,2019-05-18 05:31:00', '510,Creation,120000,2019-05-18 02:30:00', '510,Load,50000,2019-05-18 02:31:00', '1289,Load,10000,2019-05-18 05:31:30', '361,Purchase,100000,2019-05-18 06:32:00', '361,Load,90000,2019-05-18 06:33:00', '1289,Purchase,150000,2019-05-18 05:32:00', '1289,Load,140000,2019-05-18 05:34:00', '510,Purchase,150000,2019-05-18 02:32:00', '510,Load,10000,2019-05-18 02:33:00', '510,Load,100000,2019-05-18 02:34:00', '361,Creation,120000,2019-05-18 06:30:00', '361,Load,50000,2019-05-18 06:31:00', '7,Creation,120000,2019-05-18 09:30:00', '8888,Creation,50000,2019-05-18 15:30:00', '8888,Load,50000,2019-05-18 15:35:00', '10,Creation,10000,2019-05-18 14:29:00', '10,Load,70000,2019-05-18 14:30:00', '8888,Purchase,100000,2019-05-18 15:40:00', '8888,Load,50000,2019-05-18 15:47:00']
amounts_to_return_users(input)