penggunaan_elektrik=0
unit_penggunaan_elektrik=0
bil_elektrik=0
penggunaan_elektrik=int(input("Masukkan penggunaan elektrik:"))
if penggunaan_elektrik>=1:
    kadar_tarif=0.218
    unit_penggunaan_elektrik=200
elif penggunaan_elektrik>=201:
    kadar_tarif=0.334
    unit_penggunaan_elektrik=100
elif penggunaan_elektrik>=301:
    kadar_tarif=0.516
    unit_penggunaan_elektrik=300
else:
    kadar_tarif=0.546
    unit_penggunaan_elektrik=300
bil_elektrik=unit_penggunaan_elektrik*kadar_tarif
print("Bil elektrik ialah RM",bil_elektrik)
