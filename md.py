



if __name__ == '__main__':
    # pytorch 使用的是不是gpu  true是
    import torch
    print(torch.cuda.is_available())


    '''
    
    https://gpushare.com/store          V100/32g  3块/1小时

    
    控制鼠标键的包
        目前使用
            pydirectinput   
            pyautogui
        
        PyUserInput
        pynput
    https://github.com/taojy123/KeymouseGo  按键精灵
    
    
    Person      -- 人物  20
    WuPin       -- 物品  10*金币
    Men         -- 门    60
    Monster     -- 怪物 35
    BossJiangLi -- boss 奖励  40
    NextPerson  -- 下一个角色   10
    NextGame    -- 下一句游戏     10
    
    160
    
    a -- 第一张地图 
    b -- 第二张地图
    c -- 第三张地图
    d -- 第四张地图
    e -- 第五张地图
    f -- 第六张地图
    g -- boss 地图
    
    35
    
    195  基础
    
    人物 * 20  站立左 站立右  跑左 跑右
    物品 * 1000  金币 材料 装备 

    https://github.com/fzls/djc_helper
    https://github.com/awsay/game-helper
    https://github.com/Zageku/DNF_pvf_python
    
    
    
    '''

    pass