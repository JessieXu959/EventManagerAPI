from typing import List, Dict
from collections import Counter

class EventAnalyzer:
    @staticmethod
    def get_joiners_multiple_meetings_method(events: List[Dict]) -> List[str]:
        
        joiner_counter = Counter()
        for event in events:
            if 'joiners' in event:
                for joiner in event['joiners']:
                    joiner_counter[joiner['name']] += 1

        
        joiners_multiple_meetings = [name for name, count in joiner_counter.items() if count >= 2]
        return joiners_multiple_meetings