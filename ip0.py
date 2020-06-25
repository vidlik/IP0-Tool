import requests 
import socket  
import pyfiglet 

result = pyfiglet.figlet_format("IP0 Tool", font = "slant" ) 
print(result) 


print(requests.get('http://ip.42.pl/raw').text + '<-- ваша IP-адреса')
 
global get_ip
get_ip = input('Введіть IP: ')

def info():
	response = requests.get( f'http://ipinfo.io/{get_ip}/json')

	user_ip = response.json()[ 'ip' ]
	user_city = response.json()[ 'city' ]
	user_region = response.json()[ 'region' ]
	user_country = response.json()[ 'country' ]
	user_location = response.json()[ 'loc' ]
	user_org = response.json()[ 'org' ]
	user_timezone = response.json()[ 'timezone' ]

	global all_info
	all_info = f'\n-ІНФОРМАЦІЯ-\nIP : {user_ip}\nМісто : {user_city}\nКраїна : {user_country}\nЛокація : {user_location}\nОрганізація : {user_org}\nЧасовий пояс : {user_timezone}'

	print(all_info)

def record():
	user_record = input('\nЗаписати? (y/n)(y-так, n-ні) :')

	if user_record == 'y':
		file = open('запис.txt', 'a')
		file.write(f'{all_info}\n')
		file.close()

		print('\nУспішно!')

	if user_record == 'n':
		print('\nOK')

def main():
	info()
	record()
main()
