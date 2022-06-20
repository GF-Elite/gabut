import re, requests, bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()

user = input("masukan id : ")
pw = input("masukan sandi : ")

try:
	url = ses.get("https://mbasic.facebook.com/login.php")
	data = {
		"lsd":re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),
		"jazoest":re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
		"m_ts":re.search('name="m_ts" value="(.*?)"', str(url.text)).group(1),
		"li":re.search('name="li" value="(.*?)"', str(url.text)).group(1),
		"try_number": "0", 
		"unrecognized_tries": "0", 
		"email": user, 
		"pass": pw, 
		"login": "Masuk",
		"bi_xrwh": "0"}
	post = ses.post("https://mbasic.facebook.com/login.php",data=data)
	if "c_user" in ses.cookies.get_dict():
		print("akun ok")
	elif "checkpoint" in ses.cookies.get_dict():
		parsing1 = parser(post.text,"html.parser")
		action1 = parsing1.find("form",{"method":"post"})["action"]
		data2 = {
			"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(post.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(post.text)).group(1),
			"checkpoint_data": "",
			"submit[Continue]": "Lanjutkan",
			"nh":re.search('name="nh" value="(.*?)"', str(post.text)).group(1)}
		post2 = ses.post("https://mbasic.facebook.com"+action1, data=data2)
		parsing2 = parser(post2.text,"html.parser")
		option = parsing2.find_all("option")
		if len(option) == 0:
			print("tidak ada opsi terdeteksi")
		else:
			for opsi in option:
				print(opsi.text)
	else:
		print("kata sandi salah")
except Exception as e:
	print(e)
		
