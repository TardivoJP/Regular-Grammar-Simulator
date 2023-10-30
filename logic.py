def setToList(map, key):
    if key in map:
        return list(map[key])
    else:
        print(f"Key '{key}' not found in the map.")
        return []
        
def howConstruct(map, startKey, targetWord, currentWord, iteration, result=None):
    if result is None:
        result = []
    
    if(currentWord == targetWord):
        result.append("Construcao completa!")
        return result
    
    if(len(currentWord) > (len(targetWord) + 1)):
        return None
    
    if(iteration == 1):
        startingKeyRules = setToList(map, startKey)
        updatedCurrentWord = ""
        
        for constructionRule in startingKeyRules:
            updatedCurrentWord = currentWord + constructionRule
            result = howConstruct(map, startKey, targetWord, updatedCurrentWord, (iteration + 1))
            if(result is not None):
                result.insert(0, "Aplicado - (S > " + constructionRule + ") - String atual = '" + updatedCurrentWord + "'")
                return result
            
    if(iteration > 1):
        index = -1
        
        for i in range(len(currentWord)):
            potentialKey = currentWord[i]
            if(potentialKey in map):
                index = i
                keyValue = potentialKey
                break
        
        if(index != -1):
            currentKeyRules = setToList(map, keyValue)
            updatedCurrentWord = ""
            
            for constructionRule in currentKeyRules:
                if(constructionRule == "**"):
                    updatedCurrentWord = currentWord[:index] + currentWord[index + 1:]
                else:
                    updatedCurrentWord = currentWord[:index] + constructionRule + currentWord[index + 1:]
                    
                result = howConstruct(map, startKey, targetWord, updatedCurrentWord, (iteration + 1))
                if(result is not None):
                    result.insert(0, "Aplicado - (" + keyValue + " > " + constructionRule + ") - String atual = '" + updatedCurrentWord + "'")
                    return result
        else:
            return None
        
    return None