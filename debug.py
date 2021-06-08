# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/6/6 6:55
software: PyCharm

Description:
    this is the main program of this card game, now this a a word version.

Attention：
    pandas读取中文的时候需要添加encoding="gb2312"，否则报错
"""
import sys
import time
import pandas as pd
import random
import numpy as np

_LONG_TIME_SLEEP = 2.5
_MEDIUM_TIME_SLEEP = 1.5
_SHORT_TIME_SLEEP = 1
_VERSION = "v1.02"


class ThreeKingdomGame:
    def __init__(self):
        self.heroes_list = pd.read_csv("./settingsDebug/heroesParameters.csv", encoding="gb2312")
        self.customer_hero = pd.read_csv("./settingsDebug/customerParameters_hero.csv", encoding="gb2312")
        self.customer_object = pd.read_csv("./settingsDebug/customerParameters_object.csv", encoding="gb2312")
        self.customer_flag = pd.read_csv("./settingsDebug/customerParameters_flag.csv", encoding="gb2312")
        self.enemy = None
        self.battle_field = pd.read_csv("./settingsDebug/battleFieldParameters.csv", encoding="gb2312")

    def MainGame(self):
        if self.customer_flag["游戏运行次数"][0] == 0:
            print("\033[1;34m唔，头好痛，这里是哪里？我记得我躺在自己家里啊...\033[0m")
            time.sleep(_MEDIUM_TIME_SLEEP)
            print("\033[1;34m(休息了大约半个时辰)\033[0m")
            time.sleep(_LONG_TIME_SLEEP)
            print("\033[1;34m难道说~~~我是穿越了吗？系统，系统，我的金手指在哪里呢？\033[0m")
            time.sleep(_MEDIUM_TIME_SLEEP)
            print("\033[1;34m我的呼喊如石沉大海，音讯全无...\033[0m")
            time.sleep(_MEDIUM_TIME_SLEEP)
            print("\033[1;34m就在我感到绝望的时候，突然...\033[0m")
            time.sleep(_MEDIUM_TIME_SLEEP)
            print("\033[1;34m叮, 恭喜宿主成功穿越，开始绑定系统，当前进度0%....\033[0m")
            time.sleep(_LONG_TIME_SLEEP)
            print("\033[1;34m25%...\033[0m")
            time.sleep(_LONG_TIME_SLEEP)
            print("\033[1;34m50%...\033[0m")
            time.sleep(_LONG_TIME_SLEEP)
            print("\033[1;34m75%...\033[0m")
            time.sleep(_LONG_TIME_SLEEP)
            print("\033[1;34m100%...系统激活成功...\033[0m")
            time.sleep(_MEDIUM_TIME_SLEEP)
            print()
            self.customer_flag["游戏运行次数"][0] += 1
            self.customer_flag.to_csv("./settingsDebug/customerParameters_flag.csv", encoding="gb2312", index=False)

        # print("\033[1;36m欢迎来到无双三国卡牌游戏世界\033[0m")
        # print("\033[1;32m1. 开始游戏\033[0m")
        # print("\033[1;32m2. 退出游戏\033[0m")
        # count = 0
        # while True:
        #     choice = input("\033[1;36m请选择您需要的操作(请输入对应的序号)：\033[0m")
        #     if choice == "1":
        #         if self.customer_flag["开始游戏次数"][0] == 0:
        #             print()
        #             print("\033[1;34m检测到宿主首次开始游戏，特奖励新手大礼包一份\033[0m")
        #             time.sleep(_LONG_TIME_SLEEP)
        #             print("\033[1;34m新手大礼包正在准备中，请等待...\033[0m")
        #             time.sleep(_LONG_TIME_SLEEP)
        #             print("\033[1;34m系统赠送宿主100个金币，新手大礼包已成功发放，请宿主在背包中查收\033[0m")
        #             time.sleep(_LONG_TIME_SLEEP)
        #             print("\033[1;34m快去召唤你的无双英雄陪你一路征战整个世界，笑傲江湖吧\033[0m")
        #             self.customer_flag["开始游戏次数"][0] += 1
        #             self.customer_flag.to_csv("./settingsDebug/customerParameters_flag.csv", encoding="gb2312",
        #                                       index=False)
        #             break
        #         else:
        #             break
        #     elif choice == "2":
        #         # 采用sys.exit()退出整个游戏
        #         self.exitGame()
        #     else:
        #         # 判断，如果三次连续输入错误，强制退出程序。
        #         if count == 2:
        #             print()
        #             print("\033[1;34m看起来您不是真的想要玩这个游戏\033[0m")
        #             time.sleep(_LONG_TIME_SLEEP)
        #             print("\033[1;31m警告：由于您的输入错误次数已经累计达到三次， 强制退出程序已启动...\033[0m")
        #             time.sleep(_LONG_TIME_SLEEP)
        #             print("\033[1;34m强制退出中...\033[0m")
        #             time.sleep(_LONG_TIME_SLEEP)
        #             print("\033[1;34m已强制退出程序\033[0m")
        #             sys.exit()
        #         print("\033[1;32m提示：您输入的选项有误，请输出正确的序号，如：'1' 或者 '2'，剩余可输入次数{}\033[0m".format(2 - count))
        #         print()
        #         count += 1
        #
        # print()
        # print("\033[1;34m正在加载游戏世界...\033[0m")
        # time.sleep(_SHORT_TIME_SLEEP)
        # print("\033[1;34m您已成功进入无双三国世界...., 请尽情的在三国世界中遨游吧！\033[0m")

        while True:
            print()
            print("\033[1;32m1. 对战\033[0m")
            print("\033[1;32m2. 英雄酒馆\033[0m")
            print("\033[1;32m3. 查看英雄属性\033[0m")
            print("\033[1;32m4. 背包\033[0m")
            print("\033[1;32m5. 退出游戏\033[0m")
            choice1 = input("\033[1;36m请选择您需要的操作(请输入对应的序号)：\033[0m")
            if choice1 == "1":
                while True:
                    # 判断用户此时是否具有英雄，若没有，则提示应该获取英雄
                    print()
                    print("\033[1;32m1. PvE副本\033[0m")
                    print("\033[1;32m2. PvP竞技场\033[0m")
                    print("\033[1;32m3. 返回上一级菜单\033[0m")
                    choice2 = input("\033[1;36m请选择您需要的操作(请输入对应的序号)：\033[0m")
                    if choice2 == "1":
                        while True:
                            print()
                            print("\033[1;34m当前副本---第一章 黄巾之乱\033[0m")
                            print("\033[1;34m当前可以挑战的副本列表：\033[0m")
                            print("\033[1;32m1. 副本挑战1-1\033[0m")
                            choice3 = input("\033[1;36m请输入您想要挑战的副本编号:\033[0m ")
                            if choice3 == "1":
                                while True:
                                    print()
                                    print("\033[1;32m1.查看敌方武将信息\033[0m ")
                                    print("\033[1;32m2.挑战\033[0m ")
                                    print("\033[1;32m3.返回副本列表\033[0m ")
                                    choice4 = input("\033[1;36m请选择您需要的操作(请输入对应的序号)：\033[0m")
                                    file = "./settingsDebug/enemyParameters.csv"
                                    # 加载关卡对应敌方武将
                                    self.loadEnemy(file)
                                    if choice4 == "1":
                                        print()
                                        print('\033[1;33m-' * 11 + '敌方属性' + '{0}\033[0m'.format("-" * 11))
                                        print('\033[1;33m|' + "等级" + '{0}'.format(
                                            self.enemy["等级"][0]).rjust(
                                            24) + '|\033[0m')
                                        print('\033[1;33m|' + "星级" + '{0}'.format(
                                            self.enemy["星级"][0]).rjust(
                                            24) + '|\033[0m')
                                        print('\033[1;33m|' + "名称" + '{0}'.format(
                                            self.enemy["名称"][0]).rjust(
                                            22) + '|\033[0m')
                                        print('\033[1;33m|' + "攻击" + '{0}'.format(
                                            self.enemy["攻击"][0]).rjust(
                                            24) + '|\033[0m')
                                        print('\033[1;33m|' + "血量" + '{0}'.format(
                                            self.enemy["血量"][0]).rjust(
                                            24) + '|\033[0m')
                                        print('\033[1;33m|' + "品质" + '{0}'.format(
                                            self.enemy["品质"][0]).rjust(
                                            24) + '|\033[0m')
                                        print('\033[1;33m-\033[0m' * 30)
                                    elif choice4 == "2":
                                        # 从第一个回合开始,count代表当前回合数
                                        count = 1
                                        # 使用场景算法计算场景相关参数
                                        total_length = self.battle_field["总长度"][0]
                                        title_left = np.ceil((total_length - 2 * 3 - len(str(count))) / 2).astype(np.int)
                                        title_right = np.floor((total_length - 2 * 3 - len(str(count))) / 2).astype(np.int)
                                        # e: enemy
                                        # p: player
                                        # 2: 两侧边框部位'|'符号的占用字符数
                                        # 5: ATT和HP字符占用字符数
                                        # 3: 攻击血量之间有一个3个字符的间隔
                                        # 这里的算法还需要优化，+2 -1应该还需要进行细分
                                        e_name_left = np.ceil((total_length - 2 - 2 * len(self.enemy["名称"][0])) / 2).astype(np.int)
                                        e_name_right = np.floor((total_length - 2 - 2 * len(self.enemy["名称"][0])) / 2).astype(
                                            np.int)
                                        e_value_left = np.ceil((total_length - 2 - 2 - 5 - 3 - len(str(self.enemy["攻击"][0])) - len(
                                            str(self.enemy["血量"][0]))) / 2).astype(np.int)
                                        e_value_right = np.floor((total_length - 2 - 2 - 5 - 3 - len(str(self.enemy["攻击"][0])) - len(
                                            str(self.enemy["血量"][0]))) / 2).astype(np.int) - 1

                                        p_name_left = np.ceil((total_length - 2 - 2 * len(self.customer_hero["名称"][0])) / 2).astype(np.int)
                                        p_name_right = np.floor((total_length - 2 - 2 * len(self.customer_hero["名称"][0])) / 2).astype(np.int)
                                        # 注意100与ATT之间，100与HP之间还存在一个空格，因此要额外减2个字符
                                        p_value_left = np.ceil((total_length - 2 - 2 - 5 - 3 - len(str(self.customer_hero["攻击"][0])) - len(
                                            str(self.enemy["血量"][0]))) / 2).astype(np.int)
                                        p_value_right = np.floor((total_length - 2 - 2 - 5 - 3 - len(str(self.customer_hero["攻击"][0])) - len(
                                            str(self.enemy["血量"][0]))) / 2).astype(np.int) - 1
                                        middle_left_right = (total_length - 2).astype(np.int)
                                        # 进入战斗循环体
                                        while self.enemy["血量"][0] > 0:
                                            # 目前简单化模型---玩家先手
                                            # 开始战斗！加载场景算法并绘制战斗场景，然后进行回合制战斗即可
                                            print()
                                            print("{0}第{1}回合{2}".format('-' * title_left, count, '-' * title_right))
                                            print("|{0}\033[1;33m{1}\033[0m{2}|".format(' ' * e_name_left, self.enemy["名称"][0], ' ' * e_name_right))
                                            print("|{0}\033[1;33m{1} ATT{2}{3} HP\033[0m{4}|".format(' ' * e_value_left, self.enemy["攻击"][0], ' ' * 3,
                                                                                                     self.enemy["血量"][0], ' ' * e_value_right))
                                            print("|" + "{0}".format(" " * middle_left_right) + "|")
                                            print("|" + "{0}".format(" " * middle_left_right) + "|")
                                            print("|" + "【{0}】使用拳头对【{1}】造成【{2}】点伤害".format(self.customer_hero["名称"][0], self.enemy["名称"][0],
                                                                                           self.customer_hero["攻击"][0]) + "|")
                                            print("|" + "【{0}】剩余血量【{1}】".format(self.enemy["名称"][0], self.enemy["血量"][0]) + "|")
                                            print("|" + "{0}".format(" " * middle_left_right) + "|")
                                            print("|" + "{0}".format(" " * middle_left_right) + "|")
                                            print("|" + "{0}".format(" " * middle_left_right) + "|")
                                            print(
                                                "|{0}\033[1;33m{1}\033[0m{2}|".format(' ' * p_name_left, self.customer_hero["名称"][0],
                                                                                      ' ' * p_name_right))
                                            print("|{0}\033[1;33m{1} ATT{2}{3} HP\033[0m{4}|".format(' ' * p_value_left, self.customer_hero["攻击"][0],
                                                                                                     ' ' * 3, self.customer_hero["血量"][0],
                                                                                                     ' ' * p_value_right))
                                            print('-' * total_length)
                                            time.sleep(_LONG_TIME_SLEEP)
                                            print()
                                            print("{0}第{1}回合{2}".format('-' * title_left, count, '-' * title_right))
                                            print("|{0}\033[1;33m{1}\033[0m{2}|".format(' ' * e_name_left, self.enemy["名称"][0], ' ' * e_name_right))
                                            print("|{0}\033[1;33m{1} ATT{2}{3} HP\033[0m{4}|".format(' ' * e_value_left, self.enemy["攻击"][0], ' ' * 3,
                                                                                                     self.enemy["血量"][0], ' ' * e_value_right))
                                            print("|" + "{0}".format(" " * middle_left_right) + "|")
                                            print("|" + "{0}".format(" " * middle_left_right) + "|")
                                            print("|" + "{0}使用拳头对{1}造成{2}点伤害".format(self.customer_hero["名称"][0], self.enemy["名称"][0],
                                                                                     self.customer_hero["攻击"][0]) + "|")
                                            print("|" + "【{0}】剩余血量【{1}】".format(self.enemy["名称"][0], self.enemy["血量"][0]) + "|")
                                            print("|" + "{0}".format(" " * middle_left_right) + "|")
                                            print("|" + "{0}".format(" " * middle_left_right) + "|")
                                            print("|" + "{0}".format(" " * middle_left_right) + "|")
                                            print(
                                                "|{0}\033[1;33m{1}\033[0m{2}|".format(' ' * p_name_left, self.customer_hero["名称"][0],
                                                                                      ' ' * p_name_right))
                                            print("|{0}\033[1;33m{1} ATT{2}{3} HP\033[0m{4}|".format(' ' * p_value_left, self.customer_hero["攻击"][0],
                                                                                                     ' ' * 3, self.customer_hero["血量"][0],
                                                                                                     ' ' * p_value_right))
                                            print('-' * total_length)
                                            count += 1
                                    elif choice4 == "3":
                                        break

                            # 得判断输入的参数是否正确！！！后面补充
                            pass
                    elif choice2 == "2":
                        print()
                        print("\033[1;32m竞技场功能正在研发中...请耐心等待...\033[0m")
                        pass
                    # 返回上一级菜单
                    elif choice2 == "3":
                        break
                    else:
                        print("\033[1;32m提示：您输入的选项有误，请输出正确的序号，如：'1' 或者 '2' 或者 '3'\033[0m")

            elif choice1 == "2":
                if self.customer_hero["名字"].any():
                    print()
                    print("\033[1;32m提示：您已经拥有了属于自己的无双武将，请认真培养，酒馆暂时不对您开放\033[0m")
                    continue

                print()
                print("\033[1;34m欢迎来到英雄酒馆~在这里您可以花费金币招募到自己的专属英雄\033[0m")
                print()
                print("\033[1;32m1. 抽取英雄---费用100金币\033[0m")
                print("\033[1;32m2. 退出酒馆\033[0m")
                choice2 = input("\033[1;36m请选择您需要的操作(请输入对应的序号)：\033[0m")
                if choice2 == "1":
                    print()
                    print("\033[1;32m查询到您当前的金币余额为：{0}\033[0m".format(self.customer_object["金币"][0]))
                    time.sleep(_SHORT_TIME_SLEEP)
                    # 先对玩家背包进行判断，看看金币是否够用
                    if self.customer_object["金币"][0] >= 100:
                        print()
                        print("\033[1;34m正在扣除招募资金...\033[0m")
                        time.sleep(_LONG_TIME_SLEEP)
                        print("\033[1;34m抽取英雄进行中....开始施法\033[0m")
                        print("\033[1;34m3...\033[0m")
                        time.sleep(_SHORT_TIME_SLEEP)
                        print("\033[1;34m2...\033[0m")
                        time.sleep(_SHORT_TIME_SLEEP)
                        print("\033[1;34m1...\033[0m")
                        time.sleep(_SHORT_TIME_SLEEP)
                        rand_num = random.randint(0, 9)
                        self.customer_hero = self.heroes_list[rand_num:rand_num + 1]
                        print()
                        print("\033[1;33m恭喜你获得英雄---{0}\033[0m".format(self.customer_hero["名字"][rand_num]))
                        # 一个汉字字符大约为两个英文字符占位
                        print('\033[1;33m-' * 11 + '英雄属性' + '{0}\033[0m'.format("-" * 11))
                        print('\033[1;33m|' + "等级" + '{0}'.format(self.customer_hero["等级"][rand_num]).rjust(
                            24) + '|\033[0m')
                        print('\033[1;33m|' + "姓名" + '{0}'.format(self.customer_hero["名字"][rand_num]).rjust(
                            23) + '|\033[0m')
                        print('\033[1;33m|' + "攻击" + '{0}'.format(self.customer_hero["攻击"][rand_num]).rjust(
                            24) + '|\033[0m')
                        print('\033[1;33m|' + "防御" + '{0}'.format(self.customer_hero["防御"][rand_num]).rjust(
                            24) + '|\033[0m')
                        print('\033[1;33m|' + "血量" + '{0}'.format(self.customer_hero["血量"][rand_num]).rjust(
                            24) + '|\033[0m')
                        print('\033[1;33m|' + "品质" + '{0}'.format(self.customer_hero["品质"][rand_num]).rjust(
                            24) + '|\033[0m')
                        print('\033[1;33m|' + "成长" + '{0}'.format(self.customer_hero["成长系数"][rand_num]).rjust(
                            24) + '|\033[0m')
                        print('\033[1;33m-\033[0m' * 30)
                        self.customer_object["金币"][0] -= 100
                        self.customer_object.to_csv("./settingsDebug/customerParameters_object.csv", encoding="gb2312",
                                                    index=False)
                        self.customer_hero.to_csv("./settingsDebug/customerParameters_hero.csv", encoding="gb2312",
                                                  index=False)
                        # 还需要再读一次，如果是首次创建的角色的话
                        self.customer_hero = pd.read_csv("./settingsDebug/customerParameters_hero.csv",
                                                         encoding="gb2312")
                    else:
                        print("\033[1;32m提示：您的金币余额不足，当前不能够进行英雄召唤\033[0m")

                elif choice2 == "2":
                    pass
                else:
                    print("\033[1;32m提示：您输入的选项有误，请输出正确的序号，如：'1' 或者 '2'\033[0m")
            elif choice1 == "3":
                if not self.customer_hero["名字"].any():
                    print()
                    print("\033[1;32m提示：您还未拥有属于自己的无双武将，请到英雄酒馆进行召唤\033[0m")
                    continue

                print()
                print('\033[1;33m-' * 11 + '英雄属性 ' + '{0}\033[0m'.format('-' * 11))
                print('\033[1;33m|' + "等级" + '{0}'.format(self.customer_hero["等级"][0]).rjust(24) + '|\033[0m')
                print('\033[1;33m|' + "姓名" + '{0}'.format(self.customer_hero["名字"][0]).rjust(23) + '|\033[0m')
                print('\033[1;33m|' + "攻击" + '{0}'.format(self.customer_hero["攻击"][0]).rjust(24) + '|\033[0m')
                print('\033[1;33m|' + "防御" + '{0}'.format(self.customer_hero["防御"][0]).rjust(24) + '|\033[0m')
                print('\033[1;33m|' + "血量" + '{0}'.format(self.customer_hero["血量"][0]).rjust(24) + '|\033[0m')
                print('\033[1;33m|' + "品质" + '{0}'.format(self.customer_hero["品质"][0]).rjust(24) + '|')
                print('\033[1;33m|' + "成长" + '{0}'.format(self.customer_hero["成长系数"][0]).rjust(24) + '|\033[0m')
                print('\033[1;33m-\033[0m' * 30)

            elif choice1 == "4":
                print()
                print("\033[1;33m您当前所有拥有的物品如下：\033[0m")
                print("\033[1;33m金币：{0}\033[0m".format(self.customer_object["金币"][0]))

                # 可以不加返回选项，自动返回主界面
            elif choice1 == "5":
                self.exitGame()

            else:
                print("\033[1;32m提示：您输入的选项有误，请输出正确的序号，如：'1' 或者 '2' 或者 '3' 或者 '4'\033[0m")

    def exitGame(self):
        print()
        time.sleep(_MEDIUM_TIME_SLEEP)
        print("\033[1;34m正在进行退出游戏前的准备...\033[0m")
        time.sleep(_LONG_TIME_SLEEP)
        print("\033[1;34m正在注销账号...\033[0m")
        time.sleep(_LONG_TIME_SLEEP)
        print("\033[1;34m正在退出游戏...\033[0m")
        time.sleep(_LONG_TIME_SLEEP)
        print("\033[1;34m已成功退出三国游戏世界...等待您的下次登入...\033[0m")
        sys.exit()

    def loadEnemy(self, file):
        self.enemy = pd.read_csv(file, encoding="gb2312")


if __name__ == '__main__':
    game = ThreeKingdomGame()
    game.MainGame()
