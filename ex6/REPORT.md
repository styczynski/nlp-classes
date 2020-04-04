# Report

Recognized entities from the first 10 sentences (in TEXT category) are categorized into 4 categories:
1. GOOD - Valid NE
2. MISS - Named Entities that were undetected
3. FAIL - Tokens that are not NE but were recognized as NE
4. PART - Invalid NE (partial detection or separation)

| Entity                  | Result |
|-------------------------|--------|
| Crude                   | FAIL   |
| Oracle                  | FAIL   |
| Europe                  | GOOD   |
| GM                      | FAIL   |
| Harvard School (Public) | PART   |
| Yankees                 | GOOD   |
| Hollywood               | FAIL   |
| Dodgers                 | GOOD   |
| Genome Institute        | GOOD   |
| Singapore               | GOOD   |
| GIS                     | GOOD   |
| SARS                    | FAIL   |
| Phish                   | FAIL   |
| Vermont                 | GOOD   |
| Euro-Scandinavian       | GOOD   |
| Denmark                 | FAIL   |
| Sweden                  | FAIL   |

Summary:
_______________

    GOOD: 8
    MISS: 0
    FAIL: 8
    PART: 1
    TOTAL: 17
_______________