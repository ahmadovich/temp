def sort_by_last_letter(strings):
        def return_last_letter(s):
            
            return s[-1]
        return sorted(strings, key= return_last_letter )

print(sort_by_last_letter(['is','this','is','a','test','string']))

