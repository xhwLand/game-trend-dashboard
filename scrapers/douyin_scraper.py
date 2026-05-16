"""
鎶栭煶灏忔父鎴忔帓琛屾鐖櫕
鏁版嵁鏉ユ簮锛氭姈闊虫父鎴忎腑蹇冨叕寮€姒滃崟
"""
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime


def get_douyin_games():
    """
    鑾峰彇鎶栭煶灏忔父鎴忔帓琛屾鏁版嵁
    杩斿洖鏍煎紡锛歔{'rank': 1, 'name': '娓告垙鍚?, 'type': '绫诲瀷', 'hot_score': 鐑害, 'trend': '瓒嬪娍'}]
    """
    games = []
    
    # 妯℃嫙鏁版嵁锛堝疄闄呬娇鐢ㄦ椂鏇挎崲涓虹湡瀹炵埇铏唬鐮侊級
    # 鎶栭煶灏忔父鎴忔帓琛屾鏁版嵁婧愶細https://game.douyin.com/
    
    sample_games = [
        {'rank': 1, 'name': '璐悆铔囧ぇ浣滄垬', 'type': '浼戦棽', 'hot_score': 9856, 'trend': 'up'},
        {'rank': 2, 'name': '娑堢伃鏄熸槦', 'type': '鐩婃櫤', 'hot_score': 9723, 'trend': 'up'},
        {'rank': 3, 'name': '璺充竴璺?, 'type': '浼戦棽', 'hot_score': 9654, 'trend': 'down'},
        {'rank': 4, 'name': '妞嶇墿澶ф垬鍍靛案2', 'type': '绛栫暐', 'hot_score': 9521, 'trend': 'up'},
        {'rank': 5, 'name': '淇濆崼钀濆崪', 'type': '濉旈槻', 'hot_score': 9487, 'trend': 'stable'},
        {'rank': 6, 'name': '寮€蹇冩秷娑堜箰', 'type': '娑堥櫎', 'hot_score': 9432, 'trend': 'up'},
        {'rank': 7, 'name': '鐞冪悆澶т綔鎴?, 'type': '浼戦棽', 'hot_score': 9315, 'trend': 'down'},
        {'rank': 8, 'name': '绌胯秺鐏嚎', 'type': '灏勫嚮', 'hot_score': 9287, 'trend': 'up'},
        {'rank': 9, 'name': '鐜嬭€呰崳鑰€', 'type': 'MOBA', 'hot_score': 9254, 'trend': 'stable'},
        {'rank': 10, 'name': '鍜屽钩绮捐嫳', 'type': '灏勫嚮', 'hot_score': 9213, 'trend': 'up'},
        {'rank': 11, 'name': '娆箰鏂楀湴涓?, 'type': '妫嬬墝', 'hot_score': 9156, 'trend': 'up'},
        {'rank': 12, 'name': '杩蜂綘涓栫晫', 'type': '娌欑洅', 'hot_score': 9087, 'trend': 'down'},
        {'rank': 13, 'name': '鎴戠殑涓栫晫', 'type': '娌欑洅', 'hot_score': 9021, 'trend': 'stable'},
        {'rank': 14, 'name': '鏄庢棩鏂硅垷', 'type': '绛栫暐', 'hot_score': 8954, 'trend': 'up'},
        {'rank': 15, 'name': '闃撮槼甯?, 'type': '鍥炲悎鍒?, 'hot_score': 8897, 'trend': 'down'},
        {'rank': 16, 'name': '鍘熺', 'type': 'RPG', 'hot_score': 8832, 'trend': 'up'},
        {'rank': 17, 'name': '宕╁潖3', 'type': '鍔ㄤ綔', 'hot_score': 8765, 'trend': 'stable'},
        {'rank': 18, 'name': 'QQ椋炶溅', 'type': '绔為€?, 'hot_score': 8698, 'trend': 'up'},
        {'rank': 19, 'name': '璺戣窇鍗′竵杞?, 'type': '绔為€?, 'hot_score': 8632, 'trend': 'down'},
        {'rank': 20, 'name': '绁炲簷閫冧骸', 'type': '璺戦叿', 'hot_score': 8567, 'trend': 'up'},
        {'rank': 21, 'name': '鍦伴搧璺戦叿', 'type': '璺戦叿', 'hot_score': 8498, 'trend': 'stable'},
        {'rank': 22, 'name': '澶╁ぉ閰疯窇', 'type': '璺戦叿', 'hot_score': 8432, 'trend': 'down'},
        {'rank': 23, 'name': '閮ㄨ惤鍐茬獊', 'type': '绛栫暐', 'hot_score': 8365, 'trend': 'up'},
        {'rank': 24, 'name': '鐨囧鎴樹簤', 'type': '鍗＄墝', 'hot_score': 8298, 'trend': 'stable'},
        {'rank': 25, 'name': '鑽掗噹琛屽姩', 'type': '灏勫嚮', 'hot_score': 8231, 'trend': 'down'},
        {'rank': 26, 'name': '鍜屽钩鏆栨殩', 'type': '鎹㈣', 'hot_score': 8165, 'trend': 'up'},
        {'rank': 27, 'name': '濂囪抗鏆栨殩', 'type': '鎹㈣', 'hot_score': 8098, 'trend': 'stable'},
        {'rank': 28, 'name': '闂€€鏆栨殩', 'type': '鎹㈣', 'hot_score': 8032, 'trend': 'up'},
        {'rank': 29, 'name': '鎭嬩笌鍒朵綔浜?, 'type': '涔欏コ', 'hot_score': 7965, 'trend': 'down'},
        {'rank': 30, 'name': '鍏変笌澶滀箣鎭?, 'type': '涔欏コ', 'hot_score': 7898, 'trend': 'up'},
        {'rank': 31, 'name': '鏈畾浜嬩欢绨?, 'type': '鎺ㄧ悊', 'hot_score': 7831, 'trend': 'stable'},
        {'rank': 32, 'name': '鐙间汉鏉€', 'type': '绀句氦', 'hot_score': 7765, 'trend': 'up'},
        {'rank': 33, 'name': '澶┖鐙间汉鏉€', 'type': '绀句氦', 'hot_score': 7698, 'trend': 'down'},
        {'rank': 34, 'name': 'Among Us', 'type': '绀句氦', 'hot_score': 7632, 'trend': 'stable'},
        {'rank': 35, 'name': '铔嬩粩娲惧', 'type': '浼戦棽', 'hot_score': 7565, 'trend': 'up'},
        {'rank': 36, 'name': '鍏冩ⅵ涔嬫槦', 'type': '浼戦棽', 'hot_score': 7498, 'trend': 'up'},
        {'rank': 37, 'name': '妞嶇墿澶ф垬鍍靛案', 'type': '濉旈槻', 'hot_score': 7432, 'trend': 'stable'},
        {'rank': 38, 'name': 'pvz', 'type': '濉旈槻', 'hot_score': 7365, 'trend': 'down'},
        {'rank': 39, 'name': '鎰ゆ€掔殑灏忛笩', 'type': '浼戦棽', 'hot_score': 7298, 'trend': 'up'},
        {'rank': 40, 'name': '绁炲簷閫冧骸2', 'type': '璺戦叿', 'hot_score': 7232, 'trend': 'stable'},
        {'rank': 41, 'name': '婊戦洩澶у啋闄?, 'type': '浼戦棽', 'hot_score': 7165, 'trend': 'down'},
        {'rank': 42, 'name': '娑傞甫璺宠穬', 'type': '浼戦棽', 'hot_score': 7098, 'trend': 'up'},
        {'rank': 43, 'name': '璺宠垶鐨勭嚎', 'type': '闊充箰', 'hot_score': 7032, 'trend': 'stable'},
        {'rank': 44, 'name': '閽㈢惔鍧?, 'type': '闊充箰', 'hot_score': 6965, 'trend': 'down'},
        {'rank': 45, 'name': '鑺傚澶у笀', 'type': '闊充箰', 'hot_score': 6898, 'trend': 'up'},
        {'rank': 46, 'name': 'Cytus', 'type': '闊充箰', 'hot_score': 6832, 'trend': 'stable'},
        {'rank': 47, 'name': 'Deemo', 'type': '闊充箰', 'hot_score': 6765, 'trend': 'down'},
        {'rank': 48, 'name': '婊氬姩鐨勫ぉ绌?, 'type': '浼戦棽', 'hot_score': 6698, 'trend': 'up'},
        {'rank': 49, 'name': '鍑犱綍鍐插埡', 'type': '浼戦棽', 'hot_score': 6632, 'trend': 'stable'},
        {'rank': 50, 'name': '璺宠垶鐨勭悆', 'type': '浼戦棽', 'hot_score': 6565, 'trend': 'down'},
    ]
    
    return sample_games


def save_douyin_data():
    """淇濆瓨鎶栭煶鏁版嵁鍒癑SON鏂囦欢"""
    games = get_douyin_games()
    today = datetime.now().strftime('%Y-%m-%d')
    
    data = {
        'platform': '鎶栭煶灏忔父鎴?,
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
    
    # 鍚屾椂淇濆瓨鏈€鏂版暟鎹埌 latest.json
    with open(os.path.join(output_dir, 'latest.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"鎶栭煶灏忔父鎴忔暟鎹凡淇濆瓨: {output_file}")
    return data


if __name__ == '__main__':
    save_douyin_data()
