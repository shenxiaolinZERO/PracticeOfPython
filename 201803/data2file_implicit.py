import pandas as pd
import print_to_file as p2f


def main():
    # group_num =1
    train_file_flag = 1
    test_file_flag =1
    data_dir = '..\\data'
    # if train_file_flag == 1:
        # train_file(data_dir)
    if test_file_flag == 1:
        test_file(data_dir)


def test_file(data_dir):
    test = pd.read_csv(data_dir+'\\dataset1\\test_part_000.csv')
    test_item_list = []
    test_session_item_list = []
    user_session_dic = {}

    #先获取所有的item列表
    for i in range(test.shape[0]): # df.shape[0]，df.shape[1]分别获取行数、列数
        # 所有item减去 在该session中点击+购买，即所有item-该session中的显式（explicit）item作为隐式（implicit）item
        item_row = test.ix[i, -2].strip('{').strip('}').replace(' ', '').split(',')
        for j in item_row:
            item_id = int(j)
            test_item_list.append(item_id)
    test_item_list = list(set(test_item_list))

    #获取 test_session_item_list = [] 和 user_session_dic = {}
    for i in range(test.shape[0]): # df.shape[0]，df.shape[1]分别获取行数、列数
        cur_user = test.ix[i, 'user_id']
        if cur_user in user_session_dic:
            user_session_dic[cur_user].append(test.ix[i, 'session_id'])
        else:
            user_session_dic[cur_user] = [test.ix[i, 'session_id']]
        test_session_item_list.append([test.ix[i, 'session_id'], [], []])

        #该session中点击+购买（即csv文件倒数第2列）作为显式（explicit）item
        item_explicit = test.ix[i, -2].strip('{').strip('}').replace(' ', '').split(',')
        for j in item_explicit:
            item_id = int(j)
            test_session_item_list[i][1].append(item_id)

        # 所有item减去 在该session中点击+购买，即所有item-该session中的显式（explicit）item作为隐式（implicit）item
        test_session_item_list[i][2] = list(set(test_item_list) - set(test_session_item_list[i][1]))


    p2f.print_data_lists_to_file(test_session_item_list, data_dir+'\\dataset1\\test_implicit\\session_item.txt')
    p2f.print_list_to_file(test_item_list, data_dir+'\\dataset1\\test_implicit\\items.txt')
    p2f.print_list_dict_to_file(user_session_dic, data_dir+'\\dataset1\\test_implicit\\user_session.txt')
    print('test file already')


def train_file(data_dir, group_num):
    # 读取分好的数据,生成模型所用的session_item.txt,items.txt,user_session.txt
    for group in range(group_num):
        train = pd.read_csv(data_dir+'\\dataset'+str(group+1)+'\\train.csv')
        train_item_list = []
        train_session_item_list = []
        train_item_session_dic = {}
        user_session_dic = {}
        for i in range(train.shape[0]):
            cur_user = train.ix[i, 'user_id']
            cur_session = train.ix[i, 'session_id']
            if cur_user in user_session_dic:
                user_session_dic[cur_user].append(cur_session)
            else:
                user_session_dic[cur_user] = [cur_session]
            train_session_item_list.append([cur_session, [], []])

            item_bought = train.ix[i, -3].strip('{').strip('}').replace(' ', '').split(',')
            for j in item_bought:
                item_id = int(j)
                train_session_item_list[i][1].append(item_id)
                if item_id in train_item_session_dic:
                    train_item_session_dic[item_id][0].append(cur_session)
                else:
                    train_item_session_dic[item_id] = [[cur_session], []]

            item_clicked = train.ix[i, -2].strip('{').strip('}').replace(' ', '').split(',')
            item_clicked_not_bought = list(set(item_clicked) - (set(item_bought)))

            for j in item_clicked_not_bought:
                item_id = int(j)
                train_item_list.append(item_id)
                train_session_item_list[i][2].append(item_id)
                if item_id in train_item_session_dic:
                    train_item_session_dic[item_id][1].append(cur_session)
                else:
                    train_item_session_dic[item_id] = [[], [cur_session]]
        train_item_list = list(set(train_item_list))
        p2f.print_data_lists_to_file(train_session_item_list, data_dir+'\\dataset'+str(group+1)+'\\train\\session_item.txt')
        p2f.print_list_to_file(train_item_list, data_dir+'\\dataset'+str(group+1)+'\\train\\items.txt')
        p2f.print_list_dict_to_file(user_session_dic, data_dir+'\\dataset'+str(group+1)+'\\train\\user_session.txt')
        p2f.print_2lists_dict_to_file(train_item_session_dic, data_dir+'\\dataset'+str(group+1)+'\\train\\item_session.txt')
        print('train group', group+1, '\tdone')
    print('train file already')


if __name__ == '__main__':
    main()
