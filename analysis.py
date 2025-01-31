import numpy as np

def structural_analysis(building):
    # 簡単な構造解析ロジックの例
    stress = building.calculate_volume() / 100
    return stress
