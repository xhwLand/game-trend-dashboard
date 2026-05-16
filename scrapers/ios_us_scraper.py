"""
iOS缇庡尯鍏嶈垂娓告垙鎺掕姒滅埇铏?鏁版嵁鏉ユ簮锛欰pp Store鍏紑姒滃崟
"""
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime


def get_ios_us_games():
    """
    鑾峰彇iOS缇庡尯鍏嶈垂娓告垙鎺掕姒滄暟鎹?    杩斿洖鏍煎紡锛歔{'rank': 1, 'name': '娓告垙鍚?, 'developer': '寮€鍙戝晢', 'category': '绫诲埆', 'rating': 4.5}]
    """
    games = []
    
    # 妯℃嫙鏁版嵁锛堝疄闄呬娇鐢ㄦ椂鏇挎崲涓虹湡瀹炵埇铏唬鐮侊級
    # iOS缇庡尯姒滃崟鏁版嵁婧愶細https://apps.apple.com/us/charts/iphone/games/free
    # 闇€瑕佷娇鐢╥Tunes API鎴栫綉椤电埇鍙?    
    sample_games = [
        {'rank': 1, 'name': 'Subway Surfers', 'developer': 'SYBO Games', 'category': 'Runner', 'rating': 4.7},
        {'rank': 2, 'name': 'Candy Crush Saga', 'developer': 'King', 'category': 'Puzzle', 'rating': 4.6},
        {'rank': 3, 'name': 'Temple Run', 'developer': 'Imangi Studios', 'category': 'Runner', 'rating': 4.5},
        {'rank': 4, 'name': 'Among Us', 'developer': 'InnerSloth LLC', 'category': 'Party', 'rating': 4.8},
        {'rank': 5, 'name': 'Roblox', 'developer': 'Roblox Corporation', 'category': 'Adventure', 'rating': 4.5},
        {'rank': 6, 'name': 'Geometry Dash', 'developer': 'RobTop Games', 'category': 'Rhythm', 'rating': 4.7},
        {'rank': 7, 'name': 'Hill Climb Racing', 'developer': 'Fingersoft', 'category': 'Racing', 'rating': 4.6},
        {'rank': 8, 'name': 'Monopoly GO!', 'developer': 'Scopely', 'category': 'Board', 'rating': 4.4},
        {'rank': 9, 'name': 'PUBG Mobile', 'developer': 'Tencent Games', 'category': 'Shooter', 'rating': 4.5},
        {'rank': 10, 'name': 'Minecraft', 'developer': 'Mojang', 'category': 'Sandbox', 'rating': 4.8},
        {'rank': 11, 'name': 'Crossy Road', 'developer': 'Hipster Whale', 'category': 'Arcade', 'rating': 4.6},
        {'rank': 12, 'name': 'Stumble Guys', 'developer': 'Kitka Games', 'category': 'Party', 'rating': 4.5},
        {'rank': 13, 'name': 'Toca Life World', 'developer': 'Toca Boca', 'category': 'Kids', 'rating': 4.4},
        {'rank': 14, 'name': 'FIFA Mobile', 'developer': 'EA Sports', 'category': 'Sports', 'rating': 4.3},
        {'rank': 15, 'name': '8 Ball Pool', 'developer': 'Miniclip', 'category': 'Sports', 'rating': 4.6},
        {'rank': 16, 'name': 'Brawl Stars', 'developer': 'Supercell', 'category': 'Action', 'rating': 4.5},
        {'rank': 17, 'name': 'Clash Royale', 'developer': 'Supercell', 'category': 'Strategy', 'rating': 4.6},
        {'rank': 18, 'name': 'Clash of Clans', 'developer': 'Supercell', 'category': 'Strategy', 'rating': 4.7},
        {'rank': 19, 'name': 'Gardenscapes', 'developer': 'Playrix', 'category': 'Puzzle', 'rating': 4.5},
        {'rank': 20, 'name': 'Homescapes', 'developer': 'Playrix', 'category': 'Puzzle', 'rating': 4.5},
        {'rank': 21, 'name': 'Township', 'developer': 'Playrix', 'category': 'Simulation', 'rating': 4.6},
        {'rank': 22, 'name': 'Temple Run 2', 'developer': 'Imangi Studios', 'category': 'Runner', 'rating': 4.5},
        {'rank': 23, 'name': 'Jetpack Joyride', 'developer': 'Halfbrick', 'category': 'Runner', 'rating': 4.6},
        {'rank': 24, 'name': 'Fruit Ninja', 'developer': 'Halfbrick', 'category': 'Arcade', 'rating': 4.5},
        {'rank': 25, 'name': 'Angry Birds 2', 'developer': 'Rovio', 'category': 'Puzzle', 'rating': 4.4},
        {'rank': 26, 'name': 'Flappy Bird', 'developer': 'Gears Interactive', 'category': 'Arcade', 'rating': 4.2},
        {'rank': 27, 'name': '2048', 'developer': 'Ketchapp', 'category': 'Puzzle', 'rating': 4.3},
        {'rank': 28, 'name': 'Dumb Ways to Die', 'developer': 'Metro Trains', 'category': 'Arcade', 'rating': 4.5},
        {'rank': 29, 'name': 'Cut the Rope', 'developer': 'ZeptoLab', 'category': 'Puzzle', 'rating': 4.6},
        {'rank': 30, 'name': 'Dots', 'developer': 'Dots', 'category': 'Puzzle', 'rating': 4.4},
        {'rank': 31, 'name': 'Two Dots', 'developer': 'Dots', 'category': 'Puzzle', 'rating': 4.5},
        {'rank': 32, 'name': 'Candy Crush Soda Saga', 'developer': 'King', 'category': 'Puzzle', 'rating': 4.5},
        {'rank': 33, 'name': 'Bejeweled', 'developer': 'EA', 'category': 'Puzzle', 'rating': 4.4},
        {'rank': 34, 'name': 'Diamond Mine', 'developer': 'PopCap', 'category': 'Puzzle', 'rating': 4.3},
        {'rank': 35, 'name': 'Zookeeper', 'developer': 'Nintendo', 'category': 'Puzzle', 'rating': 4.5},
        {'rank': 36, 'name': 'Tiny Wings', 'developer': 'Andreas Iljedsson', 'category': 'Arcade', 'rating': 4.6},
        {'rank': 37, 'name': 'Bad Piggies', 'developer': 'Rovio', 'category': 'Puzzle', 'rating': 4.5},
        {'rank': 38, 'name': 'Where is My Water', 'developer': 'Disney', 'category': 'Puzzle', 'rating': 4.4},
        {'rank': 39, 'name': 'Where's My Perry', 'developer': 'Disney', 'category': 'Puzzle', 'rating': 4.4},
        {'rank': 40, 'name': 'Mighty Mighty', 'developer': 'Mediatonic', 'category': 'Arcade', 'rating': 4.3},
        {'rank': 41, 'name': 'Duel Links', 'developer': 'Konami', 'category': 'Card', 'rating': 4.5},
        {'rank': 42, 'name': 'Marvel Contest', 'developer': 'Kabam', 'category': 'RPG', 'rating': 4.4},
        {'rank': 43, 'name': 'Star Wars Galaxy', 'developer': 'EA', 'category': 'RPG', 'rating': 4.3},
        {'rank': 44, 'name': 'Harry Potter', 'developer': 'Jam City', 'category': 'Puzzle', 'rating': 4.4},
        {'rank': 45, 'name': 'Sonic Dash', 'developer': 'Sega', 'category': 'Runner', 'rating': 4.5},
        {'rank': 46, 'name': 'Tasty Treats', 'developer': 'Jam City', 'category': 'Puzzle', 'rating': 4.3},
        {'rank': 47, 'name': 'Pokemon GO', 'developer': 'Niantic', 'category': 'AR', 'rating': 4.6},
        {'rank': 48, 'name': 'Mario Kart Tour', 'developer': 'Nintendo', 'category': 'Racing', 'rating': 4.2},
        {'rank': 49, 'name': 'Sonic Forces', 'developer': 'Sega', 'category': 'Action', 'rating': 4.3},
        {'rank': 50, 'name': 'Asphalt 9', 'developer': 'Gameloft', 'category': 'Racing', 'rating': 4.5},
    ]
    
    return sample_games


def save_ios_us_data():
    """淇濆瓨iOS缇庡尯鏁版嵁鍒癑SON鏂囦欢"""
    games = get_ios_us_games()
    today = datetime.now().strftime('%Y-%m-%d')
    
    data = {
        'platform': 'iOS缇庡尯鍏嶈垂姒?,
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
    
    # 鍚屾椂淇濆瓨鏈€鏂版暟鎹埌 latest.json
    with open(os.path.join(output_dir, 'latest.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"iOS缇庡尯鏁版嵁宸蹭繚瀛? {output_file}")
    return data


if __name__ == '__main__':
    save_ios_us_data()
