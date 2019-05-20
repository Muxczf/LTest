# -*- coding: utf-8 -*-

import Tkinter
from Tkconstants import *
import tkMessageBox
import random
from turtle import *
from time import sleep

def show_okcancel_msgbox(root, label_text, ok_text, ok_cb, cancel_text, cancel_cb):
	if label_text:
		label = Tkinter.Label(root, textvariable = label_text)
		label.pack()
	
	if ok_text:
		btn_ok = Tkinter.Button(root, textvariable = ok_text, command = ok_cb, width=25)
		btn_ok.pack(side=LEFT)

	if cancel_text:
		btn_cancel = Tkinter.Button(root, textvariable = cancel_text, command = cancel_cb, width=25)
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
	global score, B_SHOW_TAOXIN, wrong_score
	
	n = 0
	# last_answer_res = True
	while score < SCORE_ENDGAME and n < len(DICT_QUESTION):
		res = False
		if n == len(DICT_QUESTION) - 1:
			res = show_question(title_msg = "这是一个超超超简单的问题", text_msg = DICT_QUESTION[n])
		else:
			res = show_question(text_msg = DICT_QUESTION[n])

		if DICT_ANSWER[n] == res:
			score += 1
			
			if n == len(DICT_QUESTION) - 1 and score >= SCORE_ENDGAME:
				break

			show_right("", "%s\n可以可以，有那么点意思 (*^．^*)親一個!!!\n你现在已经得到 %d 分啦" % (get_name(), score))
			# last_answer_res = True
		else:
			score -= 1
			if n == len(DICT_QUESTION) - 1:
				show_wrong("", "%s\n好好想想最后一道题该怎么回答哦，哪怕答错一道都没有奖励的哦ƪ(‾ε‾“)ʃƪ(‾ε‾“)ʃ"% get_name())
			else:
				show_wrong("", "%s\n这么简单你都答不对（╯‵□′）╯︵┴─┴\n你现在只有 %d 分了哦" % (get_name(), score))
			
			wrong_score += 1
			# last_answer_res = False
		n += 1
	
	# 结算
	if score >= SCORE_ENDGAME:
		show_info("", "行吧~行吧~ 居然全答对了，我布大才子的颜面尽失，无法在江湖立足了，小看你了╮(－_－)╭")
		B_SHOW_TAOXIN = True

		wrong_text = "%s\n点右上角的叉关了游戏吧，赶紧去学雅思\n你说都已经答完了，还恋恋不舍干嘛╮(－_－)╭" % get_name()
		if wrong_score > 0:
			wrong_text = "%s\n点右上角的叉关了游戏吧，赶紧去学雅思\n你说你答错 %d 次才全蒙对了，还恋恋不舍干嘛╮(－_－)╭" % (get_name(), wrong_score)
		set_main_box_msg([wrong_text, "重新玩一次", "程序员的浪漫是啥？(￣﹁￣)"])
	else:
		show_info("", "t3")
		score = 0

def end_game():
	global root, B_SHOW_TAOXIN

	show_right("", "t2")

def show_info(title_msg = "", text_msg = "show_info"):
	return tkMessageBox.showinfo(title_msg, text_msg)

def show_question(title_msg = "", text_msg = "show_question"):
	return tkMessageBox.askyesno(title_msg, text_msg)

def show_right(title_msg = "", text_msg = "show_right"):
	return tkMessageBox.showinfo(title_msg, text_msg)

def show_wrong(title_msg = "", text_msg = "show_wrong"):
	return tkMessageBox.showerror(title_msg, text_msg)

def get_name():
	return NAME_LIST[random.randint(0, len(NAME_LIST) - 1)]

def inner_show_taoxin():
	def go_to(x, y):
		up()
		goto(x, y)
		down()

	def big_Circle(size):  #函数用于绘制心的大圆
		speed(10)
		for i in range(150):
			forward(size)
			right(0.3)

	def small_Circle(size):  #函数用于绘制心的小圆
		speed(10)
		for i in range(210):
			forward(size)
			right(0.786)

	def line(size):
		speed(1)
		forward(51*size)

	def heart( x, y, size):
		go_to(x, y)
		left(150)
		begin_fill()
		line(size)
		big_Circle(size)
		small_Circle(size)
		left(120)
		small_Circle(size)
		big_Circle(size)
		line(size)
		end_fill()

	def arrow():
		pensize(10)
		setheading(0)
		go_to(-400, 0)
		left(15)
		forward(150)
		go_to(339, 178)
		forward(150)

	def arrowHead():
		pensize(1)
		speed(5)
		color('red', 'red')
		begin_fill()
		left(120)
		forward(20)
		right(150)
		forward(35)
		right(120)
		forward(35)
		right(150)
		forward(20)
		end_fill()

	pensize(2)
	color('red', 'pink')
	# getscreen().tracer(30, 0) # 取消注释后，快速显示图案
	heart(200, 0, 1)
	setheading(0)
	heart(-80, -100, 1.5)
	arrow()
	arrowHead()
	go_to(400, -300)
	done()

def show_taoxin():
	global root, B_SHOW_TAOXIN
	if B_SHOW_TAOXIN:
		show_right("", "那你该不会真的以为我啥奖励都不给你吧（＾ω＾）")
		show_right("", "猜猜是啥（＾ω＾）")
		show_right("", "猜不到？（＾ω＾）")
		show_right("", "还是猜不到？（＾ω＾）")

		inner_show_taoxin()

		show_right("", "t4")
		show_right("", "t5")

if __name__=="__main__":
	
	NAME_LIST = [
		"body1",
		"body2",
		"body3",
		"body4",
		"body5",
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
		True,
		True,
	]

	score = 0
	wrong_score = 0
	SCORE_ENDGAME = 5
	B_SHOW_TAOXIN = False

	# 居中
	root = Tkinter.Tk()
	w = 400
	h = 120
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