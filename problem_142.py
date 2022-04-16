from heapq import heappush, heappop

def process_logs(logs, n):
    conversation_count = {}

    def increase_conversation_count(user_id):
        if conversation_count.get(sender_id):
            conversation_count[sender_id] += 1
        else:
            conversation_count[sender_id] = 1

    for log in logs:
        log_data = log.split(' ')
        sender_id = log_data[0]
        recepient_id = log_data[1]
        if sender_id == recepient_id:
            increase_conversation_count(sender_id)
        else:
            increase_conversation_count(sender_id)
            increase_conversation_count(recepient_id)

    min_heap = []
    count = 0
    for user_id in conversation_count:
        if count < n:
            heappush(min_heap, (conversation_count[user_id], user_id))
        else:
            if min_heap[0][0] < conversation_count[user_id]:
                heappop(min_heap)
                heappush(min_heap, (conversation_count[user_id], user_id))

        count += 1

    top_users = [convers_user[1] for convers_user in min_heap]
    return top_users


print(process_logs(["88 99 200", "88 99 300", "99 32 100", "12 12 15"], 2))

        

