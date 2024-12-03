data_panen = {
    'lokasi1':{
        'nama_lokasi':'Kebun A',
        'hasil_panen': {
            'padi':1200,
            'jagung':800,
            'kedelai':500
        } 
    },
    'lokasi2':{
        'nama_lokasi':'Kebun B',
        'hasil_panen': {
            'padi':1500,
            'jagung':900,
            'kedelai':450
        } 
    },
    'lokasi3':{
        'nama_lokasi':'Kebun C',
        'hasil_panen': {
            'padi':1100,
            'jagung':750,
            'kedelai':600
        }
    },
    'lokasi4':{
        'nama_lokasi':'Kebun D',
        'hasil_panen': {
            'padi':1300,
            'jagung':850,
            'kedelai':550
        }
    },
    'lokasi5':{
        'nama_lokasi':'Kebun E',
        'hasil_panen': {
            'padi':1400,
            'jagung':950,
            'kedelai':480
        }
    }
}
print("Jawaban No 1")
for l,s in data_panen.items():
    print(f"Lokasi : {l}")
    print(f"Nama Lokasi : {s['nama_lokasi']}")
    print(f"Hasil Panen : {s['hasil_panen']}")

print("\nJawaban No 2")
pn_jagung = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Hasil Panen jagung pada Lokasi Ke-2 adalah {pn_jagung}")

print("\nJawaban No 3")
lok3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama Lokasi ke-3 adalah {lok3}")

print("\nJawaban No 4 dan 5")
padi = []
kedelai = []
for d,o in data_panen.items():
    hsp_padi= o['hasil_panen']['padi']
    padi.append(hsp_padi)
    hsp_kedelai= o['hasil_panen']['kedelai']
    kedelai.append(hsp_kedelai)

print("Hasil Panen Padi :")
for d in range(len(padi)) :
    print(f"Lokasi ke-{d+1} : padi = {padi[d]}")
print("Hasil Panen Kedelai :")
for e in range(len(padi)) :
    print(f"Lokasi ke-{e+1} : kedelai = {kedelai[e]}")

print("\nJawaban No 6")
for k,p in data_panen.items():
    hs_padi = p['hasil_panen']['padi']
    hs_jagung = p['hasil_panen']['jagung']
    if hs_padi > 1300 or hs_jagung > 800 :
        print(f"{p['nama_lokasi']} memerlukan perhatian khusus")
    else : 
        print(f"{p['nama_lokasi']} dalam kondisi yang sangat baik dan aman")

print("Tugas Git tentang Dictionary")