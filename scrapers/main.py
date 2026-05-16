"""
主入口脚本 - 运行所有爬虫并生成数据
使用方法: python main.py
"""
import sys
import os

# 添加scrapers目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from douyin_scraper import save_douyin_data
from wechat_scraper import save_wechat_data
from ios_us_scraper import save_ios_us_data
from google_us_scraper import save_google_us_data


def run_all_scrapers():
    """运行所有爬虫"""
    print("=" * 50)
    print("开始抓取游戏榜单数据...")
    print("=" * 50)
    
    results = {}
    
    # 抓取各平台数据
    try:
        print("\n[1/4] 抓取抖音小游戏排行榜...")
        results['douyin'] = save_douyin_data()
        print("✓ 抖音数据抓取完成")
    except Exception as e:
        print(f"✗ 抖音数据抓取失败: {e}")
        results['douyin'] = None
    
    try:
        print("\n[2/4] 抓取微信小游戏排行榜...")
        results['wechat'] = save_wechat_data()
        print("✓ 微信数据抓取完成")
    except Exception as e:
        print(f"✗ 微信数据抓取失败: {e}")
        results['wechat'] = None
    
    try:
        print("\n[3/4] 抓取iOS美区免费游戏排行榜...")
        results['ios_us'] = save_ios_us_data()
        print("✓ iOS美区数据抓取完成")
    except Exception as e:
        print(f"✗ iOS美区数据抓取失败: {e}")
        results['ios_us'] = None
    
    try:
        print("\n[4/4] 抓取Google Play美区免费游戏排行榜...")
        results['google_us'] = save_google_us_data()
        print("✓ Google Play美区数据抓取完成")
    except Exception as e:
        print(f"✗ Google Play美区数据抓取失败: {e}")
        results['google_us'] = None
    
    # 汇总报告
    print("\n" + "=" * 50)
    print("抓取完成汇总:")
    print("=" * 50)
    for platform, data in results.items():
        if data:
            print(f"✓ {data['platform']}: {data['count']} 条数据")
        else:
            print(f"✗ {platform}: 抓取失败")
    
    return results


if __name__ == '__main__':
    run_all_scrapers()
