product_id = "037-00901-00027"
split = product_id.split('-')
country_code = split[0]
product_code = split[1]
batch_number = split[2]
print(" country code is = ", country_code,'\n',"Product code is = ",product_code, '\n',"batch number is =", batch_number)
