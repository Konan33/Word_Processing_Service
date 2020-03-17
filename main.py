#Intro
print('*'*56)
print('* CHÀO MỪNG QUÝ KHÁCH ĐÃ ĐẾN VỚI DỊCH VỤ XỬ LÝ VĂN BẢN *')
print('*'*56)
OldString = input('Quý khách vui lòng cho chúng tôi xem văn bản cần xử lý: ')

#Lại là Intro
while True:
  print('-'*40)  
  print('Chúng tôi có những dịch vụ sau đây\n1. Trộm long tráo phụng\n2. Triệu hồi Thánh Gióng\n3. Cải trang vi hành\n4. Hiệu triệu tướng lĩnh\n5. Trợ giúp từ xa\n6. Triệu hồi qua gương\n7. Cách ly tối đa\n8. Vào nhầm dịch vụ')
  print('-'*40)
  x = int(input('Quý khách vui lòng chọn số: '))
  #Kiểm tra lựa chọn
  if (x == 1):
    a = input('Vui lòng nhập từ cần thay thế: ')
    b = input('Vui lòng nhập từ thay thế: ')
    NewString = OldString.replace(a,b)
    print('Sau khi trộm long tráo phụng: ',NewString)
  elif (x == 2):
    print('Sau khi triệu hồi Thánh Gióng: ',OldString.upper())
  elif (x == 3):
    print('Sau khi cải trang vi hành: ',OldString.lower())
  elif (x == 4):
    print('Sau khi hiệu triệu tướng lĩnh: ',OldString.capitalize())
  elif (x == 5):
    a = input('Vui lòng nhập ký tự cần thêm: ')
    b = input('Vui lòng nhập vị trí ký tự cần thêm: ')
    print('Sau khi được trợ giúp từ xa: ',a.join(b))
  elif (x == 6):
    print('Văn bản sau khi triệu hồi qua gương: ',''.join(reversed(OldString)))
  elif (x == 7):
    print('Văn bản sau khi cách ly: ',OldString.split(' '))
  else:
    print('Cảm ơn quý khách đã lướt qua!')
    break