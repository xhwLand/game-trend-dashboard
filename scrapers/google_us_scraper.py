"""
Google Play美区免费游戏排行榜爬虫
数据来源：google_play_scraper库
"""
from google_play_scraper import search
import json
import os
from datetime import datetime


def get_google_us_games():
    """通过google_play_scraper获取Google Play美区热门游戏"""
    try:
        result = search(
            "games",
            lang="en",
            country="us",
            n_hits=50
        )
        
        games = []
        for i, app in enumerate(result[:50]):
            games.append({
                'rank': i + 1,
                'name': app.get('title', 'Unknown'),
                'developer': app.get('developer', ''),
                'category': app.get('genre', 'Games'),
                'score': app.get('score', 0) or 0
            })
        
        return games
    
    except Exception as e:
        print(f"Google Play抓取失败: {e}")
        return []


def save_google_us_data():
    """保存Google Play美区数据到JSON文件"""
    games = get_google_us_games()
    today = datetime.now().strftime('%Y-%m-%d')
    
    data = {
        'platform': 'Google Play美区免费榜',
        'update_date': today,
        'update_time': datetime.now().isoformat(),
        'count': len(games),
        'games': games
    }
    
    output_dir = 'data/google_us'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{today}.json')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    with open(os.path.join(output_dir, 'latest.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Google Play美区数据已保存: {output_file}")
    return data


if __name__ == '__main__':
    save_google_us_data()
