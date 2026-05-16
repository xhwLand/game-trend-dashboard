"""
iOS美区免费游戏排行榜爬虫
数据来源：Apple官方RSS API (itunes.apple.com)
"""
import requests
import json
import os
from datetime import datetime


def get_ios_us_games():
    """
    通过Apple官方RSS API获取iOS美区免费游戏排行榜
    返回格式：[{'rank': 1, 'name': '游戏名', 'developer': '开发商', 'category': '类别', 'rating': 0}]
    """
    url = "https://itunes.apple.com/us/rss/topfreeapplications/limit=100/genre=6014/json"
    
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        
        games = []
        entries = data.get('feed', {}).get('entry', [])
        
        for i, entry in enumerate(entries):
            name = entry.get('im:name', {}).get('label', 'Unknown')
            developer = entry.get('im:artist', {}).get('label', 'Unknown')
            category = entry.get('category', {}).get('attributes', {}).get('term', 'Games')
            
            games.append({
                'rank': i + 1,
                'name': name,
                'developer': developer,
                'category': category,
                'score': 0  # RSS API不含评分数据
            })
            
            if i + 1 >= 50:  # 只取前50
                break
        
        return games
    
    except Exception as e:
        print(f"iOS API请求失败: {e}")
        return []


def save_ios_us_data():
    """保存iOS美区数据到JSON文件"""
    games = get_ios_us_games()
    today = datetime.now().strftime('%Y-%m-%d')
    
    data = {
        'platform': 'iOS美区免费榜',
        'update_date': today,
        'update_time': datetime.now().isoformat(),
        'count': len(games),
        'games': games
    }
    
    output_dir = 'data/ios_us'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{today}.json')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    with open(os.path.join(output_dir, 'latest.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"iOS美区数据已保存: {output_file}")
    return data


if __name__ == '__main__':
    save_ios_us_data()
