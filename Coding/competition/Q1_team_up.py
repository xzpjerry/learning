
#!/usr/bin/env python3
def solution(test_cases):
    for case in range(test_cases):
        num_person = int(input('num_person:'))

        team_info = {person: [] for person in range(1, num_person + 1)}

        num_relation = int(input('num_relation:'))
        for relation in range(num_relation):
            raw_source_sink = input('source_person sink_person:').split()
            source = int(raw_source_sink[0])
            sink = int(raw_source_sink[1])
            team_info[source].append(sink)
            team_info[sink].append(source)

        out_put_result = 0
        total_visited = {person: False for person in team_info}

        for person in team_info:
            '''
            The thought is to check every 3 people combination of each
            person one by one, after checking, remove this person
            from the graph and check the next person.
            '''
            total_visited[person] = True
            local_visited = []
            for friend in team_info[person]:
                if total_visited[friend]:
                    continue
                local_visited.append(friend)
                inter = list(filter(lambda x: not total_visited[
                             x] and x not in local_visited and x in team_info[friend], team_info[person]))
                out_put_result += len(inter)

        print('\nResult:', out_put_result)

num_test_case = int(input('num_cases:'))
solution(num_test_case)
