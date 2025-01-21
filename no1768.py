def mergeAlternately(word1, word2):
    max_len = len(word1) if len(word1) > len(word2) else len(word2)
    answer = ""
    for i in range(max_len):
        if i < len(word1):
            answer += word1[i]
        if i < len(word2):
            answer += word2[i]
    
    return answer
                