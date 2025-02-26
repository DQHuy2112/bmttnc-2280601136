def tongchan(lst):
    tong =0
    for num in lst:
        if num %2 ==0:
            tong+=num
    return tong

input_list = input("Nhập dnah sách các số , cách nhau bằng dấu phẩy:")
numbers = list(map(int , input_list.split(',')))

tong_chan = tongchan(numbers)
print("Tổng các số chẵn trong List là: ",tong_chan)