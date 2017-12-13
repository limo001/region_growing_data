 






   shuffle(FileList) # Usefull for further segmenting the validation set
    for filename in FileList:
        file_name = filename.split('/')[3]  
        print file_name
        imagename = file_name[:6] 
        fo = open("/home/li_mo/3rd-party/caffe/class_labels.txt", "r") 
        for line in fo.readlines():
            data = line.split()
            foname = data[0]
            label_number = data[1]
            if foname == imagename :
                label = int(label_number) 
                data_label.append(label)
       
        fo.close()        
       # label = int(filename.split('/')[2])
       # data_label.append(label)  
       # fo.close()
        Im = Image.open(filename)
        pixel = Im.load()
        width, height = Im.size
        for x in range(0,width):
            for y in range(0,height):
                data_image.append(pixel[y,x][0])
               # print pixel[y,x]
       # print data_image
                
	  #data_label.append(label) # labels start (one unsigned byte each)
    print data_label
    print data_image
    hexval = "{0:#0{1}x}".format(len(FileList),6) # number of files in HEX
	# header for label array
    header = array('B')
    header.extend([0,0,8,1,0,0])
    header.append(int('0x'+hexval[2:][:2],16))
    header.append(int('0x'+hexval[2:][2:],16))	
    data_label = header + data_label
    # additional header for images array	
    if max([width,height]) <= 256:
        header.extend([0,0,0,width,0,0,0,height])
    else:
        raise ValueError('Image exceeds maximum size: 256x256 pixels');

    header[3] = 3 # Changing MSB for image data (0x00000803)
    data_image = header + data_image
    
    output_file = open(name[1]+'-images-idx3-ubyte', 'wb')
    data_image.tofile(output_file)
    output_file.close()
    output_file = open(name[1]+'-labels-idx1-ubyte', 'wb')
    data_label.tofile(output_file)
    output_file.close()

# gzip resulting files

for name in Names:
	os.system('gzip '+name[1]+'-images-idx3-ubyte')
	os.system('gzip '+name[1]+'-labels-idx1-ubyte')

 
