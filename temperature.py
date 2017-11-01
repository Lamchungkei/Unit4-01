# Created by: Kay Lin 
# Created on: 30th-Oct-2017
# Created for: ICS3U
# This program displays Celsius converts to Farenheit,
# but Celsius the user can enter different number

def farenheit(temperature):
    tf = ((1.8 * tc + 32))
    print('The temperature in farenheit is ' + str(tf))
    
tc = input( 'Enter a temperature in Celsius: ' )
farenheit(tc)

