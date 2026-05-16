"""
涓诲叆鍙ｈ剼鏈?- 杩愯鎵€鏈夌埇铏苟鐢熸垚鏁版嵁
浣跨敤鏂规硶: python main.py
"""
import sys
import os

# 娣诲姞scrapers鐩綍鍒拌矾寰?sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from douyin_scraper import save_douyin_data
from wechat_scraper import save_wechat_data
from ios_us_scraper import save_ios_us_data
from google_us_scraper import save_google_us_data


def run_all_scrapers():
    """杩愯鎵€鏈夌埇铏?""
    print("=" * 50)
    print("寮€濮嬫姄鍙栨父鎴忔鍗曟暟鎹?..")
    print("=" * 50)
    
    results = {}
    
    # 鎶撳彇鍚勫钩鍙版暟鎹?    try:
        print("\n[1/4] 鎶撳彇鎶栭煶灏忔父鎴忔帓琛屾...")
        results['douyin'] = save_douyin_data()
        print("鉁?鎶栭煶鏁版嵁鎶撳彇瀹屾垚")
    except Exception as e:
        print(f"鉁?鎶栭煶鏁版嵁鎶撳彇澶辫触: {e}")
        results['douyin'] = None
    
    try:
        print("\n[2/4] 鎶撳彇寰俊灏忔父鎴忔帓琛屾...")
        results['wechat'] = save_wechat_data()
        print("鉁?寰俊鏁版嵁鎶撳彇瀹屾垚")
    except Exception as e:
        print(f"鉁?寰俊鏁版嵁鎶撳彇澶辫触: {e}")
        results['wechat'] = None
    
    try:
        print("\n[3/4] 鎶撳彇iOS缇庡尯鍏嶈垂娓告垙鎺掕姒?..")
        results['ios_us'] = save_ios_us_data()
        print("鉁?iOS缇庡尯鏁版嵁鎶撳彇瀹屾垚")
    except Exception as e:
        print(f"鉁?iOS缇庡尯鏁版嵁鎶撳彇澶辫触: {e}")
        results['ios_us'] = None
    
    try:
        print("\n[4/4] 鎶撳彇Google Play缇庡尯鍏嶈垂娓告垙鎺掕姒?..")
        results['google_us'] = save_google_us_data()
        print("鉁?Google Play缇庡尯鏁版嵁鎶撳彇瀹屾垚")
    except Exception as e:
        print(f"鉁?Google Play缇庡尯鏁版嵁鎶撳彇澶辫触: {e}")
        results['google_us'] = None
    
    # 姹囨€绘姤鍛?    print("\n" + "=" * 50)
    print("鎶撳彇瀹屾垚姹囨€?")
    print("=" * 50)
    for platform, data in results.items():
        if data:
            print(f"鉁?{data['platform']}: {data['count']} 鏉℃暟鎹?)
        else:
            print(f"鉁?{platform}: 鎶撳彇澶辫触")
    
    return results


if __name__ == '__main__':
    run_all_scrapers()
