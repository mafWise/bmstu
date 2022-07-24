from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from numpy import array, uint8
#from numpy import *


def open_pic(img):
	file_path = askopenfilename(title = 'Выебрите файл', defaultextension='.bmp', filetypes=[(".bmp", ".bmp")])
	if not(file_path):
		return img

	img = Image.open(file_path).convert('RGB')
	width, heigh = img.size

	to_display = ImageTk.PhotoImage(img.resize((250, 250)))
	pic['image'] = to_display
	pic.image = to_display

	return img, ''


def bitmap(img):
	width, heigh = img.size
	#pixels = array([[(lambda w, h: list(img.getpixel(tuple([w, h]))))(w, h) 
	#	for w in range(width)] for h in range(heigh)], dtype = uint8)

	pixels = []
	for h in range(heigh):
		pixels.append([])
		for w in range(width):
			pixels[-1].append(list(img.getpixel(tuple([w, h]))))
	pixels = array(pixels, dtype = uint8)

	return pixels

def encrypt(img):
	#text_mask = 0b10000000
	img_mask = 0b11111110
	last_bit = 0b10000000

	if (img == None):
		print('open before')
		#messagebox.showerror("Error", "open .bmp picture before doing smth.")
		return img, "open .bmp picture before doing smth."

	width, heigh = img.size
	pixels = bitmap(img)
	s = text.get()
	if s == '':
		print('Nothing to encrypt.')
		#messagebox.showerror("Error", "Nothing to encrypt.")
		return img, "Nothing to encrypt."
	elif len(s) > heigh * width // 3 - 1:
		print('Too many symbols.')
		#messagebox.showerror("Error", "Too many symbols to encrypt.")
		return img, "Too many symbols to encrypt."
	else:
		try:
			s = list(text.get().encode('ascii')) + [0]
		except:
			#messagebox.showerror("Error", "Not ascii symbols.")
			return img, "Not ascii symbols."

	shape = pixels.shape
	pixels = pixels.ravel()

	i = 0
	while s != []:
			if ((i + 1) % 9 != 0 or i == 0):
				pixels[i] = pixels[i] & img_mask | int((s[0] & last_bit) != 0)
				last_bit >>= 1
			else:
				last_bit = 0b10000000
				s.pop(0)
			i += 1

	#if type(s) != str:
	#	while s != []:
	#		if ((i + 1) % 9 != 0 or i == 0):
	#			pixels[i] = pixels[i] & img_mask | int((s[0] & last_bit) != 0)
	#			last_bit >>= 1
	#		else:
	#			last_bit = 0b10000000
	#			s.pop(0)
	#		i += 1
	pixels.resize(shape)

	encrypted_img = Image.fromarray(pixels)
	#messagebox.showinfo('result', 'successfully encrypted.')
	return encrypted_img, 'successfully encrypted.'


def decrypt(img):
	if (img == None):
		print('open before')
		#messagebox.showerror("Error", "open .bmp picture before doing smth.")
		return img, "open .bmp picture before doing smth."

	last_bit = 0b00000001
	i = 0
	s = 0
	pixels = bitmap(img)

	shape = pixels.shape
	pixels = pixels.ravel()

	i = 0
	enc_text = ''
	symb = ''

	while(i < len(pixels) and symb != '\x00'):
		if ((i + 1) % 9 != 0 or i == 0):
			s += (pixels[i] % 2) << (8 - (i + 1) % 9)
			#print(pixels[i] % 2)
		else:
			enc_text += symb
			symb = chr(s)
			#print('symb: ', s, chr(s))
			s = 0
		i += 1

	pixels.resize(shape)

	print('text: ', enc_text)
	text.delete(0, END)
	text.insert(0, enc_text)
	return img, enc_text


def save_img(img):
	if (img == None):
		print('open before')
		#messagebox.showerror("Error", "open .bmp picture before doing smth.")
		return img, "open .bmp picture before doing smth."

	save_path = asksaveasfilename(title = 'Save file', defaultextension='.bmp', filetypes=[(".bmp", ".bmp")])
	if save_path:
		img.save(save_path)


def message(text):
	if text != '':
		messagebox.showinfo('message', text)

window = Tk()
window.title('lab3')

class image:
#	img = None
	pass

img = image()
img.img = None
img.img_m = None, ''

#Button(window, text="choose picture", command = lambda: setattr(img, 'img', open_pic(img.img))).pack()
Button(window, text="choose picture", command = lambda: setattr(img, 'img_m', open_pic(img.img_m[0]))).pack()


pic = Label(window)
pic.pack()

text = Entry(window, width = 50)
text.pack()

#Button(window, text="encrypt", command = lambda: setattr(img, 'img', encrypt(img.img))).pack(side=LEFT)
Button(window, text="encrypt", command = lambda: [setattr(img, 'img_m', encrypt(img.img_m[0])), message(img.img_m[1])]).pack(side=LEFT)

#Button(window, text="decrypt", command = lambda: decrypt(img.img)).pack(side=RIGHT)
Button(window, text="decrypt", command = lambda: [setattr(img, 'img_m', decrypt(img.img_m[0])), message(img.img_m[1])]).pack(side=RIGHT)

#Button(window, text="save picture", command = lambda: save_img(img.img)).pack(side=TOP)
Button(window, text="save picture", command = lambda: [save_img(img.img_m[0]), message(img.img_m[1]) ]).pack(side=TOP)

window.mainloop()

