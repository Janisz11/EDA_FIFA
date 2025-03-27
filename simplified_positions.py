def simplify_position(pos):
    if isinstance(pos, str):
        if 'GK' in pos:
            return 'Goalkeeper'
        elif any(p in pos for p in ['CB', 'LB', 'RB', 'LWB', 'RWB']):
            return 'Defender'
        elif any(p in pos for p in ['CDM', 'CM', 'CAM', 'LM', 'RM']):
            return 'Midfielder'
        elif any(p in pos for p in ['ST', 'CF', 'LW', 'RW']):
            return 'Forward'
    return 'Other'