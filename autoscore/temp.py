NAME_LIST = ['金筱易', '徐嘉孺', '冯国申', '杨书勤', '王建为', '宋祎垌', '王天骏', '曹佳硕', '王希蒙', '穆玥彤', '栾博业', '王禹璇', '金云鹏', '张靖悦', '赵益铭', '解丰硕', '滕金楠', '赵一博', '尧洁', '董钰鑫', '张馨童', '李思佳', '许新敏', '刘佳欣', '陈冬妮', '英瑞桐', '康汝佳怡', '张田佳含', '郑荟竹', '王奥涵', '石成功', '于世畔', '刘一田', '赵津磊', '白长健', '高艺鸣', '付晓玮', '李宇梁', '沈春潇', '李昶杰', '程铄茜', '沈凯文', '杨箫宁', '杨思齐', '刘宇凡', '薛宇轩', '周艺卓',]

dic = dict.fromkeys(NAME_LIST,False)
data = {k for k,v in dic.items() if v == False}

print(data)