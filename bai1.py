total = int(input("Tổng số tiền ban đầu của hóa đơn "))

if total > 500000 :
    sale_off = total * 0.1
    total -= sale_off
    print(f"Số tiền được giảm giá: {sale_off}VND")
else:
    print("Không được giảm giá")

print(f"Tổng số tiền khách phải trả là: {total}VND")