import cv2, math, random, numpy as np

def msg(index = 0):
  if index == 0:
    return input("Message: ")
  elif index == 1:
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
  elif index == 2:
    return "Lorem ipsum"
  else:
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget nisi pulvinar, commodo ex a, fermentum diam. Aliquam in feugiat ligula. Suspendisse tempor, orci in aliquam rhoncus, nisi ipsum elementum est, lobortis fermentum ex tortor vitae est. Cras at elit urna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nunc egestas ipsum libero, sed hendrerit eros tincidunt id. Nunc venenatis magna ac mauris facilisis sodales. Ut mauris ex, condimentum nec mi vel, ullamcorper fringilla quam. Etiam nibh nibh, consectetur eget nulla sit amet, rutrum blandit risus. Pellentesque vitae semper arcu. Donec diam nulla, laoreet ac lobortis et, posuere in dolor. Phasellus vitae ante ac nulla facilisis euismod sit amet feugiat orci. Mauris id sem a nulla interdum molestie. Mauris quis nisl felis. Phasellus tempor feugiat laoreet. Nullam tempor augue nulla, in luctus mauris efficitur id. Sed nulla ex, ultrices et sodales pretium, condimentum sit amet lectus. Fusce scelerisque nisl vulputate arcu commodo elementum. Integer tincidunt, odio at sollicitudin vestibulum, tellus turpis consequat augue, a semper neque ante at sem. Aliquam tempor feugiat augue id iaculis. Nam porta erat id libero pulvinar sagittis. Nulla faucibus lectus eu quam tincidunt suscipit. Proin vitae efficitur mi. Aliquam lacinia, nisl eu convallis facilisis, tortor orci lacinia lacus, eu sodales urna ex at lectus. Suspendisse felis urna, placerat non leo ultricies, vehicula hendrerit neque. Aliquam rutrum mollis quam, vel suscipit nunc semper ac. Nulla in malesuada libero. In ut nunc pretium, luctus risus convallis, scelerisque lacus. Curabitur urna tellus, dictum nec tellus sed, mollis blandit libero. Duis cursus mauris sed dolor aliquet, eget gravida ipsum bibendum. Morbi eget dapibus augue, vitae consectetur velit. Pellentesque ullamcorper fringilla sem nec congue. Mauris feugiat ullamcorper elit a pulvinar. Mauris vehicula pulvinar ex sit amet rhoncus. Quisque eget commodo magna, a gravida ex. Nam purus velit, pharetra ut leo ut, porta dictum mauris. Curabitur elementum ligula et accumsan laoreet. Etiam venenatis non magna et fermentum. Sed odio felis, ultrices sit amet felis vitae, fringilla molestie leo. Ut nec risus sit amet tortor vulputate placerat. Cras feugiat sem justo, nec venenatis nibh aliquet id. Maecenas ut feugiat mauris, eu gravida lorem. In vitae augue massa. In hac habitasse platea dictumst. Suspendisse porttitor, lorem quis vulputate mattis, augue dolor tempus turpis, eget varius felis nisi varius ante. Cras vel tincidunt leo. Etiam mollis, ipsum et imperdiet dapibus, lacus lectus maximus elit, nec rutrum felis nisi rhoncus sapien. Nulla sit amet lacinia velit. Fusce ut tempor nisi. In finibus congue semper. Cras nec nibh dolor. Ut commodo dolor tortor. Sed nec ullamcorper orci. Cras velit erat, tincidunt sed viverra ac, cursus a odio. In eget orci quam. Pellentesque molestie viverra nunc, in dignissim orci tempor ut. "

def msgToBinMatrix(msg,imgSize = None, distance = None):

  msgAsciiArray = [ord(i) for i in msg]
  msgBinArray = [bin(i)[2:].rjust(8,"0") for i in msgAsciiArray]
  msgBinStr = ''.join(msgBinArray)

  print("[Info] The size of the message is", len(msgBinStr))

  if imgSize != None and distance == None:
    distance = math.floor((imgSize[0]*imgSize[1])/len(msgBinStr))

  msgBinStr = msgBinStr.replace("0","0".rjust(distance,"0")).replace("1","1".rjust(distance,"0"))
  msgBinStrLength = len(msgBinStr)


  if imgSize == None:
    sqrtSize = math.sqrt(msgBinStrLength)
    imgWidth = math.ceil(sqrtSize)
    imgSize = (imgWidth,imgWidth)

  imgSizeBits = imgSize[0]*imgSize[1]

  print("[Info] The size of the message is", msgBinStrLength)
  print("[Info] The image has a size of", imgSizeBits)

  if msgBinStrLength > imgSizeBits:
    return None, "[Error] The size of the image can't contain the message, increase the image dimensions"

  msgBinStr = msgBinStr.ljust(imgSizeBits,'0')

  imgArr = np.array(["0" if i == "0" else "255" for i in msgBinStr]).reshape(imgSize[0],imgSize[1])

  return imgArr, None

def visualizeImage(imgArr,imgSize = None):
  if imgSize == None:
    imgWidth = len(imgArr)
    imgSize = (imgWidth,imgWidth)

  img = np.zeros([imgSize[0],imgSize[1]])
  img[:,:] = imgArr
  # img[:,:,1] = imgArr # np.zeros(imgSize, dtype=int)
  # img[:,:,2] = imgArr # np.ones(imgSize, dtype=int)

  # resizedImg = cv2.resize(img,(800,800))
  cv2.imwrite('imageFromMessage.png', img)
  
  cv2.imshow("bho1", img)
  # cv2.imshow("bho2", resizedImg)

  cv2.waitKey(0)

message = msg(4)*34
imgSize = (720,1280)
# imgSize = (20,20)
imgArr, err = msgToBinMatrix(message,imgSize=imgSize)

if err != None: print(err)
else: visualizeImage(imgArr,imgSize=imgSize)
