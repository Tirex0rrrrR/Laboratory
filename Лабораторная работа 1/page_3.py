# TODO Найдите количество книг, которое можно разместить на дискете
byte_disk=1.44*1024*1024
byte_simbool=4
byte_line=4*25
byte_page=byte_line*50
byte_book=byte_page*100
page_calc=byte_disk//byte_book
print("Количество книг, помещающихся на дискету:", round(page_calc))
