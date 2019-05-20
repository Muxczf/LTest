# -*- coding: utf-8 -*-

import Tkinter
from Tkconstants import *
import tkMessageBox

def show_okcancel_msgbox(root, label_text, ok_text, ok_cb, cancel_text, cancel_cb):
	if label_text:
		label = Tkinter.Label(root, textvariable = label_text)
		label.pack()
	
	if ok_text:
		btn_ok = Tkinter.Button(root, textvariable = ok_text, command = ok_cb, width=20)
		btn_ok.pack(side=LEFT)

	if cancel_text:
		btn_cancel = Tkinter.Button(root, textvariable = cancel_text, command = cancel_cb, width=20)
		btn_cancel.pack(side=RIGHT)

def set_main_box_msg(*args):
	global main_label_text, main_ok_text, main_cancel_text
	
	if args[0][0]:
		main_label_text.set(args[0][0])

	if args[0][1]:
		main_ok_text.set(args[0][1])

	if args[0][2]:
		main_cancel_text.set(args[0][2])

def show_question(title_msg = "Ask question", text_msg = "xx"):
	return tkMessageBox.askyesno(title_msg, text_msg)

def show_right(title_msg = "right", text_msg = "xx"):
	return tkMessageBox.showinfo(title_msg, text_msg)

def show_wrong(title_msg = "wrong", text_msg = "xx"):
	return tkMessageBox.showerror(title_msg, text_msg)

def show_taoxin():
	global root, B_SHOW_TAOXIN
	if B_SHOW_TAOXIN:
		# xx
		pass
	
	root.destroy()

if __name__=="__main__":
	
	DICT_QUESTION = [
		"q1",
		"q2",
		"q3",
		"q4",
		"q5",
		"q6",
	]

	DICT_ANSWER = [
		True,
		False,
		True,
		False,
		True,
		False,
	]

	score = 0
	SCORE_ENDGAME = 10
	B_SHOW_TAOXIN = False

	# 居中
	root = Tkinter.Tk()
	w = 400
	h = 80
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))
	root.resizable(False, False)

	main_label_text 	= Tkinter.StringVar()
	main_ok_text 		= Tkinter.StringVar()
	main_cancel_text 	= Tkinter.StringVar()

	def start_game():
		global score, B_SHOW_TAOXIN
		
		n = 0
		while score < SCORE_ENDGAME and n < len(DICT_QUESTION):
			if DICT_ANSWER[n] == show_question(text_msg = DICT_QUESTION[n]):
				score += 2
				show_right("right", "cur_score %d" % score)
			else:
				score -= 2
				show_wrong("wrong", "cur_score %d" % score)
			n += 1
		
		# 结算
		if score >= SCORE_ENDGAME:
			show_right("right", "all good")
			B_SHOW_TAOXIN = True
		else:
			show_wrong("wrong", "try again")

	def end_game():
		global root, B_SHOW_TAOXIN

		show_right("last sup")

		show_taoxin()
		# root.quit()

	set_main_box_msg(["什么鬼", "开始", "结束"])
	show_okcancel_msgbox(root, main_label_text, 
		main_ok_text,
		start_game, 
		main_cancel_text, 
		end_game)

	root.protocol("WM_DELETE_WINDOW", show_taoxin)

	root.mainloop()