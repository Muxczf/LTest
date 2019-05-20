# -*- coding: utf-8 -*-

import Tkinter
from Tkconstants import *
import tkMessageBox
import random

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

def start_game():
	global score, B_SHOW_TAOXIN
	
	n = 0
	last_answer_res = True
	while score < SCORE_ENDGAME and n < len(DICT_QUESTION):
		if DICT_ANSWER[n] == show_question(text_msg = DICT_QUESTION[n]):
			score += 2
			show_right("", "%s\n可以可以，有那么点意思 (*^．^*) 親一個!!!\n你现在已经有 %d 分啦" % (get_name(), score))
			last_answer_res = True
		else:
			score -= 2
			show_wrong("", "%s\n这么简单你都答不对（╯‵□′）╯︵┴─┴\n你现在只有 %d 分了哦" % (get_name(), score))
			last_answer_res = False
		n += 1
	
	# 结算
	if score >= SCORE_ENDGAME:
		show_info("", "行吧~行吧~ 居然全答对了，我颜面荡然无存，小看你了╮(－_－)╭")
		B_SHOW_TAOXIN = True
	else:
		show_info("", "t4")
		score = 0

def end_game():
	global root, B_SHOW_TAOXIN

	show_right("", "t2")

	show_taoxin()

def show_info(title_msg = "", text_msg = "show_info"):
	return tkMessageBox.showinfo(title_msg, text_msg)

def show_question(title_msg = "这是一个很简单的问题", text_msg = "show_question"):
	return tkMessageBox.askyesno(title_msg, text_msg)

def show_right(title_msg = "", text_msg = "show_right"):
	return tkMessageBox.showinfo(title_msg, text_msg)

def show_wrong(title_msg = "", text_msg = "show_wrong"):
	return tkMessageBox.showerror(title_msg, text_msg)

def get_name():
	return NAME_LIST[random.randint(0, len(NAME_LIST) - 1)]

def show_taoxin():
	global root, B_SHOW_TAOXIN
	if B_SHOW_TAOXIN:
		show_right("", "你该不会以为我啥奖励都不给你吧（＾ω＾）")
		show_right("", "猜猜是啥（＾ω＾）")
		show_right("", "猜不到？（＾ω＾）")


		show_right("", "t4")

if __name__=="__main__":
	
	NAME_LIST = [
		"body1",
		"body2",
		"body3",
	]

	DICT_QUESTION = [
		"q1",
		"q2",
		"q3",
		"q4",
		"q5",
	]

	DICT_ANSWER = [
		True,
		False,
		True,
		False,
		True,
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

	set_main_box_msg(["%s\nt1" % get_name(), "假装知道(つ´ω`)つ", "啥玩意，不xiu得(￣﹁￣)"])
	show_okcancel_msgbox(root, main_label_text, 
		main_ok_text,
		start_game, 
		main_cancel_text, 
		end_game)

	def quit_all():
		show_taoxin()
		root.destroy()
	root.protocol("WM_DELETE_WINDOW", quit_all)

	root.mainloop()