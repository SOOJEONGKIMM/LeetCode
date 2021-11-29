class Solution:
    def dfs(self, n, graph, visited, component):
        if visited[n]:
            return 
        visited[n]=True
        component.append(n)
        for neighbor in graph[n]:
            if not visited[neighbor]:
                self.dfs(neighbor, graph, visited, component)
                
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        visited = {}
        email_merged={}
        for account in accounts:
            emails = account[1:]
            first_email = emails[0]
            #Value of the key if it is in the dictionary. 
            for email in emails:
                graph.setdefault(email, set()).add(first_email)
                graph.setdefault(first_email, set()).add(email)
                visited[email]=False
                email_merged[email] = account[0]
                
        res = []

        for email, account in email_merged.items():
            if visited[email]:
                continue
                
            comp=[]
            self.dfs(email, graph, visited, comp)
            res.append([account]+sorted(comp))
            
        return res