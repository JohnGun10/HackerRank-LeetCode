english_std_count = int(input())
english_std_list = set(map(int,input().strip().split()))
french_std_count = int(input())
french_std_list = set(map(int,input().strip().split()))
print(len(english_std_list.symmetric_difference(french_std_list)))

