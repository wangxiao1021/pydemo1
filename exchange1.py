# 人民币的输入
rmb_val = input('请输入人民币金额: ')
TOUSD = 6.7
rmb = eval(rmb_val)
usd = rmb / TOUSD
print("美元金额：", usd)
