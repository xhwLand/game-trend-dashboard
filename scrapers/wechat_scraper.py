"""
寰俊灏忔父鎴忔帓琛屾鐖櫕
鏁版嵁鏉ユ簮锛氬井淇″皬娓告垙涓績鍏紑姒滃崟
"""
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime


def get_wechat_games():
    """
    鑾峰彇寰俊灏忔父鎴忔帓琛屾鏁版嵁
    杩斿洖鏍煎紡锛歔{'rank': 1, 'name': '娓告垙鍚?, 'type': '绫诲瀷', 'hot_score': 鐑害, 'trend': '瓒嬪娍'}]
    """
    games = []
    
    # 妯℃嫙鏁版嵁锛堝疄闄呬娇鐢ㄦ椂鏇挎崲涓虹湡瀹炵埇铏唬鐮侊級
    # 寰俊灏忔父鎴忔帓琛屾鏁版嵁婧愶細https://game.wechat.com/
    
    sample_games = [
        {'rank': 1, 'name': '璺充竴璺?, 'type': '浼戦棽', 'hot_score': 9923, 'trend': 'up'},
        {'rank': 2, 'name': '娆箰鏂楀湴涓?, 'type': '妫嬬墝', 'hot_score': 9856, 'trend': 'stable'},
        {'rank': 3, 'name': '娆箰楹诲皢', 'type': '妫嬬墝', 'hot_score': 9789, 'trend': 'up'},
        {'rank': 4, 'name': '澶╁ぉ璞℃', 'type': '妫嬬墝', 'hot_score': 9723, 'trend': 'down'},
        {'rank': 5, 'name': '鑵捐娆箰鎹曢奔', 'type': '浼戦棽', 'hot_score': 9656, 'trend': 'up'},
        {'rank': 6, 'name': '鎷崇殗鍛借繍', 'type': '鍔ㄤ綔', 'hot_score': 9589, 'trend': 'stable'},
        {'rank': 7, 'name': '鐏煷浜烘垬浜?, 'type': '绛栫暐', 'hot_score': 9523, 'trend': 'up'},
        {'rank': 8, 'name': '妞嶇墿澶ф垬鍍靛案', 'type': '濉旈槻', 'hot_score': 9456, 'trend': 'down'},
        {'rank': 9, 'name': '淇濆崼钀濆崪', 'type': '濉旈槻', 'hot_score': 9389, 'trend': 'stable'},
        {'rank': 10, 'name': '寮€蹇冩秷娑堜箰', 'type': '娑堥櫎', 'hot_score': 9323, 'trend': 'up'},
        {'rank': 11, 'name': '娑堢伃鏄熸槦', 'type': '娑堥櫎', 'hot_score': 9256, 'trend': 'up'},
        {'rank': 12, 'name': '娉℃场榫?, 'type': '娑堥櫎', 'hot_score': 9189, 'trend': 'down'},
        {'rank': 13, 'name': '璐悆铔囧ぇ浣滄垬', 'type': '浼戦棽', 'hot_score': 9123, 'trend': 'stable'},
        {'rank': 14, 'name': '鐞冪悆澶т綔鎴?, 'type': '浼戦棽', 'hot_score': 9056, 'trend': 'up'},
        {'rank': 15, 'name': '閽㈢惔鍧?', 'type': '闊充箰', 'hot_score': 8989, 'trend': 'down'},
        {'rank': 16, 'name': '璺宠垶鐨勭嚎', 'type': '闊充箰', 'hot_score': 8923, 'trend': 'stable'},
        {'rank': 17, 'name': '鑺傚澶у笀', 'type': '闊充箰', 'hot_score': 8856, 'trend': 'up'},
        {'rank': 18, 'name': '绁炲簷閫冧骸', 'type': '璺戦叿', 'hot_score': 8789, 'trend': 'down'},
        {'rank': 19, 'name': '鍦伴搧璺戦叿', 'type': '璺戦叿', 'hot_score': 8723, 'trend': 'up'},
        {'rank': 20, 'name': '澶╁ぉ閰疯窇', 'type': '璺戦叿', 'hot_score': 8656, 'trend': 'stable'},
        {'rank': 21, 'name': '绌胯秺鐏嚎', 'type': '灏勫嚮', 'hot_score': 8589, 'trend': 'up'},
        {'rank': 22, 'name': '鐜嬭€呰崳鑰€', 'type': 'MOBA', 'hot_score': 8523, 'trend': 'down'},
        {'rank': 23, 'name': '鍜屽钩绮捐嫳', 'type': '灏勫嚮', 'hot_score': 8456, 'trend': 'stable'},
        {'rank': 24, 'name': 'QQ椋炶溅', 'type': '绔為€?, 'hot_score': 8389, 'trend': 'up'},
        {'rank': 25, 'name': '璺戣窇鍗′竵杞?, 'type': '绔為€?, 'hot_score': 8323, 'trend': 'down'},
        {'rank': 26, 'name': '娆箰鍧﹀厠澶ф垬', 'type': '灏勫嚮', 'hot_score': 8256, 'trend': 'up'},
        {'rank': 27, 'name': '鍏ㄦ皯椋炴満澶ф垬', 'type': '椋炶灏勫嚮', 'hot_score': 8189, 'trend': 'stable'},
        {'rank': 28, 'name': '闆烽渾鎴樻満', 'type': '椋炶灏勫嚮', 'hot_score': 8123, 'trend': 'down'},
        {'rank': 29, 'name': '閮ㄨ惤鍐茬獊', 'type': '绛栫暐', 'hot_score': 8056, 'trend': 'up'},
        {'rank': 30, 'name': '鐨囧鎴樹簤', 'type': '鍗＄墝', 'hot_score': 7989, 'trend': 'stable'},
        {'rank': 31, 'name': '鑽掗噹琛屽姩', 'type': '灏勫嚮', 'hot_score': 7923, 'trend': 'down'},
        {'rank': 32, 'name': '鎴戠殑涓栫晫', 'type': '娌欑洅', 'hot_score': 7856, 'trend': 'up'},
        {'rank': 33, 'name': '杩蜂綘涓栫晫', 'type': '娌欑洅', 'hot_score': 7789, 'trend': 'stable'},
        {'rank': 34, 'name': '铔嬩粩娲惧', 'type': '浼戦棽', 'hot_score': 7723, 'trend': 'up'},
        {'rank': 35, 'name': '鍏冩ⅵ涔嬫槦', 'type': '浼戦棽', 'hot_score': 7656, 'trend': 'up'},
        {'rank': 36, 'name': '缇婁簡涓緤', 'type': '娑堥櫎', 'hot_score': 7589, 'trend': 'down'},
        {'rank': 37, 'name': '鏉ユ壘鑼?, 'type': '鐩婃櫤', 'hot_score': 7523, 'trend': 'stable'},
        {'rank': 38, 'name': '澶у鏉ユ壘鑼?, 'type': '鐩婃櫤', 'hot_score': 7456, 'trend': 'up'},
        {'rank': 39, 'name': '浣犵敾鎴戠寽', 'type': '绀句氦', 'hot_score': 7389, 'trend': 'down'},
        {'rank': 40, 'name': '璋佹槸鍗у簳', 'type': '绀句氦', 'hot_score': 7323, 'trend': 'stable'},
        {'rank': 41, 'name': '鐙间汉鏉€', 'type': '绀句氦', 'hot_score': 7256, 'trend': 'up'},
        {'rank': 42, 'name': '澶┖鐙间汉鏉€', 'type': '绀句氦', 'hot_score': 7189, 'trend': 'down'},
        {'rank': 43, 'name': '浜斿瓙妫?, 'type': '妫嬬墝', 'hot_score': 7123, 'trend': 'stable'},
        {'rank': 44, 'name': '鍥存', 'type': '妫嬬墝', 'hot_score': 7056, 'trend': 'up'},
        {'rank': 45, 'name': '鍥介檯璞℃', 'type': '妫嬬墝', 'hot_score': 6989, 'trend': 'down'},
        {'rank': 46, 'name': '椋炶妫?, 'type': '妫嬬墝', 'hot_score': 6923, 'trend': 'stable'},
        {'rank': 47, 'name': '澶у瘜缈?, 'type': '妫嬬墝', 'hot_score': 6856, 'trend': 'up'},
        {'rank': 48, 'name': '鏂楀湴涓?, 'type': '妫嬬墝', 'hot_score': 6789, 'trend': 'down'},
        {'rank': 49, 'name': '鍥涘窛楹诲皢', 'type': '妫嬬墝', 'hot_score': 6723, 'trend': 'stable'},
        {'rank': 50, 'name': '骞夸笢楹诲皢', 'type': '妫嬬墝', 'hot_score': 6656, 'trend': 'up'},
    ]
    
    return games


def save_wechat_data():
    """淇濆瓨寰俊鏁版嵁鍒癑SON鏂囦欢"""
    games = get_wechat_games()
    today = datetime.now().strftime('%Y-%m-%d')
    
    data = {
        'platform': '寰俊灏忔父鎴?,
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
    
    # 鍚屾椂淇濆瓨鏈€鏂版暟鎹埌 latest.json
    with open(os.path.join(output_dir, 'latest.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"寰俊灏忔父鎴忔暟鎹凡淇濆瓨: {output_file}")
    return data


if __name__ == '__main__':
    save_wechat_data()
