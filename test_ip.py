import os
import subprocess
import telebot

bot = telebot.TeleBot('your_token')

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, check_new_ip())
	
def check_new_ip():
	check_new_ip = subprocess.run(['curl', '2ip.ru'],
								stdout=subprocess.PIPE)
	new_ip = (check_new_ip.stdout.decode('utf-8')).rstrip('\n')
	compare_ip(new_ip)
	return new_ip

def compare_ip(new_ip):
	ip_address_file = open('ip_address', 'r')
	old_ip = (ip_address_file.readline()).rstrip('\n')
	ip_address_file.close()
	if new_ip != old_ip:
		ip_address_file = open('ip_address', 'w')
		ip_address_file.write(new_ip + '\n')
		ip_address_file.close()
		
bot.polling()
