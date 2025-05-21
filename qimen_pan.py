import datetime
import ephem
import math
from datetime import datetime, timedelta

# 定义八门、九星、八神等
MEN = ["休门", "生门", "伤门", "杜门", "景门", "死门", "惊门", "开门"]
STAR = ["天蓬", "天芮", "天冲", "天辅", "天禽", "天心", "天柱", "天任", "天英"]
GOD = ["值符", "腾蛇", "太阴", "六合", "白虎", "玄武", "九地", "九天"]
JIAZI = ["甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉",
         "甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未",
         "甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳",
         "甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯",
         "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑",
         "甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"]

def get_ganzhi(year, month, day, hour):
    """计算干支"""
    # 简化版干支计算，精确计算需要完整的万年历
    base_date = datetime(1984, 2, 4, 23, 30)  # 1984年立春
    target_date = datetime(year, month, day, hour)
    days = (target_date - base_date).days
    return JIAZI[days % 60]

def get_jieqi(year, month, day):
    """获取当前节气"""
    # 简化版，实际应使用精确的天文计算
    jieqi = ["立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
             "立夏", "小满", "芒种", "夏至", "小暑", "大暑",
             "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
             "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"]
    # 这里应该根据实际节气日期返回，简化处理
    return jieqi[month * 2 - 2] if day < 15 else jieqi[month * 2 - 1]

def get_yuan(year, month, day):
    """获取三元"""
    jieqi = get_jieqi(year, month, day)
    # 简化处理，实际应根据节气计算
    if jieqi in ["冬至", "惊蛰", "清明", "立夏"]:
        return "上元"
    elif jieqi in ["小寒", "春分", "立夏", "芒种"]:
        return "中元"
    else:
        return "下元"

def create_pan(year, month, day, hour):
    """创建奇门盘"""
    ganzhi = get_ganzhi(year, month, day, hour)
    jieqi = get_jieqi(year, month, day)
    yuan = get_yuan(year, month, day)
    
    print(f"时间：{year}年{month}月{day}日{hour}时")
    print(f"干支：{ganzhi}")
    print(f"节气：{jieqi} {yuan}")
    print("\n奇门遁甲排盘：")
    print("-------------------")
    print("  八门：", " ".join(MEN))
    print("  九星：", " ".join(STAR))
    print("  八神：", " ".join(GOD))
    print("-------------------")
    print("注：此为简化版排盘，实际排盘需考虑更多因素")

if __name__ == "__main__":
    now = datetime.now()
    create_pan(now.year, now.month, now.day, now.hour)
