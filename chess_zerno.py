
chess_cell_amount = 64
zerno_weight = 5e-08     # 50 mg = 5e-08 tonn
zerno_ro = 8e+08         # tonna/km^3

S_country = 17100000     # km^2
S_region = 178200        # km^2
S_city = 502.7           # km^2

Y_country = 75000000     # ton
Y_region = 1706000       # ton

total_zerno = 1
current_cell = 1
current_zerno = 1

# print current_cell, " ", current_zerno, " ", total_zerno

while current_cell < chess_cell_amount:
    current_cell = current_cell + 1
    current_zerno = current_zerno * 2
    total_zerno = total_zerno + current_zerno
    # print current_cell, " ", current_zerno, " ", total_zerno

print "TOTAL ZEREN: ", total_zerno

total_ton = total_zerno * zerno_weight
print "TOTAL TON: ", total_ton

h_country = total_ton / (zerno_ro * S_country)
print "H Russia: ", h_country, "km"

h_region = total_ton / (zerno_ro * S_region)
print "H NSO: ", h_region, "km"

h_city = total_ton / (zerno_ro * S_city)
print "H Novosibirsk: ", h_city, "km"

year_country = total_ton / Y_country
print "Russia: ", year_country, "years"

year_region = total_ton / Y_region
print "NSO: ", year_region, "years"
