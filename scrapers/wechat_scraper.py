"""
微信小游戏排行榜爬虫
数据来源：微信小游戏中心公开榜单
"""
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime


def get_wechat_games():
    """
    获取微信小游戏排行榜数据
    返回格式：[{'rank': 1, 'name': '游戏名', 'type': '类型', 'hot_score': 热度, 'trend': '趋势'}]
    """
    games = []
    
    # 模拟数据（实际使用时替换为真实爬虫代码）
    # 微信小游戏排行榜数据源：https://game.wechat.com/
    
    sample_games = [
        {'rank': 1, 'name': '跳一跳', 'type': '休闲', 'hot_score': 9923, 'trend': 'up'},
        {'rank': 2, 'name': '欢乐斗地主', 'type': '棋牌', 'hot_score': 9856, 'trend': 'stable'},
        {'rank': 3, 'name': '欢乐麻将', 'type': '棋牌', 'hot_score': 9789, 'trend': 'up'},
        {'rank': 4, 'name': '天天象棋', 'type': '棋牌', 'hot_score': 9723, 'trend': 'down'},
        {'rank': 5, 'name': '腾讯欢乐捕鱼', 'type': '休闲', 'hot_score': 9656, 'trend': 'up'},
        {'rank': 6, 'name': '拳皇命运', 'type': '动作', 'hot_score': 9589, 'trend': 'stable'},
        {'rank': 7, 'name': '火柴人战争', 'type': '策略', 'hot_score': 9523, 'trend': 'up'},
        {'rank': 8, 'name': '植物大战僵尸', 'type': '塔防', 'hot_score': 9456, 'trend': 'down'},
        {'rank': 9, 'name': '保卫萝卜', 'type': '塔防', 'hot_score': 9389, 'trend': 'stable'},
        {'rank': 10, 'name': '开心消消乐', 'type': '消除', 'hot_score': 9323, 'trend': 'up'},
        {'rank': 11, 'name': '消灭星星', 'type': '消除', 'hot_score': 9256, 'trend': 'up'},
        {'rank': 12, 'name': '泡泡龙', 'type': '消除', 'hot_score': 9189, 'trend': 'down'},
        {'rank': 13, 'name': '贪吃蛇大作战', 'type': '休闲', 'hot_score': 9123, 'trend': 'stable'},
        {'rank': 14, 'name': '球球大作战', 'type': '休闲', 'hot_score': 9056, 'trend': 'up'},
        {'rank': 15, 'name': '钢琴块2', 'type': '音乐', 'hot_score': 8989, 'trend': 'down'},
        {'rank': 16, 'name': '跳舞的线', 'type': '音乐', 'hot_score': 8923, 'trend': 'stable'},
        {'rank': 17, 'name': '节奏大师', 'type': '音乐', 'hot_score': 8856, 'trend': 'up'},
        {'rank': 18, 'name': '神庙逃亡', 'type': '跑酷', 'hot_score': 8789, 'trend': 'down'},
        {'rank': 19, 'name': '地铁跑酷', 'type': '跑酷', 'hot_score': 8723, 'trend': 'up'},
        {'rank': 20, 'name': '天天酷跑', 'type': '跑酷', 'hot_score': 8656, 'trend': 'stable'},
        {'rank': 21, 'name': '穿越火线', 'type': '射击', 'hot_score': 8589, 'trend': 'up'},
        {'rank': 22, 'name': '王者荣耀', 'type': 'MOBA', 'hot_score': 8523, 'trend': 'down'},
        {'rank': 23, 'name': '和平精英', 'type': '射击', 'hot_score': 8456, 'trend': 'stable'},
        {'rank': 24, 'name': 'QQ飞车', 'type': '竞速', 'hot_score': 8389, 'trend': 'up'},
        {'rank': 25, 'name': '跑跑卡丁车', 'type': '竞速', 'hot_score': 8323, 'trend': 'down'},
        {'rank': 26, 'name': '欢乐坦克大战', 'type': '射击', 'hot_score': 8256, 'trend': 'up'},
        {'rank': 27, 'name': '全民飞机大战', 'type': '飞行射击', 'hot_score': 8189, 'trend': 'stable'},
        {'rank': 28, 'name': '雷霆战机', 'type': '飞行射击', 'hot_score': 8123, 'trend': 'down'},
        {'rank': 29, 'name': '部落冲突', 'type': '策略', 'hot_score': 8056, 'trend': 'up'},
        {'rank': 30, 'name': '皇室战争', 'type': '卡牌', 'hot_score': 7989, 'trend': 'stable'},
        {'rank': 31, 'name': '荒野行动', 'type': '射击', 'hot_score': 7923, 'trend': 'down'},
        {'rank': 32, 'name': '我的世界', 'type': '沙盒', 'hot_score': 7856, 'trend': 'up'},
        {'rank': 33, 'name': '迷你世界', 'type': '沙盒', 'hot_score': 7789, 'trend': 'stable'},
        {'rank': 34, 'name': '蛋仔派对', 'type': '休闲', 'hot_score': 7723, 'trend': 'up'},
        {'rank': 35, 'name': '元梦之星', 'type': '休闲', 'hot_score': 7656, 'trend': 'up'},
        {'rank': 36, 'name': '羊了个羊', 'type': '消除', 'hot_score': 7589, 'trend': 'down'},
        {'rank': 37, 'name': '来找茬', 'type': '益智', 'hot_score': 7523, 'trend': 'stable'},
        {'rank': 38, 'name': '大家来找茬', 'type': '益智', 'hot_score': 7456, 'trend': 'up'},
        {'rank': 39, 'name': '你画我猜', 'type': '社交', 'hot_score': 7389, 'trend': 'down'},
        {'rank': 40, 'name': '谁是卧底', 'type': '社交', 'hot_score': 7323, 'trend': 'stable'},
        {'rank': 41, 'name': '狼人杀', 'type': '社交', 'hot_score': 7256, 'trend': 'up'},
        {'rank': 42, 'name': '太空狼人杀', 'type': '社交', 'hot_score': 7189, 'trend': 'down'},
        {'rank': 43, 'name': '五子棋', 'type': '棋牌', 'hot_score': 7123, 'trend': 'stable'},
        {'rank': 44, 'name': '围棋', 'type': '棋牌', 'hot_score': 7056, 'trend': 'up'},
        {'rank': 45, 'name': '国际象棋', 'type': '棋牌', 'hot_score': 6989, 'trend': 'down'},
        {'rank': 46, 'name': '飞行棋', 'type': '棋牌', 'hot_score': 6923, 'trend': 'stable'},
        {'rank': 47, 'name': '大富翁', 'type': '棋牌', 'hot_score': 6856, 'trend': 'up'},
        {'rank': 48, 'name': '斗地主', 'type': '棋牌', 'hot_score': 6789, 'trend': 'down'},
        {'rank': 49, 'name': '四川麻将', 'type': '棋牌', 'hot_score': 6723, 'trend': 'stable'},
        {'rank': 50, 'name': '广东麻将', 'type': '棋牌', 'hot_score': 6656, 'trend': 'up'},
    ]
    
    return games


def save_wechat_data():
    """保存微信数据到JSON文件"""
    games = get_wechat_games()
    today = datetime.now().strftime('%Y-%m-%d')
    
    data = {
        'platform': '微信小游戏',
        'update_date': today,
        'update_time': datetime.now().isoformat(),
        'count': len(games),
        'games': games
    }
    
    output_dir = 'data/wechat'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{today}.json')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 同时保存最新数据到 latest.json
    with open(os.path.join(output_dir, 'latest.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"微信小游戏数据已保存: {output_file}")
    return data


if __name__ == '__main__':
    save_wechat_data()
