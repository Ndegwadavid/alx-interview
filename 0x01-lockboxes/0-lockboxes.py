def canUnlockAll(boxes):
    if not boxes:
        return False
    
    keys = set([0])  
    new_keys = set([0])  
    
    while new_keys:
        current_keys = new_keys
        new_keys = set()
        
        for key in current_keys:
            for box in boxes[key]:
                if box not in keys:
                    new_keys.add(box)
        
        keys.update(new_keys)
    
    return len(keys) == len(boxes)


boxes = [[1], [2], [3], []]  
print(canUnlockAll(boxes))  
