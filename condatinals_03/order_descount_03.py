#program to check for order discount
#inputs
item_cost = 500
item_qty = 3
special_client = 1          #1. special           0> not special


#processing
total_order_cost = item_cost * item_qty
discount_pct = 0
if total_order_cost >= 1000:
    if special_client == 1:   #special
        discount_pct = 20
    else:
        discount_pct = 10

discount_val = discount_pct / 100 * total_order_cost
print("total_order_cost before discount = ", total_order_cost )
total_order_cost = total_order_cost - discount_val  #   هنا سطر الخصم


print("discount pct = ", discount_pct)
print("discount value = ", discount_val)
print("total order cost after discount = ", total_order_cost)

