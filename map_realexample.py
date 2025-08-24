
#map_real_world_example


employees= [{"name":"Archana","salary":10000},{"name":"Anjitha","salary":350000},{"name":"Akshara","salary":15000}]
tax_rate= .25
tax_list=list(map(lambda emp: emp["salary"]*tax_rate,employees))
print(tax_list)