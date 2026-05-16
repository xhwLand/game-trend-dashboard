"""
抖音小游戏排行榜爬虫
数据来源：抖音游戏中心公开榜单
"""
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime


def get_douyin_games():
    """
    获取抖音小游戏排行榜数据
    返回格式：[{'rank': 1, 'name': '游戏名', 'type': '类型', 'hot_score': 热度, 'trend': '趋势'}]
    """
    games = []
    
    # 模拟数据（实际使用时替换为真实爬虫代码）
    # 抖音小游戏排行榜数据源：https://game.douyin.com/
    
    sample_games = [
        {'rank': 1, 'name': '贪吃蛇大作战', 'type': '休闲', 'hot_score': 9856, 'trend': 'up'},
        {'rank': 2, 'name': '消灭星星', 'type': '益智', 'hot_score': 9723, 'trend': 'up'},
        {'rank': 3, 'name': '跳一跳', 'type': '休闲', 'hot_score': 9654, 'trend': 'down'},
        {'rank': 4, 'name': '植物大战僵尸2', 'type': '策略', 'hot_score': 9521, 'trend': 'up'},
        {'rank': 5, 'name': '保卫萝卜', 'type': '塔防', 'hot_score': 9487, 'trend': 'stable'},
        {'rank': 6, 'name': '开心消消乐', 'type': '消除', 'hot_score': 9432, 'trend': 'up'},
        {'rank': 7, 'name': '球球大作战', 'type': '休闲', 'hot_score': 9315, 'trend': 'down'},
        {'rank': 8, 'name': '穿越火线', 'type': '射击', 'hot_score': 9287, 'trend': 'up'},
        {'rank': 9, 'name': '王者荣耀', 'type': 'MOBA', 'hot_score': 9254, 'trend': 'stable'},
        {'rank': 10, 'name': '和平精英', 'type': '射击', 'hot_score': 9213, 'trend': 'up'},
        {'rank': 11, 'name': '欢乐斗地主', 'type': '棋牌', 'hot_score': 9156, 'trend': 'up'},
        {'rank': 12, 'name': '迷你世界', 'type': '沙盒', 'hot_score': 9087, 'trend': 'down'},
        {'rank': 13, 'name': '我的世界', 'type': '沙盒', 'hot_score': 9021, 'trend': 'stable'},
        {'rank': 14, 'name': '明日方舟', 'type': '策略', 'hot_score': 8954, 'trend': 'up'},
        {'rank': 15, 'name': '阴阳师', 'type': '回合制', 'hot_score': 8897, 'trend': 'down'},
        {'rank': 16, 'name': '原神', 'type': 'RPG', 'hot_score': 8832, 'trend': 'up'},
        {'rank': 17, 'name': '崩坏3', 'type': '动作', 'hot_score': 8765, 'trend': 'stable'},
        {'rank': 18, 'name': 'QQ飞车', 'type': '竞速', 'hot_score': 8698, 'trend': 'up'},
        {'rank': 19, 'name': '跑跑卡丁车', 'type': '竞速', 'hot_score': 8632, 'trend': 'down'},
        {'rank': 20, 'name': '神庙逃亡', 'type': '跑酷', 'hot_score': 8567, 'trend': 'up'},
        {'rank': 21, 'name': '地铁跑酷', 'type': '跑酷', 'hot_score': 8498, 'trend': 'stable'},
        {'rank': 22, 'name': '天天酷跑', 'type': '跑酷', 'hot_score': 8432, 'trend': 'down'},
        {'rank': 23, 'name': '部落冲突', 'type': '策略', 'hot_score': 8365, 'trend': 'up'},
        {'rank': 24, 'name': '皇室战争', 'type': '卡牌', 'hot_score': 8298, 'trend': 'stable'},
        {'rank': 25, 'name': '荒野行动', 'type': '射击', 'hot_score': 8231, 'trend': 'down'},
        {'rank': 26, 'name': '和平暖暖', 'type': '换装', 'hot_score': 8165, 'trend': 'up'},
        {'rank': 27, 'name': '奇迹暖暖', 'type': '换装', 'hot_score': 8098, 'trend': 'stable'},
        {'rank': 28, 'name': '闪耀暖暖', 'type': '换装', 'hot_score': 8032, 'trend': 'up'},
        {'rank': 29, 'name': '恋与制作人', 'type': '乙女', 'hot_score': 7965, 'trend': 'down'},
        {'rank': 30, 'name': '光与夜之恋', 'type': '乙女', 'hot_score': 7898, 'trend': 'up'},
        {'rank': 31, 'name': '未定事件簿', 'type': '推理', 'hot_score': 7831, 'trend': 'stable'},
        {'rank': 32, 'name': '狼人杀', 'type': '社交', 'hot_score': 7765, 'trend': 'up'},
        {'rank': 33, 'name': '太空狼人杀', 'type': '社交', 'hot_score': 7698, 'trend': 'down'},
        {'rank': 34, 'name': 'Among Us', 'type': '社交', 'hot_score': 7632, 'trend': 'stable'},
        {'rank': 35, 'name': '蛋仔派对', 'type': '休闲', 'hot_score': 7565, 'trend': 'up'},
        {'rank': 36, 'name': '元梦之星', 'type': '休闲', 'hot_score': 7498, 'trend': 'up'},
        {'rank': 37, 'name': '植物大战僵尸', 'type': '塔防', 'hot_score': 7432, 'trend': 'stable'},
        {'rank': 38, 'name': 'pvz', 'type': '塔防', 'hot_score': 7365, 'trend': 'down'},
        {'rank': 39, 'name': '愤怒的小鸟', 'type': '休闲', 'hot_score': 7298, 'trend': 'up'},
        {'rank': 40, 'name': '神庙逃亡2', 'type': '跑酷', 'hot_score': 7232, 'trend': 'stable'},
        {'rank': 41, 'name': '滑雪大冒险', 'type': '休闲', 'hot_score': 7165, 'trend': 'down'},
        {'rank': 42, 'name': '涂鸦跳跃', 'type': '休闲', 'hot_score': 7098, 'trend': 'up'},
        {'rank': 43, 'name': '跳舞的线', 'type': '音乐', 'hot_score': 7032, 'trend': 'stable'},
        {'rank': 44, 'name': '钢琴块', 'type': '音乐', 'hot_score': 6965, 'trend': 'down'},
        {'rank': 45, 'name': '节奏大师', 'type': '音乐', 'hot_score': 6898, 'trend': 'up'},
        {'rank': 46, 'name': 'Cytus', 'type': '音乐', 'hot_score': 6832, 'trend': 'stable'},
        {'rank': 47, 'name': 'Deemo', 'type': '音乐', 'hot_score': 6765, 'trend': 'down'},
        {'rank': 48, 'name': '滚动的天空', 'type': '休闲', 'hot_score': 6698, 'trend': 'up'},
        {'rank': 49, 'name': '几何冲刺', 'type': '休闲', 'hot_score': 6632, 'trend': 'stable'},
        {'rank': 50, 'name': '跳舞的球', 'type': '休闲', 'hot_score': 6565, 'trend': 'down'},
    ]
    
    return sample_games


def save_douyin_data():
    """保存抖音数据到JSON文件"""
    games = get_douyin_games()
    today = datetime.now().strftime('%Y-%m-%d')
    
    data = {
        'platform': '抖音小游戏',
        'update_date': today,
        'update_time': datetime.now().isoformat(),
        'count': len(games),
        'games': games
    }
    
    output_dir = 'data/douyin'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{today}.json')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 同时保存最新数据到 latest.json
    with open(os.path.join(output_dir, 'latest.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"抖音小游戏数据已保存: {output_file}")
    return data


if __name__ == '__main__':
    save_douyin_data()
