def eraseGreen(path):
	image=cv2.imread(path,-1)
	cut=0
	i,j = image.shape[0],image.shape[1]
	scale_percent = 50
	width = int(j * scale_percent / 100)
	height = int(i * scale_percent / 100)
	actW = width
	actH = height
	dsize = (width, height)
	img=cv2.resize(image,dsize)
	imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	sensitivity=20
	lower_green  = np.array([60 - sensitivity, 100, 100])
	upper_green  = np.array([60 + sensitivity, 255, 255])
	mask1 = cv2.inRange(imgHsv, lower_green, upper_green)
	maskx = cv2.morphologyEx(mask1, cv2.MORPH_ERODE, np.ones((2,2),np.uint8))
	mask2 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((4,4),np.uint8))
	mask3 = mask1+mask2+maskx

	def myfunc(img,mask):
		green = np.zeros_like(img, np.uint8)
		for i,dim1 in enumerate(mask):
			for j,dim2 in enumerate(dim1):
				if mask[i][j]>0:
					green[i][j]=np.array([255,255,255])
				else:
					green[i][j]=img[i][j]
		return green
	noG=myfunc(img,mask3)

	return noG