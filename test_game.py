
import tkinter as tk
import tkinter.font as tf

user_id = "zyj654321"
pass_word = "zyj654321"
user_id_1 = ''
user_pass_1 = ''
count = 0

name_id = "张羽吉"
life_1 = 100
attack_1 = 9999999
defelt_1 = 10

name_monster_id = "火巨人"
life_monster_1 = 50
attack_monster_1 = 12
defelt_monster_1 = 8

window = tk.Tk()
window.title("test1")
window.geometry("500x300")
hit_it_buff = False

e = tk.Entry(window,width=15)
e.pack()
e2 = tk.Entry(window,width=15,show="*")
e2.pack()

t = tk.Text(window,height=2)
t.pack()

t2 = tk.Text(window,height=2)
t2.pack()
t3 = tk.Text(window,height=2)
t3.pack()

t01 = tk.Text(window,height=5)
t01.pack()
t02 = tk.Text(window,height=3)
t02.pack()
def insert_point():
    global user_id_1
    var = e.get()
    user_id_1 = var
    t.delete(1.0,'end')
    t.insert("insert",var)
def insert_point_2():
    insert_point()
    global user_pass_1
    var = e2.get()
    user_pass_1 = var
    t2.delete(1.0,'end')
    t2.insert("insert",var)
    end_point()

def insert_point_3():
    global life_1,life_monster_1,attack_01,attack_monster_01,attack_1
    attack_01 = attack_monster_1 - defelt_1
    life_1 = life_1 - attack_01
    if life_1 < 0:
        life_1 = 0

    attack_monster_01 = attack_1 - defelt_monster_1
    life_monster_1 = life_monster_1 - attack_monster_01
    if life_monster_1 < 0:
        life_monster_1 = 0
        attack_1 += 999
    event(attack_01,attack_monster_01,life_monster_1)
    game_start()

def event(attack_01,attack_monster_01,life_monster_1):
    global count
    count += 1
    t02.delete(1.0, 'end')
    name = str(name_id)
    name_monster =str(name_monster_id)
    ft = tf.Font(family="微软雅黑",size = 10)
    if life_monster_1 == 0:
        t02.insert("insert", name_monster + '已死亡')
        t02.insert("insert", name_monster + '掉落了')
        t02.tag_add('tag','end')
        t02.tag_config("tag",foreground = "red",font= ft)

        t02.insert('insert','炎龙巨剑','tag')
        t02.insert(tk.INSERT, '\n')
        t02.insert("insert", name + '攻击力+')
        t02.insert("insert",'999','tag')
    else:
        t02.insert("insert",name_monster + '第'+ str(count) + '次攻击了' + name + '对它造成了'+ str(attack_monster_01) +'点伤害')
        t02.insert(tk.INSERT, '\n')
        t02.insert("insert",name + '第'+ str(count) +'次攻击了' + name_monster + '对它造成了'+ str(attack_01) +'点伤害')

def end_point():
    if user_pass_1 == pass_word and user_id_1 == user_id:
        t3.delete(1.0,'end')
        t3.insert("insert",'登陆成功')
        game_start()
    else:
        t3.delete(1.0,'end')
        t3.insert("insert", '密码错误')

def game_start():
    try:
        t01.delete(1.0,'end')
    except:
        pass
    global attack_1
    name = "昵称：" + str(name_id) + "       怪物：" + str(name_monster_id)
    life = '生命：' + str(life_1) + "          生命：" + str(life_monster_1)
    attack = '攻击：' + str(attack_1) + "          攻击：" + str(attack_monster_1)
    defelt = '防御：' + str(defelt_1) + "          防御：" + str(defelt_monster_1)
    t01.insert("insert",name)
    t01.insert(tk.INSERT, '\n')
    t01.insert("insert",life)
    t01.insert(tk.INSERT, '\n')
    t01.insert("insert",attack)
    t01.insert(tk.INSERT, '\n')
    t01.insert("insert",defelt)

# user = tk.Button(window,text="确认账号",command=insert_point)
# user.pack()
password = tk.Button(window,text="登陆",command=insert_point_2)
password.pack()

attack_monster = tk.Button(window,text="打怪",command=insert_point_3)
attack_monster.pack()

print("111")
window.mainloop()
