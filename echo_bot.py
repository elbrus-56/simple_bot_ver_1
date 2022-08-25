import requests
import misc
# import json
import yobit


token = misc.token
url = "https://api.telegram.org/bot" + token + "/"
LAST_UPDATE_ID = 0

def get_updates():
	return requests.get(url + "getUpdates").json()

def get_messages():
	data = get_updates()
	last_object = data["result"][-1]
	cur_update_id = last_object["update_id"]
	global LAST_UPDATE_ID
	if LAST_UPDATE_ID != cur_update_id:
		LAST_UPDATE_ID = cur_update_id
		chat_id = last_object["message"]["chat"]["id"]
		msg_txt = last_object["message"]["text"]
		message = {"chat_id": chat_id,
				"text": msg_txt }
		return message
	return None

def send_messages(chat_id, text="Подождите немного!"):
	return requests.get(url + f"sendMessage?chat_id={chat_id}&text={text}")


def main():
	# d = get_updates()
	# with open("get_updates.json", "w") as file:
	# 	json.dump(d, file, indent = 2, ensure_ascii=False)
	while True:
		answer = get_messages()
		if answer != None:
			chat_id = answer['chat_id']
			text = answer["text"]
			lst_btc = ["скажи курс битка","курс битка","курс биткойна", "btc"]
			lst_usd = ["скажи курс доллара","курс доллара","курс бакса", "usd"]
			if text in lst_btc:
				send_messages(chat_id, yobit.get_btc_usd())
			elif text in lst_usd:
				send_messages(chat_id, yobit.get_usd_rur())
			else:
				continue
		
	
if __name__ == "__main__":
	main()