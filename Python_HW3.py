int_item = 10
print('int_item = ',int_item)

comp_item = 18
print('comp_item = ',comp_item)

mult_int = int_item * 2
print('mult_int = ',mult_int)

item_2 = True
print('item_2 = ',item_2)

item_3 = False
print('item_3 = ',item_3)

item_4 = 0
print('item_4 = ',item_4)

item_5 = 1
print('item_5 = ',item_5)

usd_item = 'usd'
print('usd_item = ',usd_item)
usd_usd_rate = 1
print('usd_usd_rate = ',usd_usd_rate)

eur_item = 'eur'
print('eur_item = ',eur_item)
usd_eur_rate = 0.86
print('usd_eur_rate = ',usd_eur_rate)

uah_item = 'uah'
print('uah_item = ', uah_item)
usd_uah_rate = 26.23
print('usd_uah_rate = ',usd_uah_rate)

chf_item = 'chf'
print('chf_item = ',chf_item)
usd_chf_rate = 0.91
print('usd_chf_rate = ',usd_chf_rate)

rub_item = 'rub'
print('rub_item = ',rub_item)
usd_rub_rate = 71.88
print('usd_rub_rate = ',usd_rub_rate)

byn_item = 'byn'
print('byn_item = ',byn_item)
usd_byn_rate = 2.46
print('usd_byn_rate = ',usd_byn_rate)

print('20)  mult_int =', mult_int , '  comp_item =',comp_item)
if mult_int > comp_item : print ('Переменная mult_int больше', comp_item)

div_int = int_item / 2
print('22)  div_int =', div_int , '  comp_item =',comp_item)
if div_int < comp_item : print('Переменная div_int меньше', comp_item)

item_1 = int_item + 10
print('24)  item_1 =', item_1 , '  comp_item =',comp_item)
if item_1 < comp_item : print(('Переменная item_1 меньше', comp_item))
else: print('Переменная item_1 больше или равна', comp_item)

print('25) if item_2 ')
if item_2: print('Переменная item_2 = ', item_2)
else: print('Переменная item_2 = ', item_3)

print('26) if item_3 ')
if item_3: print('Переменная item_3 = ', item_2)
else: print('Переменная item_3 = ', item_3)

print('27) if item_5 ')
if item_5: print('Переменная item_5 = ', item_5)
else: print('Переменная item_5 = ', item_4)

print('28) if item_4 ')
if item_4: print('Переменная item_4 = ', item_5)
else: print('Переменная item_4 = ', item_4)

print('---- Currency Convertor ----')
currency_convertor = item_2
print('currency_convertor = ',currency_convertor)

# Версия 1 - 1 валюта
print('Версия 1 - 1 валюта')
if currency_convertor:
    currency_usd = usd_item
    print('currency_usd = ',currency_usd)
    target_currency = eur_item
    print('target_currency = ',target_currency)
    target_currency_amount = 50
    print('target_currency_amount = ',target_currency_amount)
    currency_result = 0

    if target_currency == "eur":
        currency_result = target_currency_amount / usd_eur_rate
        print(target_currency_amount, eur_item, ' = ', currency_result, usd_item)
    elif target_currency == "uah":
        currency_result = target_currency_amount / usd_uah_rate
        print(target_currency_amount, uah_item, " = ", currency_result, usd_item)
    elif target_currency == "chf":
        currency_result = target_currency_amount / usd_chf_rate
        print(target_currency_amount, chf_item, " = ", currency_result, usd_item)
    elif target_currency == "rub":
        currency_result = target_currency_amount / usd_rub_rate
        print(target_currency_amount, rub_item, " = ", currency_result, usd_item)
    elif target_currency == "byn":
        currency_result = target_currency_amount / usd_byn_rate
        print(target_currency_amount, byn_item, " = ", currency_result, usd_item)

    else: print("Unknow currency")
else: ('Переменная currency_convertor = ', item_3)

# Версия 2 - все валюты
print('Версия 2 - все валюты')
if currency_convertor:
    currency_usd = usd_item
    print('currency_usd = ',currency_usd)
    #target_currency = eur_item
    #print('target_currency = ',target_currency)
    target_currency_amount = 50
    print('target_currency_amount = ',target_currency_amount)
    currency_result = 0

    all_cur = ['eur', 'uah', 'chf', 'rub', 'byn']
    print(all_cur)

    for target_currency in all_cur:
        if target_currency == "eur":
            currency_result = target_currency_amount / usd_eur_rate
            print(target_currency_amount, eur_item, ' = ', currency_result, usd_item)
        elif target_currency == "uah":
            currency_result = target_currency_amount / usd_uah_rate
            print(target_currency_amount, uah_item, " = ", currency_result, usd_item)
        elif target_currency == "chf":
            currency_result = target_currency_amount / usd_chf_rate
            print(target_currency_amount, chf_item, " = ", currency_result, usd_item)
        elif target_currency == "rub":
            currency_result = target_currency_amount / usd_rub_rate
            print(target_currency_amount, rub_item, " = ", currency_result, usd_item)
        elif target_currency == "byn":
            currency_result = target_currency_amount / usd_byn_rate
            print(target_currency_amount, byn_item, " = ", currency_result, usd_item)

        else:
            print("Unknow currency")


else:
    ('Переменная currency_convertor = ', item_3)

