import random

monthly_payment = int(input('Podaj comiesięczny wkład: '))

funds = int(input('Podaj fundusz startowy: '))

years_of_investment = float(input('Podaj w latach długość inwestowania: '))

simulation_growth = float(input('Podaj punkty procentowe dziennej zmiany: '))

simulation_declaration = input('Czy symulować wachania? ')

self_input = funds

swing_height = 0

if simulation_declaration == 'tak' or simulation_declaration == 'yes' or simulation_declaration == 'TAK' or simulation_declaration == 'YES':
    simulation_declaration = True
    swing_height = int(input("Podaj skale symulowanych wachań(1 - małe, 99 - ogromne): "))




#######################  SYMULACJA WACHAŃ ########################
def simulation_swings(current_growth):
    return current_growth*random.randint(100 - swing_height, 100 + swing_height)*0.01



#######################  KALKULOWANIE ############################   
def calculator(mp, f, yoi, ss, si, day = years_of_investment*12*30):
    
    day_counter = 0
    for i in range(int(yoi*12)):
        for j in range(30):
            day_counter += 1
            if simulation_declaration:
                ss = simulation_swings(ss)
                
            increase = f*ss*0.01
            f += increase
            if day_counter == day: return({'funds':f, 'self_input':si})
        f += mp
        si += mp
    return({'funds':f, 'self_input':si})

result = calculator(monthly_payment, funds, years_of_investment, simulation_growth, self_input)

print(result['funds'])




#######################  TWORZENIE TABELI #######################
width = 200

#Prosta skala czasowa na dole ekranu
map = ['DAY 1']
for i in range(width - 4): map[0] += ' '
map[0] += 'DAY ' + str(years_of_investment*12*30)


x_scale = ((years_of_investment*12*30)/width)
y_scale = 100/result['funds']
#RYSOWANIE GRAFU

for i in range(int(result['funds']*y_scale)):
    map.append('.')
    result_placeholder = ''
    for j in range(width):

                                                                                                                        #przypisywanie x i y
        x = int(x_scale*j)
                                                                                                 #x jest powtórzeniem pętli pomnozonym przez skale mapy
        local_result = calculator(monthly_payment, funds, years_of_investment, simulation_growth, self_input, x)        #
        y = int(local_result['funds']*y_scale)
        y_placeholder = int(local_result['funds'])                                                                                  #y jest wynikiem dla danego dnia
        if y == i: #x==j
            result_placeholder = y_placeholder
            map[i+1] += '*'
            print('x: ', x, 'y: ', y)
        else:
            map[i+1] += ' '
    map[i+1] += '.   ' + str(result_placeholder)


#######################  RYSOWANIE TABELI ########################
for i in range(len(map), 0, -1):                                                                                        #finalne wyświetlenie grafu 
    print(map[i-1])

final_result = calculator(monthly_payment, funds, years_of_investment, simulation_growth, self_input)

print('Ostateczna kwota po ', years_of_investment, 'latach to: ', final_result['funds'])
print('Wkład własny: ', final_result['self_input'])
#print(map)

