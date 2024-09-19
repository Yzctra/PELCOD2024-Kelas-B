hargaparfumcitra = 35.000
hargaparfumnurul = 45.000


 # input nama pengguna
nama1 = input("haii, ini dengan siapa?")
print("haloo" , nama1 , "salam kenal")

print("mari kita baca obrolan citra dan nurul")

input("masukan angka 1 untuk next chapter")
 # percakapan dimulai
print("nurul: halloo citra, kamu tadi sedang apa di toko amanda?")
print("citra: haii nurul, aku tadi sedang membeli parfum disana")
print("nurul: oh ya?? aku juga baru aja beli parfum disana, btw berapa harga parfum yang kamu beli?")
print("citra: emm aku tadi beli parfum dengan harga" , hargaparfumcitra , "memangnya berapa harga parfum yang kamu beli nurul?")
print("nurul: ooo, harga parfum yang kubeli tadi" , hargaparfumnurul , "cit")

 # operaasi aritmatika
selisihharga = hargaparfumcitra - hargaparfumnurul
print("citra: eh kenapa harga parfum yang kita beli beda ya? padahal kita beli di toko yang sama kan, berarti beda harga parfum kita" , selisihharga , "ngga sih?")

 # input dari pengguna 
tebakharga = int(input("coba tebak berapa selisih dari harga parfum citra dan nurul: "))

 # operasi aritmatika dan logika 
selisihharga = hargaparfumcitra - hargaparfumnurul 

 # output hasil tebakan 
if tebakharga == 10.000 : 
    print("citra: yap bener bangett")
else : 
    print("nurul: emm kayaknya jawaban kamu kurang tepat deh, selisih harga parfum kami sebenernya" , selisihharga , "loh.")

input("tekan angka 3 untuk melanjutkan dialog")

 # # pertanyaan tambahan dengan operasi logika
print("citra: eh nurul, aku mau tanya lagi deh sama kamu")
citra_number = 35 
nurul_number = 12 

print("citra: kalo aku punya permen susu" , {citra_number} , "terus kamu punya permen kopi" , {nurul_number} , "jadi berap permen yang kita punya kalo semisal kita campur?")

user_answer = int(input("coba bantu nurul untuk menjawabnya yuk: "))

hasil = citra_number + nurul_number 

if user_answer == hasil : 
        print("nurul: terimakasih sudah membantu menjawab, jawaban kamu benar sekali...")
else : 
        print("nurul: emm, jawaban kamu sepertinya kurang tepat lagi dehh. karna jawaban yang benar itu" , hasil , "permen")

    
 # akhir percakapan 
print("citra: terimakasih ya nurul udah mau ngajak aku ngobrol...")
print("nurul: iya citraa, makasih juga yaa sudah mau ngobrol sama aku. dan terimakasih juga ya" , nama1 , "karna sudah ikut berpartisipasi")
